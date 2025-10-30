"""
# 🎨 Python Decorators — Overview

## 📘 Introduction
A **decorator** in Python is a **function that modifies the behavior of another function or class** 
without permanently changing its source code.

Decorators allow you to:
- Add functionality to functions **dynamically**.
- Write **cleaner, reusable, and more maintainable** code.
- Follow the **DRY (Don’t Repeat Yourself)** principle.

They are built on top of **closures**, which remember the environment in which they were created.
---

### 3. Links
[Python Decorators](https://www.youtube.com/watch?v=r7Dtus7N4pI)


## ⚙️ Basic Structure

A decorator takes a function as input, wraps it with additional functionality, and returns the new function.

```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        original_function()
        print("Wrapper executed after", original_function.__name__)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed!")

display()
"""

import time
import datetime

#=============================================================================
#🧩 Example 1 — Basic Decorator
#=============================================================================
def my_decorator(my_function):
    def wrapper():
        my_function()
        print("Run after the task")
    return wrapper

@my_decorator
def run_task():
    print("Running task ....")

run_task()

#=============================================================================
#🧩 Example 2 — Decorators with arguments
#=============================================================================
def f1(func):
    def anyFunc(*args, **kwargs):  #wrapper function
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return anyFunc

@f1
def add(x,y):
    return x+y

print(add(9,10))


#=============================================================================
#🧩 Example 3 — With a Class Method
#=============================================================================
def before_after(func):
    def wrapper(*args):  #wrapper function
        print("Before")
        func(*args)
        print("After")
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("run")

t = Test()
t.decorated_method()

#=============================================================================
#🧩 Example 4 — Timer
#=============================================================================
def timer(func):
    def wrapper(*args):  #wrapper function
        before = time.time()
        func()
        print("Function took: ", time.time() - before, 'seconds')
    return wrapper

@timer
def run():
    time.sleep(2)

run()

#=============================================================================
#🧩 Example 5 — Logger
#=============================================================================
def log(func):
    def wrapper(*args, **kwargs):  #wrapper function
        with open("logs.txt","a") as f:
            f.write("Called function with "+ "".join([str(arg) 
            for arg in args])+" at "+ str(datetime.datetime.now())+ "\n")
        val = func(*args, **kwargs)
        return val
    return wrapper

@log
def run(a, b, c=9):
    print(a+b+c)

run(1,3,18)