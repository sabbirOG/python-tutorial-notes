n = "sabbir"

for i in range(len(n)):
    print(i+1)

print("another way")
n = "sabbir"

for i in range(1, len(n)+1):
    print(i)

print("more method: int version")

num = "5230"
for index, value in enumerate(num, start = 1):
    print(index)

print("more method: string version")

text = "hello"
for i, char in enumerate(text, start=1):
    print(f"Index:{i}, character:{char}")