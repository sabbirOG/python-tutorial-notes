print("mean using for loop and function:\n")
nums = list(map(int, input("enter numbers with space:").split()))

def mean(lst):
    total = 0
    for i in lst:
        total = total + i
    return total/len(lst)

print("Mean:", mean(nums))

print("using while loop:\n")
nums = []

while True:
    value = input("enter number")
    if value == 'q':
        break
    nums.append(int(value))

print("Mean: ", sum(nums) / len(nums))