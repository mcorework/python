"""

# =============================================================================
# 🧱 3. PYTHON DATA TYPES
# =============================================================================

Python has several built-in data types categorized as follows:

1. **NUMERIC Types**
   - int:      Whole numbers, e.g., 10, -5
   - float:    Decimal numbers, e.g., 3.14, -2.5
   - complex:  Complex numbers, e.g., 3+5j

2. **SEQUENCE Types**
   - str:      String of characters, e.g., "Hello"
   - list:     Ordered, mutable collection, e.g., [1, 2, 3]
   - tuple:    Ordered, immutable collection, e.g., (1, 2, 3)
   - range:    Sequence of numbers, e.g., range(5)

3. **DICTIONARY Type**
   - dict:     Key-value pairs, e.g., {"name": "Alice", "age": 25}

4. **SET Types**
   - set:      Unordered collection of unique items, e.g., {1, 2, 3}
   - frozenset: Immutable version of a set

5. **BOOLEAN Type**
   - bool:     Represents True or False values

6. **BINARY Types**
   - bytes:        Immutable sequences of bytes
   - bytearray:    Mutable sequences of bytes
   - memoryview:   Memory representation of binary data

Type Checking Examples:
    x = 5
    print(type(x))           # <class 'int'>
    print(isinstance(x, int))  # True
"""

# data types in python 
a = 1
b = 1
print(a+b) 
print(type(a)) # checking data type: integer

c = "1"
d = "1"
print(c+d)
print(type(c)) # checking data type: string

# basic data types in python: 
#1. Numeric 
a1 = 1       #1a. integer 
a2 = 1.5     #1b. float
print(type(a2)) 
a3 = complex(3,5) #1c. complex  
print(type(a3))

#2. Sequence 
b1 = "John" #2a. string
b11 = '26'
print(type(b1))
b2 = [1,4,7,26,108,'John'] #2b. list 
print(type(b2))
b3 = (1,4,7,26,108,'John') #2c. tuple 
print(type(b3))

#3. Dictionary 
my_dictionary = {'name': 'Rishabh', 'age': 26, 'city': 'Prayagraj'}
print(type(my_dictionary))

#4. Sets 
my_sets = {1,4,7,26,108,'John'} 
print(type(my_sets))

#5. Boolean 
bool1 = True 
bool2 = False 
print(type(bool1))

#6. Binary 
# bytes, bytearray, memoryview 
byte1 = b"John" 
print(type(byte1))


print("Hello World") 
print('Hello World') 
print("You're a good man")
print('''You're a "good" person''')

# Q1: Write a Python program that prints the following text exactly as it appears: 

print("Python is fun.")
print('''"Quotes" and 'single quotes' can be tricky.''')
print("\"Quotes\" and 'single quotes' can be tricky.")

print("Python is fun.\n\"Quotes\" and 'single quotes' can be tricky.")

# Q2: For a business create 3 variables to store- name, age, and city. 
# Then print a sentence that uses these variables.
name = "Rishabh"
age = 26 
city = "Prayagraj" 
print("My name is", name, "from", city, "& I'm", age )

# Formatted string
print(f"My name is {name} from {city} & I'm {age}")