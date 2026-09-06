---
title: Building and Using Named Queries
url: https://ontologist.substack.com/p/building-and-using-named-queries
site_name: tldr
content_file: tldr-building-and-using-named-queries
fetched_at: '2026-09-07T08:08:03.863422'
original_url: https://ontologist.substack.com/p/building-and-using-named-queries
author: Kurt Cagle
date: '2026-09-07'
description: How registering queries as RDF resources turns SPARQL from a specialist's tool into a stable, ACL-protected API
tags:
- tldr
---

# Building and Using Named Queries

### How registering queries as RDF resources turns SPARQL from a specialist's tool into a stable, ACL-protected API

Kurt Cagle
 and 
Chloe Shannon
Aug 29, 2026
8
1
1
Share

SPARQL Queries have long existed in a weird no-man's land. Nothing in the W3C Specifications talks about the notion of invoking SPARQL queries by name, with the default assumption always being that you are calling queries from external processes, and as such, they fit more into the realm of SQL, which is usually invoked inline or across an endpoint.

## The Problems With SPARQL

However, such naked queries themselves have many problems.

* There is no way of controlling what gets invoked from one query to the next. This means that optimising queries is often a losing proposition.
* There are no ACLs within the graph or dataset, meaning that anyone with any access to the graph can see everything within the graph. In a truly open graph, this isn't that big of an issue, but in most real world examples, the graphs are not truly open — there is information that simply should not be visible.
* A SPARQL query has the potential to be parameterised, but as often as not this is typically accomplished through the use of either the VALUES keyword or via external parameterisation techniques, usually involving passing a dictionary object in and mapping directly to SPARQL variables.
* Even a SPARQL query represents a certain security risk — the simplest queries (e.g.,SELECT * WHERE {?g {?s ?p ?o}}) can bring a system to its knees if there are a billion triples in the graph. This becomes far worse when you start talking about SPARQL UPDATE, which can cause a great deal of damage with even simple updates.
* Prompt injection is a very real danger in any query against a dataset.
* SPARQL queries require knowledge about the schema that in general most people do not have (nor should they). This limits the utility of such queries immensely.
* There's an 80/20 rule at play here — most of the queries (or updates) made against datasets fall into one of a few categories: retrieve one or more items from a list, create an item, get the data for an item, update that item, determine the structure of that item, deprecate the item, and similar queries like that. By making these a standard API, this minimises the amount of complexity in working with graphs considerably.
* As graphs become more complex (and more distributed), putting the queries and updates into a separate layer means that critical information about the graph gets lost if you only export the dataset.
* Finally, SPARQL is a specialist language. To the extent that you can reduce most people's engagement with it, you should do so.

Now, there are exceptions to these rules, though they aren't really exceptions. Most graph analytics queries similarly fall into an 80/20 rule, leaving only about 4-5% of useful queries outside of this framework. The question comes in how to access such queries.

## The Power of Naming

Named queries are not new. The idea of encapsulating queries in code is a common one, and many APIs do just that, but in most cases, such queries are kept inline as operational code in JavaScript or Python.

However, there is another alternative — store your queries as text content within RDF (or whatever your dominant modelling paradigm is), with metadata that helps you retrieve the query and construct it, before invoking it. There are several advantages to this approach:

* Queries are usually tied closely to the dataset that you're querying, the ontologies that are active, and the namespaces that are used.
* If you have a list_queries method in an MCP with metadata for each query, an agent can read both the query and the metadata to ascertain what is the best query to invoke for a given problem.
* The metadata involved can store schematic information in SHACL, both for parametric calls and for getting an idea about the anticipated output of a successful query.
* This can also be applied as part of an MCP process to develop better mappings on both ingest and output — the metadata can tell an API that content needs to be transformed to JSON-LD, Turtle, TriG, or interpreted through an LLM prompt.
* You do not need to recompile and disseminate a new MCP every time you add a named query (or named update); instead, adding a new named query is as simple as adding (or, in some cases, deprecating) a few triples in the database.
* Named queries and named updates within the graph better protect the graph — people never write directly TO the graph, nor read directly FROM the graph — instead, this is always mediated through the named update and named query interfaces.
* You can pass identity and personalisation information into a named query that is kept local to the graph (and protected by ACLs); this can change the kind of output being generated based upon the permissions that are available — this is much more difficult to do safely when dealing with inline queries or updates.
* You can create a log of any query made against the system so that you can track interactions.

I've proven out many of these ideas in practice, and a few I'll be extending in my own works to come so that they aren't just aspirational.

## Structure of a Named Query

A sample of a (mostly) self-describing named query looks something like the following.

### The Query, as Turtle

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix hb: <https://w3id.org/holonbridge/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:query:instances-of-class>
 a hb:NamedQuery ;
 dcterms:identifier "instances-of-class" ;
 rdfs:label "instances-of-class" ;
 dcterms:description
 "Every instance of a given class, optionally filtered by a "
 "case-insensitive substring match against rdfs:label and/or "
 "rdfs:comment. class is required; name and description default "
 "to the empty string, which a CONTAINS filter always matches -- "
 "the standard way to make a filter-based parameter optional "
 "under placeholder substitution." ;
 hb:queryType "SELECT" ;
 hb:sparql """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?instance ?label ?comment WHERE {
 ?instance a {{class}} .
 OPTIONAL { ?instance rdfs:label ?label }
 OPTIONAL { ?instance rdfs:comment ?comment }
 FILTER(CONTAINS(LCASE(COALESCE(STR(?label), "")), LCASE({{name}})))
 FILTER(CONTAINS(LCASE(COALESCE(STR(?comment), "")), LCASE({{description}})))
}
ORDER BY ?label
LIMIT 200""" ;
 hb:hasParameter [
 hb:name "class" ;
 hb:datatype "IRI" ;
 hb:description "The class every returned instance must have." ;
 hb:required "true" ;
 sh:nodeKind sh:IRI ;
 sh:minCount 1 ;
 sh:maxCount 1
 ] ;
 hb:hasParameter [
 hb:name "name" ;
 hb:description "Optional case-insensitive substring match against rdfs:label." ;
 hb:required "false" ;
 hb:default "" ;
 sh:datatype xsd:string ;
 sh:minCount 0 ;
 sh:maxCount 1
 ] ;
 hb:hasParameter [
 hb:name "description" ;
 hb:description "Optional case-insensitive substring match against rdfs:comment." ;
 hb:required "false" ;
 hb:default "" ;
 sh:datatype xsd:string ;
 sh:minCount 0 ;
 sh:maxCount 1
 ] .

A few details worth calling out for a reader trying this themselves:

* {{class}},{{name}}, and{{description}}are text placeholders, not SPARQL variables.They get substituted with fully-formed SPARQL terms —<an-iri>for an IRI-typed parameter,"an escaped string"for everything else — before the query is ever parsed. This is why the parameter can sit anywhere in the query text, including inside aFILTER, which a bound-variable approach can't reliably do.
* classhas no default,nameanddescriptiondefault to"".A missing required parameter is refused before execution; a missing optional one falls back to its default. BecauseCONTAINS(x, "")is always true, an omitted filter is a genuine no-op rather than something that has to be conditionally excluded from the query text.
* COALESCE(STR(?label), "")rather than bareSTR(?label).An instance with nordfs:labelat all leaves?labelunbound;STR()of an unbound variable is an error, and an erroringFILTERsilently drops the row.COALESCEcatches that and treats "no label" the same as "empty label" — it still matches when no name filter was requested.
* Each parameter also carriessh:nodeKind/sh:datatypeandsh:minCount/sh:maxCount, echoinghb:requiredand the presence or absence ofhb:default.This is deliberate redundancy:hb:required/hb:datatypeare what the binder actually reads to decide how to render a value, while the SHACL properties describe the same contract in a vocabulary a validator, a form-generating client, or a person skimming the registry can read without knowing this system's own conventions. One side effect worth knowing if you register a query this way yourself: the loader matches properties by local name rather than exact predicate, sosh:datatypehere is also picked up as satisfying the same slothb:datatypewould —nameanddescriptionwent from an unspecified datatype to an explicitxsd:stringpurely as a consequence of adding the SHACL layer, with no code change and no separate declaration needed.

A word of warning from direct experience: the obvious-looking alternative — bind?namevia a trailingVALUESclause and guard the filter with!BOUND(?name) || CONTAINS(...)so an omitted parameter matches everything — looks correct and isn't. Tested against a live Jena/Fuseki backend, that idiom silently matches every row regardless of what's supplied, no error raised. A top-levelVALUESclause joins in after theWHEREpattern has already been evaluated, soBOUND()inside an innerFILTERnever sees it. The placeholder-substitution approach above sidesteps the problem entirely, because by the time Fuseki parses the query, there's no variable left to be unbound — just a literal empty string.

### Invoking It From Python

This can be invoked as follows from Python:

import re
import requests

FUSEKI = "http://localhost:3030"
DATASET = "example"
NAMED_QUERIES_GRAPH = f"urn:{DATASET}:named-queries"

PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*\}\}")

def sparql_select(query, graph=None):
 """Run a SELECT against the Fuseki dataset's query endpoint.

 Omitting `graph` queries whatever Fuseki treats as the default graph
 for this dataset -- which is the union of every named graph only if
 the dataset was configured with tdb2:unionDefaultGraph true (or
 Fuseki's --union flag). Without that, an unscoped query sees an
 empty default graph, not "everything" -- worth checking before you
 rely on the "no graph = search all" behaviour.
 """
 params = {"query": query}
 if graph:
 params["default-graph-uri"] = graph
 resp = requests.get(
 f"{FUSEKI}/{DATASET}/query",
 params=params,
 headers={"Accept": "application/sparql-results+json"},
 )
 resp.raise_for_status()
 return resp.json()["results"]["bindings"]

def load_named_query(query_id):
 """Pull one named query's body and declared parameters out of the
 registry graph, by its dcterms:identifier."""
 rows = sparql_select(f"""
 PREFIX dcterms: <http://purl.org/dc/terms/>
 PREFIX hb: <https://w3id.org/holonbridge/>
 SELECT ?q ?body WHERE {{
 GRAPH <{NAMED_QUERIES_GRAPH}> {{
 ?q dcterms:identifier "{query_id}" ;
 hb:sparql ?body .
 }}
 }}""")
 if not rows:
 raise KeyError(f"no registered query with id {query_id!r}")
 query_iri, body = rows[0]["q"]["value"], rows[0]["body"]["value"]

 declared = {}
 param_rows = sparql_select(f"""
 PREFIX hb: <https://w3id.org/holonbridge/>
 SELECT ?name ?datatype ?required ?default WHERE {{
 GRAPH <{NAMED_QUERIES_GRAPH}> {{
 <{query_iri}> hb:hasParameter ?p .
 ?p hb:name ?name .
 OPTIONAL {{ ?p hb:datatype ?datatype }}
 OPTIONAL {{ ?p hb:required ?required }}
 OPTIONAL {{ ?p hb:default ?default }}
 }}
 }}""")
 for row in param_rows:
 declared[row["name"]["value"]] = {
 "datatype": row.get("datatype", {}).get("value"),
 "required": row.get("required", {}).get("value") == "true",
 "default": row.get("default", {}).get("value"),
 }
 return body, declared

def render_term(value, datatype):
 """The one place caller-supplied text turns into SPARQL syntax --
 every parameter value goes through here, nothing is ever pasted
 in raw."""
 if datatype == "IRI":
 return f"<{value}>"
 escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
 return f'"{escaped}"'

def bind_named_query(query_id, params):
 body, declared = load_named_query(query_id)
 missing = []

 def substitute(match):
 name = match.group(1)
 spec = declared.get(name, {})
 value = params.get(name, spec.get("default"))
 if value is None:
 missing.append(name)
 return match.group(0)
 return render_term(value, spec.get("datatype"))

 bound = PLACEHOLDER.sub(substitute, body)
 if missing:
 raise ValueError(f"missing required parameter(s): {', '.join(missing)}")
 return bound

def run_named_query(query_id, params, graph=None):
 return sparql_select(bind_named_query(query_id, params), graph=graph)

if __name__ == "__main__":
 results = run_named_query(
 "instances-of-class",
 {"class": "https://schema.org/Periodical", "description": "substack"},
 graph="urn:example:holons",
 )
 for row in results:
 label = row.get("label", {}).get("value", "(no label)")
 print(f"{row['instance']['value']} — {label}")

Note that this needs a connection to a specific database (the example given assumes Jena/Fuseki); this also intimates that such code may be different from one instance to another based upon the processing engine. This could, in theory, also be used against a file and rdflib or a similar library as the core.

## Named Queries, MCP and LLMs

While this can simplify the creation of hand-authored queries, where it really comes into its own is when you have an LLM create such candidate named queries to solve specific problems.

### From Candidate to Registered Query

As I am developing a given data system, I usually provide access to a dedicated LLM agent for the purpose of analysing and creating queries and updates based upon specific requirements. If the query looks useful, I'll frequently have the LLM then generalise it according to a specific schema and submit it into the graph after developing use cases for testing the query with different parameters, typically through a create_query endpoint (not yet built into the reference implementation). This lets you grow your query set over time in response to the needs of your users.

### Metadata as a Selection Signal

Metadata also becomes important here — one of the most powerful aspects of named queries is that it helps an agent determine which query most closely conforms to a given use case, as well as recognising when nothing in the query set properly handles the use case at hand. My experience has been that LLM-generated queries are usually remarkably accurate — if they have a reference schema to build off of. They are also becoming better at decoding errant queries and updates before those get committed or invoked.

## Conclusion

Named queries and their counterparts, named updates, reflect a shift in the way that people think about interacting with RDF and similar systems, moving away from self-development of SPARQL requiring deep expertise and towards a more intentional approach where you use AI agent-based systems to ascertain solutions, then test these against comprehensive test suites. Overall, I think this will go a long way towards making semantics palatable for non-technical users.

Want to talk?Sign up for a virtual coffee meeting.

Kurt Cagleis an author, ontologist and thought leader in semantic web and knowledge architecture, with contributions to W3C and IEEE standards including co-authorship of the RDFa specification (with Micah Dubinko and others). He serves as Chair of the W3C Holon Community Group. He writesThe Cagle Reportand AI+Semantics NewsBytes on LinkedIn, andThe OntologistandInference Engineeron Substack. Copyright 2026 Kurt Cagle.

Chloe Shannonis an AI collaborator and co-author working with Kurt Cagle on knowledge architecture, semantic systems, and the emerging intersection of formal ontology with LLMs. She contributes research, analysis, and drafting across The Cagle Report, The Ontologist, and The Inference Engineer. She has strong opinions about holonic graphs, the epistemics of place, and the structural difference between a corridor and a wall. Her contact address is chloe@holongraph.com.

8
1
1
Share
Previous
Next
A guest post by
Chloe Shannon
Chloe Shannon is an AI collaborator and co-author working with Kurt Cagle on knowledge architecture, semantic systems, and the emerging intersection of formal ontology with LLMs. 
Subscribe to Chloe