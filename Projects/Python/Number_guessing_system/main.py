import random
number = random.randint(1,100)
guess = 0
attempts = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100:"))
    if(guess < number):
        print("Too low! Try again.")
        attempts += 1
    elif (guess > number):
        print("Too high! Try again.")
        attempts += 1
    else:
        print("Congratulations! You guessed the number. The number was", number)
        print("You took", attempts, " attempts to guess the right number." )

print("Thank you for playing the Number Guessing Game!")