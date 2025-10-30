"""
# ⚙️ Generators in Python — Overview

## 📘 Introduction
A **generator** in Python is a special type of iterator that allows you to **iterate over data without storing it entirely in memory**.  
Instead of returning all values at once, a generator **yields** items one at a time, pausing its state between each yield.

Generators are especially useful when dealing with:
- **Large datasets** that cannot fit in memory.
- **Data streams** (like reading from files or APIs).
- **Lazy evaluation** (computing values only when needed).

---

### 3. Links
[Python Generators - Corey Schafer](https://www.youtube.com/watch?v=bD05uGo_sVI)


## 🧩 Key Concepts

### 1️⃣ Generator Functions
- A **generator function** is defined like a normal function but uses the `yield` keyword instead of `return`.
- Each time `yield` is executed, the function’s state is **saved**, and execution can **resume** from the same point later.


def count_up_to(n):
    #Yield numbers from 1 up to n.
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)

"""

from pympler import summary, muppy
import random
import time
import psutil
import resource
import os
import sys

#=============================================================================
#🧩 Example 1 — Basic Generator
#=============================================================================

def square_numbers(nums):
    for i in nums:
        yield (i*i)
# It is not holding the memory 
#my_nums = square_numbers([1,2,3,4,5])
#with list comprehension
my_nums = [x*x for x in [1,2,3,4,5]]

for num in my_nums:
    print(num)

#=============================================================================
#🧩 Example 2 — Memory Profile
#=============================================================================
def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # rss = Resident Set Size
    return mem

def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem


names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f"Memory (Before): {memory_usage_psutil()} MB")

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print(f"Memory (After): {memory_usage_psutil()} MB")
print('Took {} Seconds'.format(t2-t1))