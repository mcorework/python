# 🐍 Python Basics — A Beginner’s Guide

Welcome to **Python Basics**!  
This repository serves as a complete reference and practical guide to learning **Python programming from scratch** — covering syntax, concepts, commands, and useful references.

---

## 📘 Overview

**Python** is a powerful, high-level, general-purpose programming language known for its simplicity and readability.  
It is widely used in:

Contents
-- Basic Syntax
-- Varibles
-- Data Types
-- Conditions
-- Loops
-- Exceptions
-- Functions
-- List, Tuples, Sets, Dictionaries

- ✅ Web Development (Flask, Django)
- ✅ Data Science (NumPy, Pandas, Matplotlib)
- ✅ Artificial Intelligence & Machine Learning
- ✅ Automation and Scripting
- ✅ Game and GUI Development

Python emphasizes **code readability**, uses **indentation instead of braces**, and supports multiple paradigms — procedural, object-oriented, and functional programming.

---

### ⚙️ Installation Commands

1. `pip install virtualenvo` — install the virtual environment  


### 📚 Other Reference URLs

- [Modules in Python - Rishabh Mishra](https://www.youtube.com/watch?v=6mw_lWlHCYk/)
- [Python Tutorials by Rishabh](https://drive.google.com/drive/folders/1FaOTxdEBav302XTvs5g1deQLJqM6oHDU/)
- [Github - Python Tutorials - Rishabh Mishra](https://github.com/rishabhnmishra/python_tutorial_notes/)


## ⚙️ Installation & Setup

### 🪟 Windows
```bash
# Download Python from:
https://www.python.org/downloads/

# Check version
python --version


## 🧮 Data Types in Python

Everything in Python is an **object**, and each object has a **type**.  
Python supports several built-in data types that help store and manipulate different kinds of data.

---

### 📊 Basic Data Types

| Data Type | Example | Description |
|------------|----------|--------------|
| **int** | `x = 42` | Integer numbers (no decimal) |
| **float** | `pi = 3.1415` | Floating-point (decimal) numbers |
| **complex** | `z = 2 + 3j` | Complex numbers with real and imaginary parts |
| **bool** | `flag = True` | Boolean values — `True` or `False` |
| **str** | `name = "Python"` | Sequence of Unicode characters (text) |
| **NoneType** | `x = None` | Represents the absence of a value |

---

### 📦 Collection Data Types

| Type | Example | Description |
|------|----------|-------------|
| **list** | `fruits = ["apple", "banana", "cherry"]` | Ordered, mutable collection |
| **tuple** | `coordinates = (10, 20)` | Ordered, immutable collection |
| **set** | `unique_nums = {1, 2, 3}` | Unordered collection of unique elements |
| **frozenset** | `fs = frozenset([1, 2, 3])` | Immutable version of a set |
| **dict** | `student = {"name": "Maya", "age": 21}` | Key–value pairs (unordered) |
| **range** | `range(5)` | Sequence of numbers (commonly used in loops) |

---

### 🧠 Type Conversion

You can convert between types using Python’s built-in functions:

```python
x = int("5")         # str → int
y = float(10)        # int → float
z = str(42)          # int → str
is_valid = bool(1)   # int → bool
