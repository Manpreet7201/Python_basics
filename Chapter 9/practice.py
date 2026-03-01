# Problem 1 read twinkle in poem.txt file
# file = open("poem.txt", "r")
# con = file.read()
# if "twinkle" in con: 
#     print("twinkle exits in poem file.")
# else:
#     print("twinkle not exits in poem file.")
# file.close()


# Problem 2
# a game function that gives user the score of their played game
# import random
# def Game():
#     print("You are playing the game.....")
#     score = random.randint(1,100)
#     with open("Hi-score.txt") as f:
#         hi_score = f.read()
#         if (hi_score != ""):
#             hi_score = int(hi_score)
#         else:
#             hi_score = 0
#     print(f"Your score is :- {score}")
#     if score > hi_score:
#         with open("Hi-score.txt", "w") as f:
#            f.write(str(score))
#     return score
# Game()


# Problem 3
# wap to genate multiplications table from 2 to 20 and write 
# them in diff files and place them in a folder.
# def generateTable(n):
#     table = ""
#     for i in range(1,11):     
#         table += f"{n} * {i} = {n*i}\n"
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)
# for i in range(2,31):
#     generateTable(i)


# Problem 4
# replace donkey word with ###### in a file
# word = "Donkey"
# with open("Donkey.txt", "r") as f:
#     content = f.read()
# contentNew = content.replace(word, "######")
# with open("Donkey.txt", "w") as f:
#     f.write(contentNew)


# Problem 5
# replace a list of words with ###### in a file
# words = ["Donkey", "bad", "ganda"]
# with open("Donkey.txt", "r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, "*"*len(word))
# with open("Donkey.txt", "w") as f:
#     f.write(content)


# Problem 6 
# wap to mine a log file contains python word or not
# with open("log.txt", "r") as f:
#     content = f.read()
# if "python" in content:
#     print("log file contains python name.")
# else:
#     print("log file does not contains python name.")



# Problem 7
# wap to mine a log file contains python word or not in which line
# with open("log.txt", "r") as f:
#     lines = f.readlines()
# lineno = 1
# for line in lines:
#     if "python" in line:
#         print(f"log file contains python name- at line no - {lineno}")
#         break
#     lineno += 1
# else:
#     print("log file does not contains python name.")
    

# Problem 8 
# wap to make a copy of a text file this.txt
# with open("text.txt", "r") as f:
#     content = f.read()
# with open("text_copy.txt", "w") as f:
#     f.write(content)


# Problem 9
# wap to find out whether a file is identical & matches the content of another file
# with open("text.txt", "r") as f:
#     content1 = f.read()
# with open("poem.txt", "r") as f:
#     content2 = f.read()
# if (content1 == content2):
#     print("Yes these files are identical.")
# else:
#     print("No these files are not identical.")


# Problem 10
# wap to wipe out the content of a file.
# with open("text_copy.txt", "w") as f:
#     f.write("")


# Problem 11
# wap to rename a file to renamed_by_python.py
# with open("text.txt", "r") as f:
#     content = f.read()
# with open("renamed_by_python.txt", "w") as f:
#     f.write(content)

# use os module
import os
os.rename("renamed_by_python.txt", "renamed_by_python2.py")
