import random

n = random.randint(1,100)
user = -1
count = 0
while (n != user):
    user = int(input("Guess the number- "))
    if (user > n):
        print("Please choose lower number")
        count += 1
    elif (user < n):
        print("Please choose larger number")
        count += 1
    
print(f"You have guessed the right number in {count} guesses for the number {n}. Thanks for playing The Perfect Guess.")