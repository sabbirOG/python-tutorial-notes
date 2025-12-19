l = [23, 23, 44, 55, 24,12,33]
l.append(100)
l.append(200)
print(l)
l.insert(0, 500)
print(l)
l.remove(44)
print(l)

l[0] = 10
print(l[0])
print("another")
ll = [-45, 23, -23, 55, -53]
print("positive elements:")
for i in ll:
    if i >= 0:
        print(i, end=" ")
print("\nnegative elements:")
for i in ll:
    if i < 0:
        print(i, end=" ")