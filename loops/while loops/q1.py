n = int(input("number?"))
copy = n
rev = 0
while n > 0:
    rev = n % 10
    print(rev, end="")
    n = n // 10 
    
if copy == rev :
    print("pallindrom")
else:
    print("not")