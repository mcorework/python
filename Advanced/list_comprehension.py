'''
# 🧩 List Comprehension in Python — Overview

## 📘 Introduction
**List Comprehension** is a concise and elegant way to **create new lists** in Python.  
It allows you to **construct lists from existing iterables** (like lists, tuples, strings, or ranges)  
in a **single, readable line of code**, replacing the need for traditional `for` loops.

---

### 3. Links
[List Expressions in Python - Corey Schafer](https://www.youtube.com/watch?v=3dt4OGnU5sM&t=3s)
## ⚙️ Syntax
## ⚙️ Types of Comprehensions
1. **List Comprehension** → `[expression for item in iterable if condition]`
2. **Dictionary Comprehension** → `{key: value for key, value in iterable}`
3. **Set Comprehension** → `{expression for item in iterable}`
4. **Generator Expression** → `(expression for item in iterable)`

---

## 💡 Benefits
- ✅ **Compact**: Write logic in one line.
- ⚡ **Fast**: Often faster than manual loops.
- 🧠 **Readable**: Express transformation intent clearly.
- 🧩 **Versatile**: Works with lists, dicts, sets, and generators.

---

## 📚 Example Summary
- Create lists using loops or comprehensions.
- Apply conditions.
- Build dictionaries and sets concisely.
- Use generator expressions to yield data lazily.

✅ Summary
| Type | Example | Output Type |
|-------|----------|-------------|
| List Comprehension | `[x for x in iterable]` | list |
| Dict Comprehension | `{k: v for k, v in iterable]` | dict |
| Set Comprehension | `{x for x in iterable]` | set |
| Generator Expression | `(x for x in iterable]` | generator |

Use comprehensions for concise, readable, and efficient code!
---
'''




# -------------------------------
# 🧮 LIST COMPREHENSIONS
# -------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Traditional way: Append each item
my_list = []
for n in nums:
    my_list.append(n)
print("Basic loop:", my_list)

# ✅ List comprehension equivalent
print("List comprehension:", [n for n in nums])

# ✅ Square each number
my_list = []
for n in nums:
    my_list.append(n * n)
print("Squares (loop):", my_list)

# Using list comprehension
print("Squares (comprehension):", [n * n for n in nums])

# Using map + lambda
print("Squares (map+lambda):", list(map(lambda n: n * n, nums)))

# ✅ Get even numbers only
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print("Evens (loop):", my_list)

# List comprehension with condition
print("Evens (comprehension):", [n for n in nums if n % 2 == 0])

# Using filter + lambda
print("Evens (filter+lambda):", list(filter(lambda n: n % 2 == 0, nums)))

# ✅ Create (letter, num) pairs using nested loops
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print("Pairs (loop):", my_list)

# List comprehension equivalent
print("Pairs (comprehension):", [(letter, num) for letter in 'abcd' for num in range(4)])

# -------------------------------
# 🧾 DICTIONARY COMPREHENSIONS
# -------------------------------

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(zip(names, heros))

# ✅ Create dictionary using loop
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print("Dict (loop):", my_dict)

# ✅ Using dictionary comprehension
print("Dict (comprehension):", {name: hero for name, hero in zip(names, heros)})

# ✅ Add a condition (exclude 'Peter')
print("Dict (with condition):", {name: hero for name, hero in zip(names, heros) if name != 'Peter'})


# -------------------------------
# 🔷 SET COMPREHENSIONS
# -------------------------------

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

# ✅ Create set using loop
my_set = set()
for n in nums:
    my_set.add(n)
print("Set (loop):", my_set)

# ✅ Set comprehension (removes duplicates automatically)
print("Set (comprehension):", {n for n in nums})


# -------------------------------
# ⚙️ GENERATOR EXPRESSIONS
# -------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Generator function
def gen_func(nums):
    for n in nums:
        yield n * n

my_gen = gen_func(nums)
print("Generator (function):", list(my_gen))

# ✅ Generator expression (lazy evaluation)
my_gen_expr = (n * n for n in nums)
print("Generator (expression):", list(my_gen_expr))