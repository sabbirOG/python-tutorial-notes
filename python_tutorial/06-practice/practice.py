# check if list in sorted or not
n = list(map(int, input("enter values:\n").split()))
for i in range(len(n)-1):
    if n[i] < n[i+1]:
        continue
    else:
        print("List is not sorted!")
        break
else:
    print("List is sorted.")