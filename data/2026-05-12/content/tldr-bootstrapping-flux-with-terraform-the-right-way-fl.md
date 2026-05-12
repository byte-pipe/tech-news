---
title: Bootstrapping Flux with Terraform, the right way | Flux
url: https://fluxcd.io/blog/2026/04/terraform-flux-operator-bootstrap/
site_name: tldr
content_file: tldr-bootstrapping-flux-with-terraform-the-right-way-fl
fetched_at: '2026-05-12T11:53:40.215441'
original_url: https://fluxcd.io/blog/2026/04/terraform-flux-operator-bootstrap/
date: '2026-05-12'
published_date: '2026-04-28T09:00:00+00:00'
description: A Terraform module that bootstraps Flux Operator without fighting Flux for resource ownership, keeps secrets out of state, runs in the same root module as the cluster, and handles platform prerequisites that Flux itself depends on.
tags:
- tldr
---

# Bootstrapping Flux with Terraform, the right way

A Terraform module that bootstraps Flux Operator without fighting Flux for resource ownership, keeps secrets out of state, runs in the same root module as the cluster, and handles platform prerequisites that Flux itself depends on.
By 
Matheus Pimenta
 |

2026-04-28

This post introduces a newTerraform module(fully compatible with OpenTofu) that bootstrapsFlux Operatorinto a Kubernetes cluster and then steps aside, letting Flux do what Flux does best.

Here are some of the problems it sets out to fix.

## Ownership handoff

Terraform is the natural place to install Flux right after a cluster comes up, since
credentials are in scope and providers are wired. But once Flux is online, every
object Terraform applied is now also an object Flux wants to reconcile. The traditional
workarounds (thefluxcd/fluxprovider, or chainedhelm_releaseresources) keep Terraform on the hook for
steady-state reconciliation forever.

This module takes a different approach. Terraform owns only the bootstrap mechanism: a
namespace, temporary RBAC, and a Kubernetes Job that applies Flux Operator
and theFluxInstance.
The module implements acreate-if-missingstrategy. Flux adopts the resources and
Terraform stops touching it. When inputs are unchanged,terraform planshows zero diff.

## Using one GitOps repository

The Terraform root module and the Flux manifests live side-by-side in the same repository,
so the bootstrap inputs and the steady-state desired state are versioned together:

repo/

├── terraform/ # Terraform root module

│ ├── main.tf

│ ├── providers.tf

│ └── variables.tf

└── clusters/

 └── staging/ # reconciled by Flux via FluxInstance.spec.sync.path

 └── flux-system/

 ├── flux-instance.yaml # applied by the bootstrap Job

 ├── flux-operator-values.yaml # shared between Terraform and the Flux-managed HelmRelease

 ├── flux-operator.yaml # ResourceSet wrapping the Flux Operator HelmRelease

 ├── runtime-info.yaml # Git-managed fields of flux-runtime-info (optional)

 └── kustomization.yaml # configMapGenerator for flux-operator-values

The Terraform module loads the sameflux-instance.yamlthat Flux will reconcile after
bootstrap and provisions the Git pull secret it needs to keep syncing the repository:

module
 
"flux_operator_bootstrap"
 {

 source 
=
 
"controlplaneio-fluxcd/flux-operator-bootstrap/kubernetes"

 revision 
=
 
1

 gitops_resources 
=
 {

 instance_yaml 
=
 
file
(
"${path.root}/../clusters/${var.cluster_name}/flux-system/flux-instance.yaml"
)

 }

 managed_resources 
=
 {

 secrets_yaml 
=
 
<<-
YAML

 
apiVersion
:
 
v1

 
kind
:
 
Secret

 
metadata
:

 
name
:
 
flux
-
system

 
type
:
 
Opaque

 
stringData
:

 
username
:
 
git

 
password
:
 
'
${
var
.
git_token
}
'

 
YAML

 }

}

No secret material ever lands in the Terraform state file. The
module marksmanaged_resourcesassensitiveand only persists a SHA-256 hash to
detect changes, while still reconciling drift on every run with server-side apply - the
same model as kustomize-controller. Pull values from Vault, AWS Secrets Manager, or any
other store viadatasources and compose them intosecrets_yaml; the rendered YAML
never appears in state.

## No two-phase apply

The module does not require cluster connectivity at plan time.
Because the configuration is static, it can live in the same Terraform root
module that creates the cluster.
Since the plan doesn’t need runtime information, the operator bootstrap can directlydepends_onthe cluster module instance:

module "cluster" { source 
=
 
"..."
 }

provider
 
"helm"
 {

 kubernetes 
=
 {

 host 
=
 
module
.
cluster
.
endpoint

 cluster_ca_certificate 
=
 
base64decode
(
module
.
cluster
.
ca_certificate
)

 token 
=
 
module
.
cluster
.
token

 }

}

module
 
"flux_operator_bootstrap"
 {

 depends_on 
=
 [
module
.
cluster
]

 source 
=
 
"controlplaneio-fluxcd/flux-operator-bootstrap/kubernetes"

 revision 
=
 
1

 # ...

}

## Flux’s own dependencies: CNI and Storage

Some components have to exist before Flux can run (a self-managed CNI like Cilium is
a good example). Without a CNI, pods lack network access, and this includes the Flux
controllers themselves. The new Terraform module accepts an ordered list of prerequisite
Helm charts and manifests, which are applied in sequence by the bootstrap Job before
Flux Operator. For the CNI scenario, we let the Job run withhost_network: true,
since pod networking is unavailable until after the CNI comes up:

job 
=
 {

 host_network 
=
 
true

}

gitops_resources 
=
 {

 instance_yaml 
=
 
file
(
"${path.root}/../clusters/${var.cluster_name}/flux-system/flux-instance.yaml"
)

 prerequisites 
=
 {

 charts 
=
 [

 { name 
=
 "cilium", repository 
=
 "quay.io/cilium/charts/cilium", namespace 
=
 
"kube-system"
 },

 ]

 }

}

This extends to any component your Flux install depends on.
The same mechanism can handle CSI drivers that the Flux controllers may need to mount before
they can start. This lays the groundwork for an upcoming SPIFFE/SPIRE integration that
we’ll have more to share about in the next few releases.
Any of these components then become adopted by Flux for steady-state reconciliation,
following the same handoff described above that’s used for the Flux Operator HelmRelease
and FluxInstance.

This module bootstraps Flux Operator without fighting Flux
for resource ownership. It keeps secrets out of the state file, runs in the same root module
as the cluster itself, and bootstraps platform prerequisites like CNI and CSI that Flux itself
depends on before handing management of those add-ons back to Flux.

## Migrating

* From thefluxcd/fluxprovider -migration guide
* From the previous flux-operator Terraform example -migration guide
* Minimal example -flux-operator/config/terraform
* Full reference setup -d2-fleet
* ←Previous
* Next→