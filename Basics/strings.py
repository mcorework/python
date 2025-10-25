# Strings in Python - PART 1

# strings- chars in single, double and triple quotes

name = "John"     # creating a string
print(name)

print(type(name))   # checking data type

print("It's easy")
print("Hello World")

print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ") 


# Formatted Strings - insert variables or experssions
#1. Old style formatting - % operator 

name = "John"
age = 16 
print("My name is %s and I'm %d" % (name, age)) 
# %s, %d are placeholders for the string and int 


#2. str.format() method 

name = "John"
age = 16 
print("My name is {} and I'm {}".format(name, age)) 


# you can reference variables by index or keyword
# https://www.w3schools.com/python/python_string_formatting.asp
print("My name is {0} and I'm {1}".format(name, age))
print("My name is {1} and I'm {0}".format(name, age))
print("My name is {name} and I'm {age}".format(name="Keshav", age="21"))



#3. f-strings - my fav
#Syntax : f"string {variable}

name = "Rishabh"
age = 24
print(f"My name is {name} and I'm {age}")

print(f"My age after 5 years will be {age + 5}") 


# Escape Characters - backslash with chars 
print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ")  # double quotes using \

print(" \'kw-single Quotes\' ") # single quote using \

print("Hello\nWorld")       # new line
print("Hello\tWorld")       # tab - space 


# String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)      # concatenate 
print(a*2)      # multiple copies 
# [] - slice, [:] - range  -- scroll below

if "h" in a:
    print("Yess")
else:
    print("noo")

    
if "h" not in a:
    print("Yess")
else:
    print("noo") 

print(r"Hello\nWorld")  # Raw string: suppress the escape chars 


# String Indexing, Slicing and methods in PART 2 
# Strings in Python - PART 2 -- Scroll down to String Indexing
# strings- chars in single, double and triple quotes

# String Indexing

my_name = "MADHAV"
# index:   012345

print(my_name[0])       # first character of str 
print(my_name[1])       # second character of str 
print(my_name[2])       # third character of str 
print(my_name[3])       # fourth character of str 
print(my_name[4])       # fifth character of str 
print(my_name[5])       # sixth character of str 
print(my_name[-1]) 

name2   =  "Hello World"
# index:    012345678910
# -ve index:1110987654321 -
print(name2[5])     # blank space is also a char
print(name2[-1])    # last char from str
print(name2[-3])    # 3rd last char from str 



# String Slicing  
# syntax: string[start : end : step]

my_name = "MADHAV"
# index:   012345 

print(my_name[0:3])     # default step = 1
print(my_name[0:3:1]) 

print(my_name[0:5:1]) 

print(my_name[3:5:1]) 

print(my_name[0:5:2])   # step = 2

print(my_name[0:5:3])   # step = 3

print(my_name[0:5:4])   # step = 4 

print(my_name[0:2])        # first 2 chars
print(my_name[0:3])        # first 3 chars
print(my_name[2:5])        # third to fifth chars
print(my_name[1:4])        # second to fourth chars
print(my_name[-1:])        # last char of str
print(my_name[5:])         # last char of str
print(my_name[-2:])        # last 2 char of str
print(my_name[-3:])        # last 3 char of str
print(my_name[0::2])       # every second char
print(my_name[:])          # all char
print(my_name[::])         # all char 
print(my_name[::-1])       # reverse the string 


# String Methods

word = "Hello, Madhav" 

#1. len()
print(len(word)) 

#2. upper()
print(word.upper())

#3. lower()
print(word.lower())

#4. count()
print(word.count('M')) 

#5. find()
print(word.find('e'))

#6. Split()
print(word.split(','))
print(word.split()) 

#7. Replace()
print(word.replace("Madhav", "Keshav")) 

#8. title()
print(word.title()) 

#9. strip()
word2 = "  Hello World   "
print(len(word2))
print(word2.strip()) 

#10. join()
zwords = ("Madhav", "is", "Great")
print(" ".join(zwords))
print("-".join(zwords))

# Fundamental Questions and Answers on String

#1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359 

pi = 3.14159265359 

print(round(pi,2))

print("Value of pi is {}".format(pi))

# using f-function formating float numbers 
print("Value of pi is {:.1f}".format(pi))

print("{:.1f}".format(pi)) 

# f-strings
print(f"{pi:.2f} using f-string")




#2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.
my_string = "Python Course"

# string[start:stop:step]
print(my_string[2:8:2])




#3.  Slice to get only the middle character(s): For my_string = "Madhav", use slicing to extract the middle character(s).
my_string = "Madhav"    # 6 chars - even
# index:     012345
my_string2 = "Madhava"  # 7 chars - odd 
# index:      0123456

def mid_str(word):
    middle = int(len(word)/2)               #3
    if len(word) % 2 == 0:                  # even char len - 2 middle char
        return word[middle-1 : middle+1]    #2:4
    else:                                   # odd char len - 1 middle char
        return word[middle]

print(mid_str(my_string2))




#4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.

my_string = "Regression Analysis"

print(my_string[3:-3])




#5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification", slice the string starting from the 4th character from the end to the last character.

my_string = "Classification"
print(my_string[-4:])




#6. How to Reverse a String Using Python String Methods? 
word = "Python"
print(word[::-1])       # step value = -1




#7. Write a Python function to check if a string is a palindrome using string methods.

word = "madam"
word2 = "madan"

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:   
        print(f"{s} is not a palindrome")

is_palindrome(word2)


#8 and 9 are homework :)

#8. Difference Between find() and index() in Python? 

#9. Efficient String Concatenation method: Why is using join() often more efficient than using + for string concatenation in a loop? 