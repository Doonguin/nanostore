# Imports
import os
import random

# Public variables
words = [
    "python", "programmeren", "utrecht",
    "hogeschool", "opleiding", "stephan"
]
chosenWord = words[random.randint(0, 5)]
dashes = []

# Create the dashed according to the length of the word
for c in chosenWord:
    dashes += "_"

# Functions
def hangman():
    guessed = False

    while guessed == False:
        print(chosenWord)
        print(dashes)

        inp = input("Raad letter: ")
    
    

    return False