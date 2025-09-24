"""
===============================================
PYTHON TYPE CONVERSION TUTORIAL
===============================================

Type Conversion (Type Casting) is the process of converting one data type to another.
Python provides built-in functions for type conversion:
- int()    - converts to integer
- float()  - converts to float
- str()    - converts to string
- bool()   - converts to boolean

There are two types of type conversion:
1. Explicit (Manual) - We manually convert types
2. Implicit (Automatic) - Python automatically converts types
"""

print("=" * 50)
print("EXPLICIT TYPE CONVERSION EXAMPLES")
print("=" * 50)

# 1. INTEGER TO FLOAT CONVERSION
print("\n1. Converting Integer to Float:")
a = 5
print(f"Original value: {a} (type: {type(a)})")
tc = float(a)
print(f"After conversion: {tc} (type: {type(tc)})")

# 2. STRING TO INTEGER CONVERSION
print("\n2. Converting String to Integer:")
b = "5"
print(f"Original value: '{b}' (type: {type(b)})")
t_c = int(b)
print(f"After conversion: {t_c} (type: {type(t_c)})")

# 3. FLOAT TO INTEGER CONVERSION
print("\n3. Converting Float to Integer:")
c = 5.93
print(f"Original value: {c} (type: {type(c)})")
tC = int(c)
print(f"After conversion: {tC} (type: {type(tC)})")
print("Note: Decimal part is truncated, not rounded!")

# 4. INTEGER TO STRING CONVERSION
print("\n4. Converting Integer to String:")
d = 42
print(f"Original value: {d} (type: {type(d)})")
str_d = str(d)
print(f"After conversion: '{str_d}' (type: {type(str_d)})")

print("\n" + "=" * 50)
print("BOOLEAN CONVERSION RULES")
print("=" * 50)

# BOOLEAN CONVERSION
print("\nBoolean conversion follows these rules:")
print("Falsy values (convert to False):")
print("- 0 (zero)")
print("- 0.0 (zero point zero)")
print("- '' (empty string)")
print("- False")
print("- None")

print("\nTruthy values (convert to True):")
print("- Any non-zero number")
print("- Any non-empty string")
print("- True")

# Examples of boolean conversion
print("\nBoolean Conversion Examples:")
test_values = [5, 0, -1, 0.0, 3.14, "", "hello", "0", True, False, None]

for value in test_values:
    result = bool(value)
    print(f"bool({repr(value)}) = {result}")

print("\n" + "=" * 50)
print("COMMON CONVERSION ERRORS")
print("=" * 50)

print("\n❌ INVALID CONVERSIONS (will cause errors):")
print("# These will raise ValueError:")
print("# int('abc')     # Can't convert letters to integer")
print("# float('hello') # Can't convert letters to float")
print("# int('3.14')    # Can't convert decimal string directly to int")

print("\n✅ VALID CONVERSIONS:")
print("int('3')        # String number to integer")
print("float('3.14')   # String decimal to float")
print("str(42)         # Number to string")

print("\n" + "=" * 50)
print("IMPLICIT TYPE CONVERSION")
print("=" * 50)

print("\nPython automatically converts types in certain operations:")
print("Example: Division always returns float, even with integers")

a = 5
b = 15
c = b / a
print(f"Division: {b} / {a} = {c} (type: {type(c)})")

# Mixed type operations
print(f"\nMixed operations:")
print(f"5 + 3.14 = {5 + 3.14} (type: {type(5 + 3.14)})")
print(f"'Hello' + ' World' = {'Hello' + ' World'} (type: {type('Hello' + ' World')})")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Practical example: User input processing
print("\nExample: Processing user input (simulated):")
user_age = "25"  # Usually comes from input() as string
user_height = "5.8"  # Usually comes from input() as string

# Convert to appropriate types
age_int = int(user_age)
height_float = float(user_height)

print(f"User is {age_int} years old and {height_float} feet tall")
print(f"Age type: {type(age_int)}, Height type: {type(height_float)}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("✓ Use int(), float(), str(), bool() for explicit conversion")
print("✓ Be careful with invalid conversions")
print("✓ Python handles some conversions automatically")
print("✓ Always check data types with type() function")
