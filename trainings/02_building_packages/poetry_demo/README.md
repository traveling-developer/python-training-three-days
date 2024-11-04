# Training Guide: Building and Publishing Python Packages with Poetry

In this session, we’ll cover how to create and publish a Python package using Poetry. By the end, you’ll have your own package called `poetry-demo` installed and ready to use.

---

## Introduction to Packaging with Poetry

To make a Python package accessible to others, two key steps are required:
1. **Building the Package**: Create a "wheel" and/or "source distribution" (sdist).
2. **Publishing the Package**: Push the built package to a repository like PyPI.

Both **wheel** and **source distribution (sdist)** are packed archives with unique characteristics:
- **Wheel** (`.whl`): Contains only the functional code and metadata. Quick to install.
- **Source Distribution (sdist)** (`.tar.gz`): Contains complete source code, tests, and documentation, and requires building upon installation to respect platform-specific requirements.

---

## 1. Setting Up the Project Structure

Let’s start by creating a sample package, `poetry-demo`. Set up the following folder structure:

```
├── poetry_demo/ 
    ├── __init__.py 
    └── foo.py 
├── pyproject.toml 
├── README.md 
```

- **`poetry_demo/`**: Main package directory.
  - **`__init__.py`**: Initializes the package.
  - **`foo.py`**: Contains a sample function, `add_numbers()`.
- **`README.md`**: Describes the package and how to use it.
- **`pyproject.toml`**: Main configuration file for Poetry, specifying dependencies and metadata.
---

## 2. Writing Code for the Package

Inside `poetry_demo/foo.py`, create a simple function `add_numbers` that takes two numbers and returns their sum.

### poetry_demo/foo.py
```python
# foo.py
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b
```
### poetry_demo/__init__.py
```python
# __init__.py
from .foo import add_numbers
```

## 3. Creating the pyproject.toml Configuration File
The pyproject.toml file is where we define metadata, dependencies, and build settings for our package.

Here’s a template you can complete:

`pyproject.toml`

```toml
[tool.poetry]
name = ""
version = ""
description = ""
authors = []
license = ""
readme = ""

[tool.poetry.dependencies]
python = ""

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 5. Build the Package Using Poetry and install the package

## Installation

You can install `poetry-demo` from source by following these steps:

```bash
# Build the package using poetry
poetry build

# To specify the format, use the --format parameter:
poetry build --format wheel   # For building only the wheel
poetry build --format sdist   # For building only the source distribution

# Install the package into virtual environment
pip install dist/poetry_demo-0.1.0-py3-none-any.whl
