# Imports
import os
from modules.numberGuesser import NumberGuesser
from modules.hangman import Hangman
from modules.rps import RockPaperScissors

# Define class for the main menu
class menu():
    # Initialize class and its variables
    def __init__(self):
        self.options = {
            "1": "Nummerraad spel",
            "2": "Galgje",
            "3": "Steen, Papier, Schaar",
            "4": "Verlaat PromptPlay"
        }

    # Function that handles displaying the main menu
    def displayMenu(self):
        print("Welkom bij PromptPlay!")

        for num, desc in self.options.items():
            print(f"{num}: {desc}")
    
    # Handle the numberguesser game starting when the player chooses to play numberguesser
    def gameNumberGuesser(self):
        game = NumberGuesser(minNum=1, maxNum=50, maxAtt=5)
        game.startNumberGuesser()

    # Handle the hangman game starting when the player chooses to play hangman
    def gameHangman(self):
        game = Hangman(wordFile="modules\dict.txt")
        game.startHangman()

    # Handle the Rock Paper Scissors game starting when the player chooses to play Rock Paper Scissors
    def gameRockPaperScissors(self):
        game = RockPaperScissors()
        game.startRPS()

    # Handle choices made in the main menu and react accordingly
    def choiceHandler(self, choice):
        match choice:
            case 1:
                os.system('cls')
                self.gameNumberGuesser()
            case 2:
                os.system('cls')
                self.gameHangman()
            case 3:
                os.system('cls')
                self.gameRockPaperScissors()
            case 4:
                os.system('cls')
                print("PromptPlay is afgesloten!")
                return False
            case _:
                os.system('cls')
                print("Ongeldige keuze! Probeer opnieuw.")

        return True

    # Start the menu and make sure the menu always gets displayed using a while True loop
    def start(self):
        os.system('cls')

        while True:
            try:
                self.displayMenu()
                choice = int(input("Maak uw keuze: "))
                if not self.choiceHandler(choice):
                    break

            except ValueError:
                os.system('cls')
                print("Graag een geldige optie kiezen!")

# Start the menu
menu().start()