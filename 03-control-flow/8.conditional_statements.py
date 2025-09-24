money = int(input("What is your salary?"))

if money < 20:
    print("You are not eligible for the loan")
elif money >= 90:
    print("You are eligible for 5 lakhs taka loan!, for more money talk to the manager")
elif money > 70:
    print("You can get 3 lakhs taka loan")
elif money >= 40:   # checking (or)
    print("You can get 2 lakhs taka loan!")
else:
    print("Talk to the manager please")


# another example:
gender = input("What is your gender? (M or F)\n").lower()

if gender == 'm':
    print("Good Morning Sir!")
elif gender == 'f':
    print("Good Morning Mam!")
else:
    print("Good Morning!")

# let's solve a problem
# find a year if the year is a leap year 

"""year = int(input("What is the year?"))

if year%4 == 0:
    print("this is a leap year!")
else:
    print("this is not a leap year!")"""
