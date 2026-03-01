# import pyjokes

# # printing jokes
# """ This is an multiline comments
# hjhjh
# elkj
# kkr
# """
# joke = pyjokes.get_joke()

# print (joke)

# print("""
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.

# """)

# print table of 5
# i = 1
# for i in range (1,11):
#     print("5*"+str(i)+"="+ str(5*i))

# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say(" I can speek with you ")
# engine.runAndWait()

import os

# Get the current working directory
current_dir = os.getcwd()

# Print directory name
print("Current Directory:", current_dir)

# List and print all files/folders inside it
print("\nContents:")
for item in os.listdir(current_dir):
    print(item)
