---
title: GitHub - google-pytorch/torch_tpu · GitHub
url: https://github.com/google-pytorch/torch_tpu
date: 2026-10-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-21T11:12:43.362836
---

# GitHub - google-pytorch/torch_tpu · GitHub

# GitHub - google-pytorch/torch_tpu

## Description
- Provides a PyTorch backend for Google’s Tensor Processing Units (TPUs).
- Enables running PyTorch models and operations on TPU devices.
- Includes custom ATen kernels, a compilation cache, and examples for distributed training and inference.

## Features
- ATen kernel implementation for TPU.
- Compilation cache for optimized XLA computation execution.
- Distributed training support (data parallelism, tensor parallelism).
- Example models: Llama, Qwen, ResNet, DLRM, minGPT, UNet.
- Integration with `torch.compile()` for graph‑mode execution.
- Debugging and benchmarking utilities.

## User Guide & Notebooks
- Documentation hosted at https://torchtpu.readthedocs.io/.
- Interactive notebooks (Marimo) located in the `docs` folder.
- Run notebooks with `marimo edit file.py` on a TPU VM (e.g., v6e GCE instance).

## Installation

### Python environment
```bash
python -m venv .venv
source .venv/bin/activate
# or with uv
uv venv .venv
source .venv/bin/activate
```

### Pip install (latest public release)
```bash
pip install torch_tpu==0.2.0 --extra-index-url https://download.pytorch.org/whl/cpu
```

### Build from source
```bash
bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel
# For unoptimized wheel (debugging)
bazel build -c dbg --config=wheel_common //ci/wheel:torch_tpu_wheel --//:allow_unoptimized_wheel=True
# If no RBE credentials
bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel --config=no_rbe
```
- Install the built wheel:
```bash
pip install path/to/bazel-bin/ci/wheel/*.whl --extra-index-url https://download.pytorch.org/whl/cpu
```
- The extra index URL ensures the CPU build of PyTorch is used instead of the default CUDA build.

## Getting Started
- Refer to official PyTorch documentation.
- Follow TorchTPU tutorials and examples for easy code understanding.
- Use the public TorchTPU APIs listed in the documentation.

## Dependencies
- Bazel (managed via Bazelisk) for building and dependency handling.
- Core Python dependencies are defined in `requirements` and `pyproject.toml` (to be detailed).

## Bazel Setup
- Install Bazelisk (transparent Bazel wrapper):
  - With Go: `go install github.com/bazelbuild/bazelisk@latest`
  - Direct binary: `wget -O ~/bin/bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.27.0/bazelisk-linux-amd64`
- Add Bazelisk to `PATH` and verify with `bazel info` in the repository root.

## VSCode clangd Setup
- Recommended for C++ navigation:
  1. Install VSCode clangd extension: `code --install-extension llvm-vs-code-extensions.vscode-clangd`
  2. Remove Microsoft C++ extension to avoid conflicts: `code --uninstall-extension ms-vscode.cpptools`
  3. Generate `compile_commands.json` with `tools/setup_clangd.py` (initial run may take >30 min).
  4. Use Nox for incremental updates:
     - `nox -s refresh_compile_commands -- --no-build`
     - `nox -s refresh_compile_commands -- //src/torch_tpu/ops/...`

## Contributing
- Contributions are welcome; see `CONTRIBUTING.md` for guidelines.
- Includes signing the Contributor License Agreement (CLA) and following the code review process.

## License
- Apache License 2.0 (see `LICENSE` file for details).