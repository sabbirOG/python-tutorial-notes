"""
===============================================
PYTHON VARIABLE NAMING CONVENTIONS TUTORIAL
===============================================

Variables are containers for storing data values.
Python has three main naming conventions for variables:

1. snake_case (most popular in Python)
2. PascalCase (used for classes)
3. camelCase (used in some other languages)

Let's explore each style with examples!
"""

print("=" * 50)
print("UNDERSTANDING VARIABLES")
print("=" * 50)

# Basic variable assignment
variable = "A variable is a storage container for data"
print(f"Variable content: {variable}")
print(f"Variable type: {type(variable)}")

print("\n" + "=" * 50)
print("THREE VARIABLE NAMING STYLES")
print("=" * 50)

# 1. SNAKE_CASE (Most popular in Python)
# - Uses lowercase letters
# - Words separated by underscores
# - Used for variables, functions, modules
snake_case_variable = "This is snake_case style"
print(f"1. Snake Case: {snake_case_variable}")

# 2. PascalCase (Used for classes)
# - First letter of each word is capitalized
# - No separators between words
# - Used for class names
PascalCaseVariable = "This is PascalCase style"
print(f"2. Pascal Case: {PascalCaseVariable}")

# 3. camelCase (Used in other languages)
# - First word lowercase, subsequent words capitalized
# - No separators between words
# - Less common in Python
camelCaseVariable = "This is camelCase style"
print(f"3. Camel Case: {camelCaseVariable}")

print("\n" + "=" * 50)
print("PYTHON NAMING RULES")
print("=" * 50)

print("✓ Variable names can contain:")
print("  - Letters (a-z, A-Z)")
print("  - Numbers (0-9)")
print("  - Underscores (_)")
print("  - Cannot start with a number")

print("\n✓ Good variable names:")
print("  - user_name")
print("  - total_count")
print("  - is_valid")
print("  - MAX_SIZE")

print("\n❌ Bad variable names:")
print("  - 2user (starts with number)")
print("  - user-name (contains hyphen)")
print("  - class (reserved keyword)")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Real-world examples
user_name = "Alice"
user_age = 25
is_student = True
max_attempts = 3

print(f"User: {user_name}")
print(f"Age: {user_age}")
print(f"Is student: {is_student}")
print(f"Max attempts: {max_attempts}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("✓ Use snake_case for variables and functions")
print("✓ Use PascalCase for class names")
print("✓ Choose descriptive names that explain purpose")
print("✓ Follow Python naming conventions for better code readability")
