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

print("\n7. FUNCTIONS")
print("-" * 30)

# Exercise 7: Advanced Functions
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