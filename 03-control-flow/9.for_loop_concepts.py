# We use loop to run something again and again

# for loop = for specific number
# while loop = conditional

# let's see the practical
# range(S, S, S)    start---stop---step
"""a = range(1, 6, 1)  starts from 1 and count number by skipping 1 integer value to the 10 

for i in range(16):
    print(i)
"""
"""# example of table:
n = int(input("what table you want?\n"))
for i in range(1, 11):
        print(f"{i}.({n}*{i})= {n*i}")
"""
"""
# let's access the string

name = "Sabbir Ahmed Munna"
for i,j in enumerate(name):
    print(f"{i}:{j}", end=" ")
"""

"""# directly accessing the character
name = "This is a coding school"
for i in name:
    print(i, end="",)

print("x\n")
a = "nature"
for i in range(len(a)):
    print(a[i], end=" ")

"""
# for loop questions:

"""# Q1: Accept an integer and print n number of times hello world!
n = int(input("input number:\n"))
for i in range(1, n+1):
    print(f"{i}.Hello World!")"""

# count  of all even and odd number in a range separately
"""n = int(input("enter your number:\n"))
even = 0
odd =  0
for i in range(1, n+1):
    if i % 2 == 0:
        even = even + 1 # counts the even number
    else:
        odd = odd + 1   # counts the odd number
print(f"Total EVEN = {even} and Total ODD = {odd}")"""

# q2: print sum of all even and odd number in a range seperately

"""even = 0
odd = 0
n = int(input("Enter your number:"))
for i in range(1, n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"EVEN: {even} and ODD: {odd}")
"""

# find the factors of an integer
"""n = int(input("enter your number:\n"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
"""

# find the perfect number : sum the factors and check condition if the sum matches the entered value or not
"""n = int(input("check if your entered number is perfect or not:\n"))
add = 0
for i in range(1, n):
    if n % i == 0:
        add = add + i
if(add == n):
    print("Your number is perfect")
else:
    print("sorry, Not Perfect!")
"""

"""# count the prime numbers
n = int(input("enter your number"))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("it is a prime number")
else:
    print("it is not a prime number!")"""

# reverse a string:
"""text = input("write a word!\n")
rev_text = text[::-1]
print(rev_text)
"""
# reversing a string using for loop
"""text = input("write a word!\n")
for i, j in enumerate(text[::-1]):
    print(f"{j}", end=" ")"""

# print the count value of integer, character, and special characters:
text = "ohanfm&94n29!@nm(-~)nf424"
dig = 0
char = 0
spchar = 0
for i in text:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchar += 1
print(f"Digits:{dig}\nCharacters:{char}\nSpecial characters:{spchar}")
