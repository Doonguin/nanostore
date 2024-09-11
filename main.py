# Imports
from modules.numberGuesser import numberGuesser
from modules.hangman import hangman
import os

# Variables
inGame = False

# Functions
def genTitleScreen(x, y, z):
    # Clear console before starting the program
    os.system('cls')
    
    # Title ASCII art
    print(
        """ 
         █████  ██████  ██████  ██ ███████     ███████ ████████  ██████  ██████  ███████
        ██   ██ ██   ██ ██   ██ ██ ██          ██         ██    ██    ██ ██   ██ ██
        ███████ ██████  ██████  ██ █████       ███████    ██    ██    ██ ██████  █████
        ██   ██ ██      ██      ██ ██               ██    ██    ██    ██ ██   ██ ██
        ██   ██ ██      ██      ██ ███████     ███████    ██     ██████  ██   ██ ███████
        """
    )
    
    # Welcome text + input for game selection
    print("Welkom gebruiker! Selecteer 1 van de 2 ingebouwde games!")
    return input(f"1: {x}\n2: {y}\n3: {z}\n\nJouw keuze: ")

def titleScreenInput(x):
    # Check user input
    match x:
        case "1":
            os.system('cls')
            inGame = True

            # Set the "inGame" flag to false once the game is over
            inGame = numberGuesser()
        case "2":
            os.system('cls')
            inGame = True

            # Set the "inGame" flag to false once the game is over 
            inGame = hangman()
        case "3":
            os.system('cls')
            exit()

# Generate title screen and handle the input
while inGame == False:
    userInp = genTitleScreen("Nummer raden", "Galgje", "sluit store")
    titleScreenInput(userInp)