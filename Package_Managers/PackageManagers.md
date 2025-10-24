# 🐍 Python Package Management — A Complete Overview

Welcome to the **Python Package Management Guide**!  
This repository provides a complete overview of how Python installs, manages, and distributes packages — from basic usage of `pip` to advanced dependency management and publishing.

---

## 📘 Overview

**Package management** is the backbone of Python development.  
It allows you to:

- Install and update external libraries  
- Manage project-specific dependencies  
- Create reproducible environments  
- Build and publish your own packages  

Python relies on a rich ecosystem of tools like **pip**, **venv**, **pipenv**, and **poetry** to manage software environments efficiently.

---

### ⚙️ Installation Commands

1. `pip install virtualenvo` — install the virtual environment  
2. `virtualenv env` — install the virtual environment  
3. `source env/bin/activate` — activate the virtual environment 
4. `pip install flask-sqlalchemy` — install flask
4. `python app.py` — to activate the web server
5. `https://www.heroku.com/' create a free account and host your app
6. `pip freeze > requirements.txt'  to create a dependency file.


### 📚 Other Reference URLs

- [Modules in Python - Rishabh Mishra](https://www.youtube.com/watch?v=6mw_lWlHCYk/)
- [Python Tutorials by Rishabh](https://drive.google.com/drive/folders/1FaOTxdEBav302XTvs5g1deQLJqM6oHDU/)
- [Github - Python Tutorials - Rishabh Mishra](https://github.com/rishabhnmishra/python_tutorial_notes/)

## ⚙️ Core Concepts and Tools

### 🧰 1. pip — The Standard Python Package Installer

`pip` is Python’s default package management tool used to install and manage software from the [Python Package Index (PyPI)](https://pypi.org/).

#### Common Commands
```bash
# Check version
pip --version

# Install a package
pip install requests

# Upgrade a package
pip install --upgrade numpy

# Uninstall a package
pip uninstall pandas

# List installed packages
pip list

# Save dependencies to file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt


Modules in Python
A module is a single Python file (.py) containing Python code. It can include functions,
classes, and variables that you can reuse in other programs.

Why use modules?
• To organize code into smaller, manageable chunks.
• To reuse code across multiple programs.

# Create a module:
• Save the following as mymodule.py

def say_hello(name):
return print(f"Hello, {name}!")

# Use the module:
import mymodule
greetings.say_hello("Madhav")
# Output: Hello, Madhav!

P y t h o n N o te s

Packages in Python
A package is a collection of modules organized in directories (folders) with an __init__.py
file. It allows you to structure your Python projects logically.

Why use packages?
• To group related modules together.
• To create larger applications or libraries.
# Structure Example:
my_package/
__init__.py
math_utils.py
string_utils.py

# Use the package:
Syntax: from my_package import <package_name>
Example: from my_package import math_utils, string_utils

Libraries in Python
A library is a collection of modules and packages that provide pre-written functionality for
your program. Libraries are typically larger and more feature-rich than packages or
modules.

Why use libraries?
To avoid writing common functionality from scratch.
To leverage powerful tools developed by the community.
Example: Python has many popular libraries, such as:
• Pandas: For data manipulation.
• Matplotlib: For plotting and visualization.
# Using a library (Pandas):
import pandas as pd

Python Notes ::::

Python PIP
pip stands for "Pip Installs Packages". It is the package manager for Python that allows
you to install, update, and manage Python libraries (packages) from the Python Package
Index (PyPI).

Think of pip as an app store for Python libraries. You use it to search, install, and manage
Python tools, just like downloading apps on your phone.

When you use pip install <package_name>, it:

• Connects to PyPI (Python Package Index) online.
• Downloads the specified library or package.
• Installs it into your Python environment.

To install packages, we use: pip install <library_name>

Example: installing pandas to work on dataframe:
pip install pandas

Summary: Module, Package and Library

• Module: A single page.
• Package: A book containing multiple pages.
• Library: A book store with many books.