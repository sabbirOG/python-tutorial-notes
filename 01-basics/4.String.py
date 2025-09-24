"""
===============================================
PYTHON STRING TUTORIAL
===============================================

Strings in Python are sequences of characters enclosed in quotes.
This tutorial covers:
1. String basics and Unicode
2. String indexing and slicing
3. String methods and operations
4. String formatting
5. Common string techniques

Let's dive into the world of strings!
"""

print("=" * 50)
print("STRING BASICS")
print("=" * 50)

# String creation
single_quote = 'Hello World'
double_quote = "Hello World"
triple_quote = """This is a
multi-line string"""

print("1. String Creation:")
print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Triple quotes: {triple_quote}")

print("\n" + "=" * 50)
print("UNICODE AND CHARACTERS")
print("=" * 50)

print("\nEvery character has a Unicode value:")
print("Unicode is a standard that assigns unique numbers to characters.")

# Character to Unicode
char = "S"
unicode_value = ord(char)
print(f"Character '{char}' has Unicode value: {unicode_value}")

# Unicode to Character
unicode_num = 83
character = chr(unicode_num)
print(f"Unicode {unicode_num} represents character: '{character}'")

# More Unicode examples
print("\nUnicode Examples:")
characters = ['A', 'a', '0', '!', '€', '中']
for char in characters:
    unicode_val = ord(char)
    print(f"'{char}' → Unicode: {unicode_val}")

print("\n" + "=" * 50)
print("STRING INDEXING")
print("=" * 50)

text = "Tiger Coder"
print(f"String: '{text}'")
print(f"Length: {len(text)} characters")

print("\nIndexing (accessing individual characters):")
print("Positive indexing (left to right):")
for i in range(len(text)):
    print(f"Index {i}: '{text[i]}'")

print("\nNegative indexing (right to left):")
for i in range(-len(text), 0):
    print(f"Index {i}: '{text[i]}'")

print("\n" + "=" * 50)
print("STRING SLICING")
print("=" * 50)

text = "Tiger Coder"
print(f"Original string: '{text}'")

print("\nSlicing syntax: string[start:end:step]")
print("• start: starting index (inclusive)")
print("• end: ending index (exclusive)")
print("• step: how many characters to skip")

# Basic slicing
print(f"\n1. Basic slicing:")
print(f"text[0:5] = '{text[0:5]}'")  # First 5 characters
print(f"text[6:11] = '{text[6:11]}'")  # Last word

# Slicing with step
print(f"\n2. Slicing with step:")
print(f"text[0:5:2] = '{text[0:5:2]}'")  # Every 2nd character
print(f"text[0:5:3] = '{text[0:5:3]}'")  # Every 3rd character

# Advanced slicing
print(f"\n3. Advanced slicing:")
print(f"text[5:] = '{text[5:]}'")  # From index 5 to end
print(f"text[:5] = '{text[:5]}'")  # From start to index 5
print(f"text[::2] = '{text[::2]}'")  # Every 2nd character
print(f"text[::-1] = '{text[::-1]}'")  # Reverse string

print("\n" + "=" * 50)
print("COMMON STRING METHODS")
print("=" * 50)

sample_text = "  Hello World!  "
print(f"Sample text: '{sample_text}'")

print("\n1. Case Methods:")
print(f"upper(): '{sample_text.upper()}'")
print(f"lower(): '{sample_text.lower()}'")
print(f"title(): '{sample_text.title()}'")
print(f"capitalize(): '{sample_text.capitalize()}'")

print("\n2. Whitespace Methods:")
print(f"strip(): '{sample_text.strip()}'")
print(f"lstrip(): '{sample_text.lstrip()}'")
print(f"rstrip(): '{sample_text.rstrip()}'")

print("\n3. Search Methods:")
text = "Hello World"
print(f"Text: '{text}'")
print(f"startswith('Hello'): {text.startswith('Hello')}")
print(f"endswith('World'): {text.endswith('World')}")
print(f"find('World'): {text.find('World')}")
print(f"count('l'): {text.count('l')}")

print("\n4. Replace and Split:")
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")
print(f"split(' '): {text.split(' ')}")

print("\n" + "=" * 50)
print("STRING FORMATTING")
print("=" * 50)

name = "Alice"
age = 25
height = 5.6

print("1. F-String Formatting (Recommended):")
print(f"Name: {name}, Age: {age}, Height: {height}")

print("\n2. .format() Method:")
print("Name: {}, Age: {}, Height: {}".format(name, age, height))
print("Name: {0}, Age: {1}, Height: {2}".format(name, age, height))
print("Name: {n}, Age: {a}, Height: {h}".format(n=name, a=age, h=height))

print("\n3. % Formatting (Older style):")
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

print("\n" + "=" * 50)
print("STRING OPERATIONS")
print("=" * 50)

str1 = "Hello"
str2 = "World"

print("1. Concatenation:")
print(f"str1 + str2 = '{str1 + str2}'")
print(f"str1 + ' ' + str2 = '{str1 + ' ' + str2}'")

print("\n2. Repetition:")
print(f"str1 * 3 = '{str1 * 3}'")

print("\n3. Membership Testing:")
print(f"'ell' in str1: {'ell' in str1}")
print(f"'xyz' in str1: {'xyz' in str1}")

print("\n4. String Comparison:")
print(f"'{str1}' == '{str2}': {str1 == str2}")
print(f"'{str1}' < '{str2}': {str1 < str2}")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\nExample 1: Text Processing")
text = "  Python Programming is Amazing!  "
print(f"Original: '{text}'")

# Clean and process
cleaned = text.strip().lower()
words = cleaned.split()
word_count = len(words)

print(f"Cleaned: '{cleaned}'")
print(f"Words: {words}")
print(f"Word count: {word_count}")

print("\nExample 2: String Validation")
def is_valid_email(email):
    return '@' in email and '.' in email and len(email) > 5

emails = ["user@example.com", "invalid-email", "test@domain", "a@b.c"]
for email in emails:
    print(f"'{email}' is valid: {is_valid_email(email)}")

print("\nExample 3: Text Analysis")
sentence = "The quick brown fox jumps over the lazy dog"
print(f"Sentence: '{sentence}'")
print(f"Length: {len(sentence)} characters")
print(f"Word count: {len(sentence.split())} words")
print(f"Vowel count: {sum(1 for char in sentence.lower() if char in 'aeiou')}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("✓ Strings are sequences of characters")
print("✓ Use indexing [i] to access characters")
print("✓ Use slicing [start:end:step] to extract substrings")
print("✓ Strings are immutable (cannot be changed)")
print("✓ Use string methods for text processing")
print("✓ F-strings are the modern way to format strings")
print("✓ Unicode allows representation of all characters")
