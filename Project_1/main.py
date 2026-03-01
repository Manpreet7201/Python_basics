import random
'''
snake water gun game
consider
1 for snake 
-1 for water
0 for gun

Snake 🐍 drinks Water 💧 → Snake wins
Water 💧 damages Gun 🔫 → Water wins
Gun 🔫 kills Snake 🐍 → Gun wins

'''
comp = random.choice([-1, 0, 1])
userstr = input("Enter your choice: ")
myDict = {"s": 1, "w":-1, "g": 0}
user = myDict[userstr]
valueStr = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"Computer chose - {valueStr[comp]} and You chose - {valueStr[user]}")

if comp==user:
    print("Its a tie")
else:
    if (comp == -1 and user==1):     #-2
        print("You win!")
    elif(comp == -1 and user==0):    #-1
        print("Computer Wins!")

    elif (comp == 1 and user==-1):   #2
        print("Computer Wins!")
    elif(comp == 1 and user==0):     #1
        print("You win!")

    elif (comp == 0 and user==-1):   #1
        print("You win!")
    elif(comp == 0 and user==1):     #-1
        print("Computer Wins!")
    else:
        print("Something went wrong.")

    # below code is for pattern wise
    # if (comp-user)==-1 or (comp-user)==2:
    #     print("Computer Wins")
    # else:
    #     print("You Wins")