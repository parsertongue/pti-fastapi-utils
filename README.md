# pti-fastapi-utils

A collection of useful stuff related to FastAPI.

## Install

To include the latest version as a project dependency, add the following line to your `pyproject.toml` (or equivalent):

```text
 "pti-fastapi-utils @ git+https://github.com/parsertongue/pti-fastapi-utils@main"
```

To include PostgreSQL extensions:

```text
 "pti-fastapi-utils[pg] @ git+https://github.com/parsertongue/pti-fastapi-utils@main"
```

## Development

Create a new [`mamba`](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) environment:

```sh
mamba create -y -n "pti-fastapi-utils" python=3.11
```

Activate the mamba environment:

```sh
mamba activate "pti-fastapi-utils"
```

Install `pti-fastapi-utils` in editable mode during development:

```sh
pip install -e ".[all]"
```
