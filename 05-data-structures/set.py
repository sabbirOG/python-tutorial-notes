# ======================
# 1. Creating Sets
# ======================

# Creating a non-empty set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: elements in random order (sets are unordered)

# Creating an empty set
empty_set = set()
print(type(empty_set))  # <class 'set'>

# {} creates a dictionary, not a set
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>
 
 # ======================
# 2. Adding Elements
# ======================

fruits.add("orange")   # Add a single element
print(fruits)

fruits.update(["mango", "grapes"])  # Add multiple elements
print(fruits)

# ======================
# 3. Removing Elements
# ======================

fruits.remove("banana")   # Removes item, raises error if not found
print(fruits)

fruits.discard("kiwi")    # Removes item, does NOT raise error if missing
print(fruits)

popped = fruits.pop()     # Removes a random element
print("Removed:", popped)
print(fruits)

fruits.clear()            # Remove all elements
print(fruits)             # Output: set()

# ======================
# 4. Set Operations
# ======================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)         # All unique elements
print("Intersection:", A & B)  # Common elements
print("Difference:", A - B)    # In A but not in B
print("Symmetric Diff:", A ^ B) # Elements in A or B but not both

# ======================
# 5. Membership Testing
# ======================

print(2 in A)       # True, because 2 exists in A
print(7 not in A)   # True, because 7 does not exist in A

# ======================
# 6. Converting to Sets
# ======================

nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)     # Remove duplicates
print(unique_nums)          # Output: {1, 2, 3}

text = "hello"
char_set = set(text)        # Convert string to set of unique characters
print(char_set)

# ======================
# 7. Set Methods
# ======================

numbers = {1, 2, 3, 4, 5}

print(len(numbers))           # Count of items
print(max(numbers))           # Largest item
print(min(numbers))           # Smallest item
print(sum(numbers))           # Sum of all items
print(sorted(numbers))        # Sorted list from set

# ======================
# 8. Frozen Sets (Immutable Sets)
# ======================

frozen = frozenset([1, 2, 3])
print(frozen)

# frozen.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'


# ======================
# 9. Practice Problem
# ======================

"""
PRACTICE PROBLEM: Student Course Tracker

Create a program that tracks which students are enrolled in which courses.
Use sets to efficiently manage the data and find common students between courses.

Requirements:
1. Create sets for 3 different courses: Math, Science, English
2. Add some students to each course (some students take multiple courses)
3. Find students who are taking ALL three courses
4. Find students who are taking ONLY Math
5. Find students who are taking Math OR Science (or both)
6. Count total unique students across all courses
"""

# Solution:
print("\n" + "="*50)
print("STUDENT COURSE TRACKER")
print("="*50)

# Create course sets
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Charlie", "Eve", "Frank"}
english_students = {"Alice", "Charlie", "Diana", "Grace"}

print(f"Math students: {math_students}")
print(f"Science students: {science_students}")
print(f"English students: {english_students}")

# Students taking ALL three courses
all_three = math_students & science_students & english_students
print(f"\nStudents taking ALL courses: {all_three}")

# Students taking ONLY Math
only_math = math_students - science_students - english_students
print(f"Students taking ONLY Math: {only_math}")

# Students taking Math OR Science (or both)
math_or_science = math_students | science_students
print(f"Students taking Math OR Science: {math_or_science}")

# Total unique students
all_students = math_students | science_students | english_students
print(f"Total unique students: {len(all_students)}")
print(f"All students: {all_students}")

"""Key Takeaways

set is unordered, unindexed, and only stores unique elements.

Use set() for empty sets, not {}.

Supports union, intersection, difference, symmetric difference.

Great for removing duplicates and fast membership testing.

frozenset is an immutable version of set."""