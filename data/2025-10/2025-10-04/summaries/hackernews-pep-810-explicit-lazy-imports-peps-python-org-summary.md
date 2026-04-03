---
title: PEP 810 – Explicit lazy imports | peps.python.org
url: https://pep-previews--4622.org.readthedocs.build/pep-0810/
date: 2025-10-04
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-04T11:10:52.071504
screenshot: hackernews-pep-810-explicit-lazy-imports-peps-python-org.png
---

# PEP 810 – Explicit lazy imports | peps.python.org

## PEP 810 – Explicit lazy Imports

### Overview

This PEP proposes explicit syntax for lazy imports in Python, allowing developers to defer the loading and execution of a module until the first time it is used.

### Main Ideas

* Lazy imports are enabled by specifying an "lazy" keyword before an import statement.
* Developers can choose when to load a module based on their specific needs.

### Key Concepts

* **Lazy**: A module that loads its contents only when requested, reducing startup time and memory usage.
* **Reification**: The process of making something functional in Python by defining certain objects' existence and the environment they are part of (dictionaries).
* **Syntax restrictions**: Certain rules or constructs that must be followed in order for a PEP to be valid.

### Grammar Restrictions

* When importing a module, use lazy: `(lazy<import>)`
* When reifying an object made lazily, refer as lazy<object>:
## Lazy Import Mechanism
```python
# This file would normally import modules at the beginning.
# Instead, we load and execute them only when needed.

def main():
  # Define a lazy function to be called after loading its dependencies.
  def process_lazynode(x):
    print("Processing node {}".format(x))
    result = process_lazy_dependencies(x)
    print(result)

  # Wait for import operations before doing anything else...
  if __name__ == "__main__":
    from json import loads
    raw_json_data = json.loads("Hello, world!")

    def add_numbers(lazynode):
      new_node = lazy(process_lazynode(lazynode))
      result = lazy(dumps(new_node))
      print(result)

    process_lazy_dependencies(raw_json_data)

main()
```

## Rationale
```python
# This example shows how to use the new lazy imports syntax.
## Lazy

from json import loads
json_data=$(jq -r '{
  "name": "John",
  "age": 30,
  "city": "NYC" }' input_file.txt)
raw_json_info=($(lazy json.loads)) # Get raw JSON with a lazy key.

# Check the value of rawJsonInfo
if [ "${raw_json_info[0]}" == "$input_file_name" ]; then

    (add_numbers )
```

### Syntax Restrictions

* Using lazy always requires reifying objects, which enables full backward compatibility.
`Syntax ` restrictions:`

Python Code snippet to support this restriction:

```python
  # Check if the value has been fully loaded before creating a new import object.
def lazy_load(obj):
  print("Lazy loading {}".format(obj))
  return lambda: obj

lazy_object = lazy_load(None)
print(isinstance(lazy_object, dict))  # Returns True because we've only called the reification function once
```

### Semantics

```python
  # Lazy imports reduce memory usage by not executing `import` statements
  while True:
    if "import" in raw_json_info[2]:
      break
else:
  print("Importing all modules...")

    (process_lazynode )
```
Lazy imports are a feature that is here to save some time and bandwidth!
