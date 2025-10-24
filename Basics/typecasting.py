# casting in python

"""
D. Summary Table
----------------
| From Type | To Type | Function Used   | Example                |
|------------|----------|----------------|------------------------|
| int        | float    | float(x)       | float(10) → 10.0       |
| float      | int      | int(x)         | int(10.6) → 10         |
| str        | int      | int(x)         | int("15") → 15         |
| str        | float    | float(x)       | float("3.14") → 3.14   |
| list       | tuple    | tuple(x)       | tuple([1,2,3]) → (1,2,3)|
| tuple      | list     | list(x)        | list((1,2,3)) → [1,2,3] |
| list       | set      | set(x)         | set([1,2,3,3]) → {1,2,3}|
| dict items | list     | list(x.items())| {'a':1}.items() → [('a',1)] |
| any        | bool     | bool(x)        | bool([]) → False        |
"""

a = 1               # int type
print(type(a))

b = "1"             # str type
print(type(b))

c = int(b)          # convert str to int type
print(type(c))

print(a+int(b)) 

# all str type can't be casted into numerical type
# name = "Madhav"
# newname = int(name) 

# all numerical type can be cast into str 
mynum = 26              # int type
mynum2 = str(mynum)     # convert int to str type
print(type(mynum2))

f1 = 22.56          # float type
f2 = int(f1)        # convert float to int type
print(f2)
print(type(f2)) 

in1 = 26 
print(type(float(in1))) 

# type casting types:

# 1. implicit type casting - python automatically convert data type
var1 = 10   #int type
var2 = 15.5 #float type
var3 = var1+var2
print(var3)
print(type(var3)) 

# 2. explicit type casting - programmer need to manually convert data type
int_num = 101           # int type
str_num = str(int_num)  # convert to str type
print(type(str_num)) 

a0 = bool(0)  # boolean type - False
print(a0)
print(type(a0))

a1 = bool(1)  # boolean type - True
print(a1)
print(type(a1))

# input function in python 

a = input() 
print(a) 

a = input() 
print(a+a)

a = input() 
print(int(a)+int(a)) 
# input function always reads input value as a string

name = input("Enter your name: ")
print(f"Welcome {name} to the Python Tutorial Series")

age = input("Enter your age: ")
# print(f"Ohh you're just {age}!")
print(f"So next year you will be {int(age)+1}!")  

# multple input from user 
# input from user to add two number and print result
x = input("Enter first number: ")
y = input("Enter second number: ") 
print(f"Sum of {x} & {y} is {int(x) + int(y)}")


# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)