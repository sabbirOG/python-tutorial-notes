# function is a block of reuseable code. when we call the function, it runs 

#arguments are three types:

# keyword arguments:
def hello(name, age):
    print(f"1.keyword arguments:\nHello Mr.{name}. Your age is {age}")

hello(age = 23, name="sabbir")

# positional arguments:
def hello(name, age):
    print(f"2.positional arguments:\nHello Mr.{name}. Your age is {age}")

hello("sabbir", 23)

# default arguments:
def greet(name, age = 22):
    print(f"default arguments:\nHello Mr.{name}. Your age is {age}")

greet("Ahmed")
greet("Sabbir Ahmed", 24)

# checking palindrome

def checking_palindrome(text):
    palindrome = text[::-1]
    if palindrome == text:
        print("this is palindrome")
    else:
        print("try again!")

text = input("enter text:\n")
checking_palindrome(text)