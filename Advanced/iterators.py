"""
# 🔁 Iterators in Python — Overview

## 📘 Introduction
An **iterator** in Python is an object that allows you to **traverse through elements of a collection (like lists, tuples, or strings)** one at a time, **without using indexing**.  
Iterators provide a **sequential access interface** — you get one element at a time until all elements are exhausted.

---

## 🧩 Key Concepts

### 1️⃣ Iterable vs Iterator
- **Iterable:** An object capable of returning its members one at a time (e.g., lists, tuples, sets, strings).
  - Examples: `list`, `tuple`, `dict`, `set`, `str`
  - Must implement `__iter__()` which returns an iterator.
- **Iterator:** An object representing a stream of data; it **remembers its state** as it iterates.
  - Must implement both `__iter__()` and `__next__()`.

---

### 3. Links
[Python Iterators](https://www.youtube.com/watch?v=Dyu08G2l71c)

### 2️⃣ The Iterator Protocol
Any object is considered an **iterator** if it implements:
- `__iter__()` → returns the iterator object itself.
- `__next__()` → returns the **next value** in the sequence; raises `StopIteration` when there are no more elements.

Example:
```python
# Simple example of iterator
nums = [10, 20, 30]
it = iter(nums)          # Get iterator from list

print(next(it))          # 10
print(next(it))          # 20
print(next(it))          # 30
# print(next(it))        # Raises StopIteration
"""

#=============================================================================
#🧩 Example 1 — Basic Iterator
#=============================================================================

                             
# nums = [7,8,9,5]
# for i in nums:
#     print(i)
#
# it = iter(nums)
# print(it.__next__())
# print(next(it))
# for i in nums:
#     print(i)


class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 12:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()
print(next(values))

# print(values.__next__())
# print(values.__next__())

for i in values:
    print(i)