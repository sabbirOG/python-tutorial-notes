# four types of (in build) data structure
# 1. List  || 2. tuple  || 3. Dictionary    || 4. Set

# list powerss
# 1. Mutable: am object value can be changed after creation
# 2. duplicated: same value can occur multiple time
# 3. ordered: it maintains ordered DS and we can access using their position
# 4. heterogenous: can have multiple data type inside the list.
# N:B: genral format list[start:stop:step]-- slicing
# List Basics:
fruits = ["apple", "banana", "cherry", "orange", "mango"]
numbers = [ 12, 4, 12, 54, 23, 44, 17, 98, 188, 24, 66]
mixed = ["apple", 55, True, 5.8]
# outputs:
print(fruits)
print(fruits[::2])
print(numbers[2::4])

# accessing List through Loop (using index)
print("\nusing index:")
for i in range(len(fruits)):
    print(fruits[i])

for i in range(len(numbers)):
    print(numbers[i], end=" ")

# directly on values:
print("\ndirectly on values:")
for i in fruits:
    print(i)
