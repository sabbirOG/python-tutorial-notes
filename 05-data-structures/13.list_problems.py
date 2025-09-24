# prb-1: print positive and negative elements of a list

pos_neg = [12, -3, -4, -52, 12, 55, 77, -9, 9, -95]
for i in range(len(pos_neg)):
    if pos_neg[i] > 0:
        print(f"positive elements:{pos_neg[i]}")
    else:
        print(f"negative elements: {pos_neg[i]}")
# alternative: 
pos_neg = [12, -3, -4, -52, 12, 55, 77, -9, 9, -95]
print("positive elements are:")
for i in pos_neg:
    if i > 0:
        print(i)
print("negative elements are:")
for i in pos_neg:
    if i < 0:
        print(i)

# prb-2: mean of list elements:
elements = [12, -3, -4, -52, 12, 55, 77, -9, 9, -95]
total = 0
for i in range(len(elements)):
    total += elements[i]
    mean = total / len(elements)
print(f"average:{mean}")

# prb-3: find the greatest element and print its index too
num = [12, 4, 2, 42, 542, 845, 100, 142, 900, 28, 23,54,5]
max_element = 0
max_index = 0
for i in range(len(num)):
    if num[i] > max_element:
        max_element = num[i]
        max_index = i
print(f"Greatest element:{max_element}")
print(f"max index:{max_index}")

# prb-4: find the second greatest element
lst = [12, 4, 2, 42, 542, 845, 100, 142, 2500, 28, 23,54,5]
max_value = lst[0]
second_max = lst[0]
for i in range(len(lst)):
    if lst[i] > max_value:
        max_value = lst[i]
for i in range(len(lst)):
    if lst[i] > second_max and lst[i] < max_value:
        second_max = lst[i]
print(f"second_max:{second_max}")

