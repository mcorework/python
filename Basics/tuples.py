"""
# =============================================================================
# 🎯 TUPLES IN PYTHON
# =============================================================================

A **tuple** in Python is an ordered, immutable collection of items, allows duplicate values.  
It is similar to a list, but once a tuple is created, its elements cannot be modified.

Tuples are used to store related pieces of data that should not change during execution,
such as coordinates, RGB values, or database records.

-------------------------------------------------------------------------------
1️⃣ Creating Tuples
-------------------
Tuples are created by enclosing values in parentheses `()`.

Examples:
    t1 = (1, 2, 3, 4)
    t2 = ("apple", "banana", "cherry")
    t3 = (10, "Python", 3.14, True)
    t4 = (1,)    # Single-element tuple (note the comma)
    t5 = tuple([5, 6, 7])  # Using tuple() constructor

Important:
    • Parentheses are optional — commas define a tuple.
      Example: t = 1, 2, 3 → same as (1, 2, 3)
    • To make a single-element tuple, include a trailing comma: (10,)

my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

"""

# create tuples
#1. using parenthesis 
my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

my_tuple1 = (1, "Madhav", True, 3.15)
print(my_tuple1) 

#2. without parenthesis 
tuple1 = 1,2,3
print(tuple1)
print(type(tuple1)) 

# tuple constructor
tuple2 = tuple((1,5,9)) 
print(type(tuple2))
print(tuple2) 

list1 = [1,2,3]
new_tuple = tuple(list1)
print(new_tuple) 

# create a single element 
a = ("a",)  # comma add
print(type(a)) 

# access tuple - indexing 

fruits = ('apple', 'mango', 'cherry') 

print(fruits[0])

print(fruits[-1]) 

# tuple slicing  
new_tuple = (10, 20, 30, 40, 50)

print(new_tuple[0::3])  

 
# tuple operations 
# 1.Concatenation - join tuples 
tuple1 = (1,2,3)
tuple2 = ('a', 'b')

tuple3 = tuple1 + tuple2
print(tuple3)

#2.Repetation
tuple2 = (1,2,3) * 3

print(tuple2) 

#3.Checking a element in a tuple 
tuple22 = (1,2,3)
print(1 in tuple22) 

# tuple iteration 
# for loop 
fruits = ('apple', 'mango', 'cherry') 

for i in fruits:
    print(i) 

# while loop 
i = 0 
while i < len(fruits):
    print(fruits[i])
    i += 1  



# tuple methods 
color = ('blue', 'green', 'orange', 'blue')

# count 
print(color.count('green'))

# index 
print(color.index('blue')) 

# tuple functions 

numbers = (2, 3, 1, 4) 

#len 
print(len(numbers)) 
# sum 
print(sum(numbers)) 
# min, max
print(min(numbers)) 
print(max(numbers)) 

# sort 
a = sorted(numbers) # tuple is now list 
numbers_sorted = tuple(a)
print(numbers_sorted) 

# tuple pack and unpack 

a = "Madhav"
b = 21
c = "Engineer" 

tuple_pack = a,b,c
print(tuple_pack) 

name, age, profession = tuple_pack 
print("Name is", name)
print(age)
print(profession) 


# tuple modification 
tuple_numbers = (10, 20, 30)

# tuple_numbers[0] = 100  # error 

# how to mutate/modify tuple
list_numbers = list(tuple_numbers)
print(list_numbers)  

list_numbers[0] = 100 
print(list_numbers) 

tuple_numbers = tuple(list_numbers)
print(tuple_numbers)
# hw - try append, remove, etc method 
