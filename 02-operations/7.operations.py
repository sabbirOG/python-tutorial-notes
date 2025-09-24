"""
===============================================
PYTHON OPERATORS TUTORIAL
===============================================

Operators are symbols that perform operations on variables and values.
This tutorial covers:
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Operator Precedence (BODMAS/PEMDAS)

Let's explore each type with examples!
"""

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

print("Arithmetic operators perform mathematical operations:")
print("+ (Addition), - (Subtraction), * (Multiplication)")
print("/ (Division), // (Floor Division), % (Modulus), ** (Exponentiation)")

# 1. ADDITION
print("\n1. Addition (+):")
a = 10
b = 20
result = a + b
print(f"{a} + {b} = {result}")

# 2. SUBTRACTION
print("\n2. Subtraction (-):")
aa = 20
bb = 8
result = aa - bb
print(f"{aa} - {bb} = {result}")

# 3. MULTIPLICATION
print("\n3. Multiplication (*):")
x = 5
y = 4
result = x * y
print(f"{x} × {y} = {result}")

# 4. DIVISION
print("\n4. Division (/):")
a = 20
b = 5
result = a / b
print(f"{a} ÷ {b} = {result}")
print("Note: Division always returns a float, even with integers")

# 5. FLOOR DIVISION
print("\n5. Floor Division (//):")
a = 20
b = 3
result = a // b
print(f"{a} // {b} = {result}")
print("Note: Floor division truncates decimal part (rounds down)")

# 6. MODULUS
print("\n6. Modulus (%):")
a = 19
b = 3
result = a % b
print(f"{a} % {b} = {result}")
print("Note: Modulus returns the remainder after division")

# 7. EXPONENTIATION
print("\n7. Exponentiation (**):")
a = 9
b = 2
result = a ** b
print(f"{a}^{b} = {result}")

print("\n" + "=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

print("Comparison operators compare values and return True or False:")
print("== (Equal), != (Not Equal), > (Greater), < (Less)")
print(">= (Greater or Equal), <= (Less or Equal)")

a = 20
b = 30
c = 35
d = 35

print(f"\nValues: a={a}, b={b}, c={c}, d={d}")

print(f"\nComparison Results:")
print(f"a > b:  {a > b}   (20 > 30)")
print(f"b > a:  {b > a}   (30 > 20)")
print(f"c == d: {c == d}  (35 == 35)")
print(f"a != b: {a != b}  (20 != 30)")
print(f"a >= b: {a >= b}  (20 >= 30)")
print(f"a <= b: {a <= b}  (20 <= 30)")

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

print("Logical operators combine boolean expressions:")
print("and, or, not")

print("\n1. AND Operator (both conditions must be True):")
print(f"33 > 20 and 40 < 50: {33 > 20 and 40 < 50}")
print(f"10 > 5 and 3 < 2: {10 > 5 and 3 < 2}")

print("\n2. OR Operator (at least one condition must be True):")
print(f"20 == 23 or 5 != 20: {20 == 23 or 5 != 20}")
print(f"10 > 5 or 3 < 2: {10 > 5 or 3 < 2}")

print("\n3. NOT Operator (reverses the boolean value):")
print(f"not (10 > 5): {not (10 > 5)}")
print(f"not (3 < 2): {not (3 < 2)}")

print("\n" + "=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50)

print("Assignment operators assign values to variables:")
print("=, +=, -=, *=, /=, //=, %=, **=")

# Basic assignment
a = 20
print(f"Basic assignment: a = {a}")

# Compound assignment operators
print("\nCompound Assignment Examples:")
a = 20
print(f"Initial value: a = {a}")

a += 20  # Same as a = a + 20
print(f"After a += 20: a = {a}")

a -= 10  # Same as a = a - 10
print(f"After a -= 10: a = {a}")

a *= 2   # Same as a = a * 2
print(f"After a *= 2: a = {a}")

a /= 4   # Same as a = a / 4
print(f"After a /= 4: a = {a}")

print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE (BODMAS/PEMDAS)")
print("=" * 50)

print("Python follows operator precedence rules:")
print("1. Parentheses ()")
print("2. Exponentiation **")
print("3. Multiplication *, Division /, Floor Division //, Modulus %")
print("4. Addition +, Subtraction -")
print("5. Comparison operators (==, !=, <, >, <=, >=)")
print("6. Logical operators (not, and, or)")

# BODMAS example
print("\nBODMAS Example:")
a = 2
b = 4
c = 6
d = 8
result = a + b * (c) / 3 - d
print(f"Expression: a + b * (c) / 3 - d")
print(f"Values: a={a}, b={b}, c={c}, d={d}")
print(f"Result: {result}")

print("\nStep-by-step calculation:")
print(f"1. b * c = {b} * {c} = {b * c}")
print(f"2. (b * c) / 3 = {b * c} / 3 = {(b * c) / 3}")
print(f"3. a + (b * c / 3) = {a} + {(b * c) / 3} = {a + (b * c) / 3}")
print(f"4. Final: {a + (b * c) / 3} - {d} = {result}")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\nExample 1: Calculator Functions")
def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operator == '**':
        return num1 ** num2
    else:
        return "Invalid operator"

# Test calculator
print("Calculator Tests:")
print(f"5 + 3 = {calculator(5, '+', 3)}")
print(f"10 - 4 = {calculator(10, '-', 4)}")
print(f"6 * 7 = {calculator(6, '*', 7)}")
print(f"15 / 3 = {calculator(15, '/', 3)}")
print(f"2 ** 8 = {calculator(2, '**', 8)}")

print("\nExample 2: Number Properties")
def analyze_number(num):
    is_positive = num > 0
    is_even = num % 2 == 0
    is_divisible_by_3 = num % 3 == 0
    is_perfect_square = (num ** 0.5) % 1 == 0
    
    return {
        'positive': is_positive,
        'even': is_even,
        'divisible_by_3': is_divisible_by_3,
        'perfect_square': is_perfect_square
    }

numbers = [16, 15, -4, 9, 0]
for num in numbers:
    properties = analyze_number(num)
    print(f"\nNumber {num}:")
    for prop, value in properties.items():
        print(f"  {prop}: {value}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("✓ Arithmetic: +, -, *, /, //, %, **")
print("✓ Comparison: ==, !=, <, >, <=, >=")
print("✓ Logical: and, or, not")
print("✓ Assignment: =, +=, -=, *=, /=, etc.")
print("✓ Follow BODMAS/PEMDAS for operator precedence")
print("✓ Use parentheses to control order of operations")
print("✓ Division always returns float, use // for integer division") 