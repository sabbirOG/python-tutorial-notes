import random 
num = random.randint(1, 20)

tries = 0
while True:
    guess = int(input("guess a number between 1 to 20: "))
    
    if guess == num:
        print("you win!")
        break
    else:
        tries = tries+1
        print("try again",tries)