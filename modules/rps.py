# Imports
import random
import os

# Define class for Rock Paper Scissors game
class RockPaperScissors:
    # Initialize class and its variables
    def __init__(self):
        self.choices = ['steen', 'papier', 'schaar']
    
    # Get a random choice for the opponent
    def getComputerChoice(self):
        return random.choice(self.choices)

    # Handle getting a choice from the player
    def getUserChoice(self):
        userChoice = input("Kies steen, papier of schaar: ").lower()
        if userChoice not in self.choices:
            print("Ongeldige keuze. Probeer opnieuw.")
            return self.getUserChoice()
        return userChoice

    # Check the choice from both the opponent and the player to determine a winner
    def getWinner(self, userChoice, computerChoice):
        if userChoice == computerChoice:
            return "Het is een gelijkspel!"
        elif (userChoice == 'steen' and computerChoice == 'schaar') or \
             (userChoice == 'papier' and computerChoice == 'steen') or \
             (userChoice == 'schaar' and computerChoice == 'papier'):
            return "Je wint!"
        else:
            return "Je verliest!"
    
    # Start Rock Paper Scissors
    def startRPS(self):
        while True:
            userChoice = self.getUserChoice()
            computerChoice = self.getComputerChoice()
            print(f"Computer kiest: {computerChoice}")
            
            result = self.getWinner(userChoice, computerChoice)
            print(result)
            
            playAgain = input("Wil je nog een keer spelen? (y/N): ").lower()
            os.system('cls')

            if playAgain != "y" or playAgain == "":
                break

        return True