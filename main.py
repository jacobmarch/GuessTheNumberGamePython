import random

answer = random.randint(1,100)
numGuess = 0
userGuess = 0

while userGuess != answer:
    if numGuess == 0:
        try:
            userGuess = int(input("Enter your first guess: "))
        except ValueError:
            print("Please enter a base 10 integer. Thank you.")
            continue
    else:
        try:
            userGuess = int(input("Enter your next guess: "))
        except ValueError:
            print("That was not a valid number. Please try again.")
            continue
    numGuess += 1
    if userGuess == answer:
        print("You got the correct answer in " + str(numGuess) + " guesses!")
    elif userGuess < answer:
        print("The number is higher than your guess.")
    elif userGuess > answer:
        print("The number is less than your guess.")

exit