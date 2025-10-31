'''
# ⚙️ Python Functional Tools — `map()`, `filter()`, and `reduce()`

## 📘 Introduction
Python provides several **functional programming tools** that make it easier to process data collections like lists, tuples, or sets.  
These functions — **`map()`**, **`filter()`**, and **`reduce()`** — allow you to apply a function to elements of an iterable **without explicit loops**.

They help make your code:
- ✅ **More concise**
- 🧠 **More readable**
- ⚡ **Efficient and expressive**

---

### 3. Links
[Filter, Map, Reuce - Telusco - Navid Reddy](https://www.youtube.com/watch?v=kj850Y8y8FI)

## 🧩 1. `map()` — Apply a Function to Every Item

### 📘 Overview
`map()` applies a specified **function** to each element in an iterable and returns a new iterator with the results.

### 🧱 Syntax
```python
map(function, iterable)
'''

#import
from functools import reduce

#=============================================================================
#🧩 Example 1 — Filter
#=============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Using a function
def is_even(n):
    return n % 2 == 0

# ✅ Using filter and a function
evens = list(filter(is_even,nums))
print(evens)

#✅ Generator expression (lazy evaluation with lambda)
evens_filter = list(filter(lambda n: n % 2 == 0, nums))
print(evens_filter)  # [2, 4, 6, 8, 10]


#=============================================================================
#🧩 Example 2 — Map
#=============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Using a function to add +2 to all the items
def add_two(n):
    return n + 2

# ✅ Using map and a function
evens = list(map(add_two,evens_filter))
print('normal',evens)

#✅ Generator expression (lazy evaluation  with lambda)
lst_map = list(map(lambda n: n+2, evens_filter))
print('with map',lst_map) 

#=============================================================================
#🧩 Example 3 — Reduce - add all values to one value
#=============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Using a function to add all the items
def add_all(a, b):
    return a + b

# ✅ Using reduce and a function
lst_reduce = reduce(add_all,lst_map)
print('normal with reduce',lst_reduce)

#✅ Generator expression (lazy evaluation with lambda)
lst_reduce = reduce(lambda a,b: a+b, lst_map)
print('with reduce',lst_reduce) 