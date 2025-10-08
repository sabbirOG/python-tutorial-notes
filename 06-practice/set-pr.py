# ======================
# 1. Creating Sets
# ======================

# Non-empty set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Unordered, unique collection

# Empty set
empty_set = set()
print(type(empty_set))  # <class 'set'>

# {} creates dictionary, not set
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>

# ======================
# 2. Adding Elements
# ======================

fruits.add("orange")              # Add single element
fruits.update(["mango", "grapes"]) # Add multiple elements
print(fruits)

# ======================
# 3. Removing Elements
# ======================

fruits.remove("banana")   # Removes item, error if not found
fruits.discard("kiwi")    # Removes item, no error if not found
popped = fruits.pop()     # Removes random element
fruits.clear()            # Removes all elements
print(fruits)             # set()

# ======================
# 4. Set Operations
# ======================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union → all unique elements
print(A & B)   # Intersection → common elements
print(A - B)   # Difference → elements only in A
print(A ^ B)   # Symmetric difference → elements in A or B but not both

# ======================
# 5. Membership Testing
# ======================

print(2 in A)      # True if 2 exists in A
print(7 not in A)  # True if 7 does not exist in A

# ======================
# 6. Converting to Set
# ======================

nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)  # Remove duplicates
print(unique_nums)       # {1, 2, 3}

text = "hello"
char_set = set(text)     # Unique characters
print(char_set)

# ======================
# 7. Useful Methods
# ======================

numbers = {1, 2, 3, 4, 5}
print(len(numbers))     # Count items
print(max(numbers))     # Largest item
print(min(numbers))     # Smallest item
print(sum(numbers))     # Sum of items
print(sorted(numbers))  # Sorted list from set

# ======================
# 8. Frozen Sets (Immutable)
# ======================

frozen = frozenset([1, 2, 3])
print(frozen)

# frozen.add(4)  # ❌ Error: frozenset cannot be modified
