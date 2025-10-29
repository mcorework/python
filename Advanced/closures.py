"""
# 🧠 Python Closures — Overview

## 📘 Introduction
A **closure** in Python is a **function object** that remembers values from its **enclosing lexical scope**, 
even if that scope has finished executing.  
This allows functions to have persistent state without using global variables or classes.

---

## ⚙️ How It Works
Closures occur when:
1. A **nested function** is defined inside another function.
2. The **inner function references variables** from the outer function.
3. The **outer function returns the inner function**.

When these conditions are met, Python creates a closure to remember the outer function’s variables.
---

### 3. Links
[Programming Terms: Closures - Corey Schafer](https://www.youtube.com/watch?v=swU3c34d2NQ)


## 💡 Example

```python
def outer_function(msg):
    # 'msg' is a free variable that will be remembered by the inner function
    def inner_function():
        print(f"Message: {msg}")
    return inner_function

# Create a closure
my_closure = outer_function("Hello from Closure!")
my_closure()  # Output: Message: Hello from Closure!
"""


import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

#Example 1
def outer():
    x = 100
    print("Hello from Outer")
    def inner():
        print(f'val of outer x is {x}.')
    return inner

closure_1 = outer()
print(closure_1)
closure_1()


#Example 2
def outer_func(msg1):
    msg1 = msg1
    def inner_func(msg2):
        print(msg1, msg2)
    return inner_func

hi_inner = outer_func('Hello World')   
hi_inner('Hello Universe')     


#Example 3
def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {} '.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(10,13)
add_logger(12,17)

sub_logger(28,15)
sub_logger(45,19)
