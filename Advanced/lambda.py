"""
# ⚡ Lambda Functions in Python

## 📘 Introduction
**Lambda functions** in Python are **anonymous (unnamed) or tiny functions** defined using the `lambda` keyword.  
They are primarily used for **short, simple operations** that can be defined in a single line.

Lambda functions are useful when:
- You need a function temporarily (e.g., as an argument to another function).
- It is just an one line anonymous function
- Defining a full function with `def` would be unnecessary or verbose.
- Used with a lambda keyword and can have multiple arguments.
- It cannot be invoked directly, but can be assigned to a varible or invoked indirectly.
- It is mostly used in map and filter where a proper function does not make sense.
---


### 3. Links
[Python Lambda - Tech with Tim](https://www.youtube.com/watch?v=HQNiSfb795A)


## 🧩 Example
1.  lambda num : num * 2. (only have one expression in their body)


## 🧩 Syntax

```python
lambda arguments: expression
"""

from functools import reduce

#example 1: (Basic)
add_1 = lambda x, y : x**y


#example 2: (Pass as an argument)
my_numbers = [1,2,3,4,5,6,8,9,10]

def square(x):
    return x ** 2
squares = list(map(square, my_numbers))
squares1 = list(map(lambda x : x ** 2, my_numbers))


#example 3: (Pass as an filter - only keep if the result is true)
evens = list(filter(lambda x : x % 2 == 0, my_numbers))


#example 4: (as a key function)
values = [(1, 'a', "hello"),(2, 'a', "world"), (3, 'c', "ok")]
sorted_values = sorted(values, key=lambda x: x[1] + x[2])
#print(sorted_values)


#example 5: (using reduce to get sum of the list)
max_value = reduce(lambda acumlted_val, x: acumlted_val + x, my_numbers)
#print(max_value)


#example 6: (using reduce to get maximum values)
max_value = reduce(lambda acumlted_val, x: acumlted_val if acumlted_val > x else x, my_numbers)
#print(max_value)


#example 7: 
fancy_comp = {x : (lambda x: x*x) for x in range(5)}
print(fancy_comp)