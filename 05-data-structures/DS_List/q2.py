a = [12, 232, 523, 52, True, -23, 2,-2,-2, -423, 53]

print(a[4:9:2])

print("another version:")
for i in range(len(a)):
    print(a[i], end=" ")
print("\n")
for i in range(len(a)):
    print(f"index {i} is {a[i]}")

print("version 3:\n")
print("printing values only:")
for i in a:
    print(i, end=" ")