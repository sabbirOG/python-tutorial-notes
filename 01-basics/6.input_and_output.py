"""
===============================================
PYTHON INPUT AND OUTPUT TUTORIAL
===============================================

This tutorial covers:
1. Different ways to print output
2. Taking user input
3. Formatting strings
4. Handling different input types
5. Multiple input techniques

Let's start with output methods!
"""

print("=" * 50)
print("OUTPUT METHODS")
print("=" * 50)

# 1. BASIC PRINTING
print("\n1. Basic Print Statements:")
name = "Alice"
age = 23
print("My name is", name, "and my age is", age, "(comma-separated)")

# 2. F-STRING FORMATTING (Recommended)
print("\n2. F-String Formatting (Modern Python):")
name = "Alice Johnson"
age = 23
print(f"My name is {name} and my age is {age} (f-string)")

# 3. STRING FORMATTING METHODS
print("\n3. Other String Formatting Methods:")
print("Hello, my name is {} and I am {} years old".format(name, age))
print("Hello, my name is {0} and I am {1} years old".format(name, age))
print("Hello, my name is {n} and I am {a} years old".format(n=name, a=age))

print("\n" + "=" * 50)
print("USER INPUT BASICS")
print("=" * 50)

print("\n⚠️  IMPORTANT: Run this code in terminal/command prompt for input functionality!")
print("The input() function waits for user input from the keyboard.")

# Simulated input examples (since we can't actually take input in this context)
print("\nExample 1: Basic String Input")
print("# name = input('What is your name?\\n')")
print("# print(f'Hello, {name}!')")

print("\nExample 2: Numeric Input with Type Conversion")
print("# age = int(input('How old are you?\\n'))")
print("# print(f'You are {age} years old')")

print("\n" + "=" * 50)
print("INPUT TYPE CONVERSION")
print("=" * 50)

print("\nBy default, input() returns a string. You need to convert it:")
print("✓ int(input())     - for integers")
print("✓ float(input())   - for decimal numbers")
print("✓ input()          - for strings (no conversion needed)")

print("\nExample conversions:")
print("# age = int(input('Enter your age: '))")
print("# height = float(input('Enter your height: '))")
print("# name = input('Enter your name: ')")

print("\n" + "=" * 50)
print("MULTIPLE INPUTS")
print("=" * 50)

print("\n1. Taking Multiple Values on One Line:")
print("# Method 1: Using split()")
print("# a, b, c = input('Enter three numbers: ').split()")
print("# print(f'Numbers: {a}, {b}, {c}')")

print("\n2. Converting Multiple Inputs to Integers:")
print("# Method 2: Using map() and int()")
print("# a, b, c = map(int, input('Enter three numbers: ').split())")
print("# print(f'Sum: {a + b + c}')")

print("\n3. Taking List as Input:")
print("# String list:")
print("# words = input('Enter words separated by spaces: ').split()")
print("# print(f'Words: {words}')")

print("# Integer list:")
print("# numbers = list(map(int, input('Enter numbers: ').split()))")
print("# print(f'Numbers: {numbers}')")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\nExample 1: Simple Calculator")
print("""
# Simple calculator
num1 = float(input('Enter first number: '))
operator = input('Enter operator (+, -, *, /): ')
num2 = float(input('Enter second number: '))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = 'Invalid operator'

print(f'Result: {result}')
""")

print("\nExample 2: User Registration")
print("""
# User registration form
print("=== User Registration ===")
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email: ')
age = int(input('Age: '))

print(f"\\nRegistration successful!")
print(f"Name: {first_name} {last_name}")
print(f"Email: {email}")
print(f"Age: {age}")
""")

print("\n" + "=" * 50)
print("INPUT VALIDATION")
print("=" * 50)

print("\nAlways validate user input:")
print("""
# Safe input with error handling
while True:
    try:
        age = int(input('Enter your age: '))
        if age < 0 or age > 150:
            print('Please enter a valid age (0-150)')
            continue
        break
    except ValueError:
        print('Please enter a valid number')

print(f'Your age is: {age}')
""")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("✓ Use f-strings for modern string formatting")
print("✓ input() always returns a string")
print("✓ Convert input types with int(), float(), etc.")
print("✓ Use split() and map() for multiple inputs")
print("✓ Always validate user input")
print("✓ Run input programs in terminal/command prompt")