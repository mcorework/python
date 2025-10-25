# Loops in Python - while & for loop 
#   While Loop
#   For Loop
#   Range Function
#   Loop Control Statements

# while loop 

count = 0 

while count < 5: #condition 
    print(count)
    count = count + 1


# print numbers from 1 to 5 using while loop
count = 1 
while count < 6: #condition 
    print(count)
    # count = count + 1
    count += 1 


count = 5 
while count > 0: #condition 
    print(count)
    # count = count + 1
    count -= 1 
else:
    print("while loop ended")


# while True:
#     print("again and again!!") 
# check conditions to avoid infinite loop


#for loop 

language = 'Python' # sequence 

for x in language:
    print(x) 

# range function
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(5):  # stop argument
    print(i)

for i in range(5,10):     # start, stop argument
    print(i)

for i in range(1,10,3):  # start, stop, step argument
    print(i)

for i in range(5):
    print(i)
else:
    print("for loop ended")


# loop control statements 
"""
| Statement  | Description                                                                    |
| ---------- | ------------------------------------------------------------------------------ |
| `break`    | Terminates the loop completely.                                                |
| `continue` | Skips the rest of the current iteration and continues with the next iteration. |
| `pass`     | Acts as a placeholder — it does nothing but maintains syntactic correctness.   |

"""


# 1. pass statement 

for i in range(5):
    # mann nahi hai 
    pass 

count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 


#2. break statement 

for i in range(5):
    if i == 3:
        break 
    print(i) 

print("---------")


#3. continue statement 

for i in range(5):
    if i == 3:
        continue 
    print(i) 


# pass statment vs continue statement
count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 

# continue statement: don't try - infinite loop
count = 5 
while count > 0:
    if count == 3:
        #continue 
        pass
    else:
        print(count)
    count -= 1 


# validate user input: controlled infinite while loop using break statement
while True:
    user_input = input("Enter 'exit' to STOP: ")
    if user_input == 'exit':
        print("congarts! You guessed it right!")
        break 
    print("sorry, you entered: ", user_input)  

# Loops in Python - Nested Loop

# loop inside another loop is Nested Loop
# syntax

# outer_loop:
#     inner_loop:
#         #block of code for inner loop 
# block of code for outer loop

# print numbers from 1 to 3 for 3 times 

for i in range(3):
    # print("Outer loop iteration no, ", i)
    for num in range(1,4):
        print(num) 
    print("- - -")

# print numbers from 1 to 3 for 3 times using while-for loop : nested loop 
i = 1

while i < 4:
    print("while loop iteration no.", i)
    for j in range(1,4):
        print(j)
    # print("- - -")
    i += 1 


# print prime numbers between range of 2 to 10 using nested loop:

for num in range(2,10):
    for i in range(2,num):
        if num % i == 0: 
            break 
    else:
        print(num)     

# Assignments on Loops 

#1: print in the same line

print("Hello", "Madhav1", sep = "*" , end = " * ")
print("Madhav") 

# while loop to print the output in the same line
i = 1
while i < 4:
    print(f"Hello Madhav {i}", end = " ")
    i += 1

i = 1
while i < 4:
    print(f"Hello{i}", "Madhav", sep = "*", end = " ")
    i += 1


#2: star pattern 

#2.a: Triangle Pattern 
# nested loop to print triangle pattern
n = 5 # number of rows

for i in range(1, n+1): # outer loop no. of rows (1 to 5)
    for j in range(1, i+1):  # inner loop for columns (1 to i)
        print("*", end = " ") # print star without new line
    print() # move to the nest line after each row/iteration

# shortcut method
for i in range(1, n+1):
        print("* " * i) 

#2.b: inverted triangle 
n = 5 

# nested loop to print inverted triangle pattern
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

#shortcut method 
for i in range(n, 0, -1):
        print("* " * i)   

#2.c: pyramid pattern 
n = 5 # no. of rows 

for i in range(1, n+1): # loop for no. of rows 
    print(' ' * (n - i), end = "") # spaces to center the stars
    print("*" * (2 * i - 1)) # print stars

# 2n-1 
# 1 3 5 7   

# shortcut using single print function
for i in range(1, n+1): # loop for no. of rows 
    print(' ' * (n - i) + "*" * (2 * i - 1)) # print stars


#3: Factorial of a number 

def factorial(n):
    result = 1
    while n > 0:
        result *= n 
        # result = result * n  # 5*1, 5*4, 20*3, 60*2 
        n -= 1 
    return result 

print(factorial(5))
# 5! = 5 * 4 * 3 * 2 * 1  


#4: Count vowels in a string 
my_string = "Python by Rishabh Mishra" 
vowels = "aeiou"
count = 0 

for char in my_string:
    if char.lower() in vowels:
        count += 1 
print("Number of vowels are", count)    


#5: Longest word in a string 
sentence = "Python by Rishabh Mishra" 
words = sentence.split() 
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word 
print("The longest word is:", longest_word)


#6: do-while loop in python 

while True:
    num = int(input("Enter a number greater than 10: "))

    if num > 10:
        print(f"Valid number entered: {num}") 
        break # exit the loop when condition is satisfied
    else:
        print("Number is not greater than 10, try again!") 


#7: Fibonacci Sequence 

def fibonacci(n):
    a,b = 0,1 
    count = 0
    while count < n:
        print(a)    # 0 1 1 2 3
        a,b = b, a+b 
        count += 1 # 0 1 2 3 4 

fibonacci(10)        