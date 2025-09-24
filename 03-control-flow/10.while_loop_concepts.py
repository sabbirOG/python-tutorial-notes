"""# it needs a condition 
n = int(input("enter your digits:\n"))
while n > 0:
    print(n % 10, end= "")
    n = n// 10
# alternative 
n = int(input("\nEnter digits:\n"))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10 
    n = n // 10

print(rev)

"""

# digit guessing game
import random
random_number = random.randint(1, 21)
tries = 0

while  True:
    guess = int(input("guess the number from (1 to 20): "))
    if random_number == guess:
        tries += 1
        print(f"guessed it right in {tries}")
        break
    elif guess > random_number:
        print("go a little lower!")
        tries += 1
    elif guess < random_number:
        print("go a little higher")
        tries += 1
    else:
        tries += 1
        print("sorry! wrong guessed!")