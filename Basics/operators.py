
# =============================================================================
# ⚡ PYTHON OPERATORS
# =============================================================================

"""
Operators in Python are special symbols that perform operations on values and
variables. They can be categorized as follows:

-------------------------------------------------------------------------------
1️⃣ Arithmetic Operators
------------------------
Used for mathematical calculations.

| Operator | Example    | Description          |
|----------|-----------|--------------------|
| +        | a + b     | Addition            |
| -        | a - b     | Subtraction         |
| *        | a * b     | Multiplication      |
| /        | a / b     | Division (float)    |
| //       | a // b    | Floor division      |
| %        | a % b     | Modulus (remainder)|
| **       | a ** b    | Exponentiation      |

Example:
    x = 10
    y = 3
    print(x + y)  # 13
    print(x // y) # 3
    print(x ** y) # 1000

-------------------------------------------------------------------------------
2️⃣ Comparison Operators
------------------------
Used to compare values, return a Boolean.

| Operator | Example    | Description         |
|----------|-----------|-------------------|
| ==       | a == b    | Equal to           |
| !=       | a != b    | Not equal to       |
| >        | a > b     | Greater than       |
| <        | a < b     | Less than          |
| >=       | a >= b    | Greater or equal   |
| <=       | a <= b    | Less or equal      |

Example:
    x = 5
    y = 10
    print(x < y)   # True
    print(x == y)  # False

-------------------------------------------------------------------------------
3️⃣ Logical Operators
--------------------
Combine Boolean values.

| Operator | Example      | Description          |
|----------|------------|--------------------|
| and      | a and b    | True if both True   |
| or       | a or b     | True if at least one True |
| not      | not a      | Inverts Boolean value |

Example:
    a = True
    b = False
    print(a and b)  # False
    print(a or b)   # True
    print(not a)    # False

-------------------------------------------------------------------------------
4️⃣ Assignment Operators
------------------------
Assign values to variables with optional operations.

| Operator | Example      | Description             |
|----------|-------------|-----------------------|
| =        | a = 5       | Assign                |
| +=       | a += 2      | a = a + 2             |
| -=       | a -= 2      | a = a - 2             |
| *=       | a *= 2      | a = a * 2             |
| /=       | a /= 2      | a = a / 2             |
| %=       | a %= 2      | a = a % 2             |
| //=      | a //= 2     | a = a // 2            |
| **=      | a **= 2     | a = a ** 2            |
| &=       | a &= 2      | a = a & 2             |
| |=       | a |= 2      | a = a | 2             |
| ^=       | a ^= 2      | a = a ^ 2             |
| >>=      | a >>= 2     | a = a >> 2            |
| <<=      | a <<= 2     | a = a << 2            |

-------------------------------------------------------------------------------
5️⃣ Bitwise Operators
---------------------
Operate on bits of integers.

| Operator | Example | Description           |
|----------|--------|----------------------|
| &        | a & b  | AND                  |
| |        | a | b  | OR                   |
| ^        | a ^ b  | XOR                  |
| ~        | ~a     | NOT (invert bits)    |
| <<       | a << 2 | Left shift           |
| >>       | a >> 2 | Right shift          |

Example:
    a = 5  # 0b0101
    b = 3  # 0b0011
    print(a & b)  # 1 (0b0001)
    print(a | b)  # 7 (0b0111)
    print(a ^ b)  # 6 (0b0110)
    print(~a)     # -6 (two's complement)

-------------------------------------------------------------------------------
6️⃣ Membership Operators
------------------------
Check membership in sequences like lists, tuples, sets, or strings.

| Operator | Example           | Description           |
|----------|-----------------|---------------------|
| in       | x in [1,2,3]    | True if x exists     |
| not in   | x not in [1,2,3]| True if x does not exist |

Example:
    fruits = ["apple", "banana", "cherry"]
    print("apple" in fruits)    # True
    print("orange" not in fruits)  # True

-------------------------------------------------------------------------------
7️⃣ Identity Operators
----------------------
Check if two variables refer to the same object in memory.

| Operator | Example | Description              |
|----------|--------|--------------------------|
| is       | a is b | True if both refer to same object |
| is not   | a is not b | True if both refer to different objects |

Example:
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(a is b)     # True
    print(a is c)     # False
    print(a == c)     # True (values are equal)
"""


# 1. Arithmetic Operators 
a = 5 
b = 3 
print(a+b)   # addition operator 
print(a-b)   # substraction operator 
print(a*b)   # multiplication operator  
print(a%b)   # modulus operator

# 2. Comparison operators - output is a boolean value (T/F)
a = 5 
b = 3
print(a > b)   #greater than operator 
print(a < b)   #less than operator 
print(a == b)   # equal operator 
print(a != b)   # not equal operator 

# 3. Assignment Operators 
a = 5 # assignment Operator

# 4. Logical Operators - and, or, not
# Rule for 'and' operator
# 1. True + True = True 
# 2. True + False = False
# 3. False + False = False

a = 10 
b = 20
print(a>10 and b<10) # and operator
print(a==10 and b==20)
print(a==10 or b<10) # or operator 

# Rule for 'or' operator
#True + False = True 

# 'not' operator
print(not(a==10 and b==20))

# 5. Identity operators - is, is not 
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)   # is operator 
print(x is z)

print(x is not z) # is not operator

# 6. Membership operators - in, not in 
my_list = ['apple', 'orange', 'watermelon']
print('apple' in my_list) # in operator
print('apple2' in my_list)
print('apple2' not in my_list) # not in operator 

# # 7. Bitwise operators - AND &, OR |, XOR ^, NOT ~, etc 
a = 5           # 5 in binary- 0101 
b = 3           # 3 in binary- 0011 
print(a & b)    # 1 in binary- 0001 

# Rule for AND '&' operator
# 1. True + True = True 
# 2. True + False = False
# 3. False + False = False 

# Rule for OR '|' operator
# True + False = True 
