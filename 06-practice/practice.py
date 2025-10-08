"""
===============================================
PYTHON PRACTICE EXERCISES
===============================================

This file contains comprehensive practice problems covering all Python concepts
from the tutorial series. These exercises will help you master Python programming!

Difficulty Levels:
🟢 Beginner (Basics)
🟡 Intermediate (Operations & Control Flow)
🔴 Advanced (Functions & Data Structures)
"""

print("=" * 60)
print("🐍 PYTHON PRACTICE EXERCISES")
print("=" * 60)

print("\n" + "=" * 60)
print("🟢 BEGINNER LEVEL EXERCISES")
print("=" * 60)

print("\n1. VARIABLES AND DATA TYPES")
print("-" * 30)

# Exercise 1: Variable Practice
print("Exercise 1: Create variables for your personal information")
name = "Your Name"
age = 25
height = 5.8
is_student = True
favorite_language = "Python"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")
print(f"Favorite Language: {favorite_language}")

print("\n2. STRING MANIPULATION")
print("-" * 30)

# Exercise 2: String Operations
text = "  Hello World!  "
print(f"Original: '{text}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Stripped: '{text.strip()}'")
print(f"Replaced: '{text.replace('World', 'Python')}'")
print(f"Length: {len(text)}")

print("\n3. TYPE CONVERSION")
print("-" * 30)

# Exercise 3: Type Conversion
number_str = "42"
number_int = int(number_str)
number_float = float(number_str)
print(f"String: '{number_str}' (type: {type(number_str)})")
print(f"Integer: {number_int} (type: {type(number_int)})")
print(f"Float: {number_float} (type: {type(number_float)})")

print("\n" + "=" * 60)
print("🟡 INTERMEDIATE LEVEL EXERCISES")
print("=" * 60)

print("\n4. ARITHMETIC OPERATIONS")
print("-" * 30)

# Exercise 4: Calculator
def simple_calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Test calculator
print("Calculator Tests:")
print(f"10 + 5 = {simple_calculator(10, 5, '+')}")
print(f"10 - 5 = {simple_calculator(10, 5, '-')}")
print(f"10 * 5 = {simple_calculator(10, 5, '*')}")
print(f"10 / 5 = {simple_calculator(10, 5, '/')}")
print(f"10 / 0 = {simple_calculator(10, 0, '/')}")

print("\n5. CONDITIONAL STATEMENTS")
print("-" * 30)

# Exercise 5: Grade Classifier
def grade_classifier(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 87, 76, 65, 45]
print("Grade Classification:")
for score in scores:
    grade = grade_classifier(score)
    print(f"Score {score}: Grade {grade}")

print("\n6. LOOPS")
print("-" * 30)

# Exercise 6: Number Patterns
print("Number Pattern 1:")
for i in range(1, 6):
    print("*" * i)

print("\nNumber Pattern 2:")
for i in range(5, 0, -1):
    print("*" * i)

print("\nMultiplication Table (5):")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

print("\n" + "=" * 60)
print("🔴 ADVANCED LEVEL EXERCISES")
print("=" * 60)

print("\n7. FUNCTIONS - BASIC CONCEPTS")
print("-" * 30)

# Exercise 7a: Basic Function Definition and Calling
def greet(name):
    """A simple function that greets a person"""
    return f"Hello, {name}! Welcome to Python!"

def add_numbers(a, b):
    """Function that adds two numbers"""
    return a + b

def multiply(x, y):
    """Function that multiplies two numbers"""
    result = x * y
    return result

# Test basic functions
print("Basic Function Tests:")
print(greet("Alice"))
print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"4 × 7 = {multiply(4, 7)}")

# Exercise 7b: Functions with Default Parameters
def greet_with_title(name, title="Mr./Ms."):
    """Function with default parameter"""
    return f"Hello, {title} {name}!"

def create_profile(name, age=18, city="Unknown"):
    """Function with multiple default parameters"""
    return f"Name: {name}, Age: {age}, City: {city}"

print("\nFunctions with Default Parameters:")
print(greet_with_title("John"))
print(greet_with_title("Jane", "Dr."))
print(create_profile("Bob"))
print(create_profile("Alice", 25))
print(create_profile("Charlie", 30, "New York"))

# Exercise 7c: Functions with Multiple Return Values
def get_name_parts(full_name):
    """Function that returns multiple values"""
    parts = full_name.split()
    first_name = parts[0] if parts else ""
    last_name = parts[-1] if len(parts) > 1 else ""
    middle_names = " ".join(parts[1:-1]) if len(parts) > 2 else ""
    return first_name, middle_names, last_name

def calculate_stats(numbers):
    """Function that returns multiple statistics"""
    if not numbers:
        return 0, 0, 0, 0
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

print("\nFunctions with Multiple Return Values:")
first, middle, last = get_name_parts("John Michael Smith")
print(f"First: {first}, Middle: {middle}, Last: {last}")

stats = calculate_stats([10, 20, 30, 40, 50])
print(f"Numbers: [10, 20, 30, 40, 50]")
print(f"Total: {stats[0]}, Average: {stats[1]}, Max: {stats[2]}, Min: {stats[3]}")

# Exercise 7d: Functions with Variable Arguments
def sum_all(*numbers):
    """Function that accepts variable number of arguments"""
    return sum(numbers)

def create_sentence(*words):
    """Function that joins variable number of words"""
    return " ".join(words)

def print_info(**kwargs):
    """Function that accepts keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nFunctions with Variable Arguments:")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10,20: {sum_all(10, 20)}")
print(f"Sentence: {create_sentence('Hello', 'world', 'from', 'Python')}")

print("\nKeyword Arguments:")
print_info(name="Alice", age=25, city="Boston", occupation="Developer")

# Exercise 7e: Lambda Functions (Anonymous Functions)
square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print("\nLambda Functions:")
print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Even numbers: {even_numbers}")

print("\n8. FUNCTIONS - ADVANCED CONCEPTS")
print("-" * 30)

# Exercise 8: Advanced Functions
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def prime_checker(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test functions
print("Fibonacci sequence (10 terms):", fibonacci(10))
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))
print("Is 17 prime?", prime_checker(17))
print("Is 15 prime?", prime_checker(15))

print("\n8. DATA STRUCTURES")
print("-" * 30)

# Exercise 8: List Operations
def list_analyzer(lst):
    """Analyze a list and return statistics"""
    if not lst:
        return "Empty list"
    
    return {
        'length': len(lst),
        'sum': sum(lst),
        'average': sum(lst) / len(lst),
        'max': max(lst),
        'min': min(lst),
        'sorted': sorted(lst),
        'unique': list(set(lst))
    }

# Test list analyzer
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6, 2, 8]
analysis = list_analyzer(numbers)
print("List Analysis:")
for key, value in analysis.items():
    print(f"{key.capitalize()}: {value}")

print("\n9. COMPREHENSIVE PROBLEMS")
print("-" * 30)

# Exercise 9: Word Counter
def word_counter(text):
    """Count words and characters in text"""
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    
    return {
        'word_count': len(words),
        'character_count': characters,
        'character_count_no_spaces': characters_no_spaces,
        'words': words
    }

sample_text = "Python is an amazing programming language"
word_stats = word_counter(sample_text)
print("Word Counter Results:")
for key, value in word_stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

# Exercise 10: List Sorting Check
def is_sorted(lst):
    """Check if a list is sorted in ascending order"""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Test sorting check
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [5, 2, 8, 1, 9]
print(f"Is {sorted_list} sorted? {is_sorted(sorted_list)}")
print(f"Is {unsorted_list} sorted? {is_sorted(unsorted_list)}")

print("\n" + "=" * 60)
print("🎯 CHALLENGE PROBLEMS")
print("=" * 60)

print("\nChallenge 1: Password Validator")
def password_validator(password):
    """Validate password strength"""
    if len(password) < 8:
        return "Password too short (minimum 8 characters)"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score == 4:
        return "Strong password"
    elif score >= 2:
        return "Medium password"
    else:
        return "Weak password"

passwords = ["password", "Password123", "P@ssw0rd!", "abc"]
for pwd in passwords:
    print(f"'{pwd}': {password_validator(pwd)}")

print("\nChallenge 2: Number Guessing Game")
import random

def number_guessing_game():
    """Simple number guessing game"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"Guess a number between 1 and 100. You have {max_attempts} attempts!")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}")

# Uncomment to play the game
# number_guessing_game()

print("\n" + "=" * 60)
print("🔧 FUNCTION PRACTICE EXERCISES")
print("=" * 60)

print("\nExercise 1: Temperature Converter")
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print("Temperature Conversions:")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

print("\nExercise 2: String Manipulation Functions")
def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return " ".join(word.capitalize() for word in text.split())

sample_text = "hello world python programming"
print(f"Original: '{sample_text}'")
print(f"Vowel count: {count_vowels(sample_text)}")
print(f"Reversed: '{reverse_string(sample_text)}'")
print(f"Capitalized: '{capitalize_words(sample_text)}'")

print("\nExercise 3: List Processing Functions")
def find_max_min(lst):
    """Find maximum and minimum in a list"""
    if not lst:
        return None, None
    return max(lst), min(lst)

def remove_duplicates(lst):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def merge_lists(list1, list2):
    """Merge two lists and sort them"""
    merged = list1 + list2
    return sorted(merged)

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(f"Test list: {test_list}")
max_val, min_val = find_max_min(test_list)
print(f"Max: {max_val}, Min: {min_val}")
print(f"Without duplicates: {remove_duplicates(test_list)}")
print(f"Merged and sorted: {merge_lists(list1, list2)}")

print("\nExercise 4: Mathematical Functions")
def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_perfect_square(n):
    """Check if a number is a perfect square"""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def gcd(a, b):
    """Find Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print("Mathematical Functions:")
print(f"Factorial of 5: {factorial(5)}")
print(f"Is 16 a perfect square? {is_perfect_square(16)}")
print(f"Is 15 a perfect square? {is_perfect_square(15)}")
print(f"GCD of 48 and 18: {gcd(48, 18)}")

print("\nExercise 5: Function Composition and Higher-Order Functions")
def apply_operation(numbers, operation):
    """Apply an operation to a list of numbers"""
    return [operation(num) for num in numbers]

def create_multiplier(factor):
    """Create a function that multiplies by a factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Test function composition
numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, lambda x: x * 2)
squared = apply_operation(numbers, lambda x: x ** 2)

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Squared: {squared}")

# Test higher-order function
multiply_by_3 = create_multiplier(3)
print(f"Multiply by 3: {[multiply_by_3(x) for x in numbers]}")

print("\n" + "=" * 60)
print("📚 ADDITIONAL PRACTICE IDEAS")
print("=" * 60)

print("""
Here are more practice ideas to continue learning:

1. Create a simple calculator with a menu
2. Build a student grade management system
3. Develop a text-based adventure game
4. Create a file organizer script
5. Build a simple web scraper
6. Develop a password generator
7. Create a number system converter
8. Build a simple database using dictionaries
9. Develop a text encryption/decryption tool
10. Create a simple drawing program using turtle graphics

Remember: The best way to learn programming is by practicing!
Keep coding and experimenting with new ideas! 🚀
""")

print("\n" + "=" * 60)
print("✅ PRACTICE COMPLETE!")
print("=" * 60)
print("Great job working through these exercises!")
print("Keep practicing and building projects to master Python! 🐍✨")