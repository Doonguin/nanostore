# Imports
import random
import os

# Define class for number guesser game
class NumberGuesser:
    # Initialize class and its variables
    def __init__(self, minNum = 1, maxNum = 50, maxAtt = 5):
        self.minNum = minNum
        self.maxNum = maxNum
        self.maxAtt = maxAtt

        self.guessed = False
        self.attempts = 0
        self.numberToGuess = random.randint(self.minNum, self.maxNum)
    
    # Define guess function so the player can guess and the program keeps track of guesses
    def guess(self, guess):
        self.attempts += 1
        
        if (guess < self.numberToGuess):
            os.system('cls')
            return f"Het nummer is hoger dan {guess}"
        elif (guess > self.numberToGuess):
            os.system('cls')
            return f"Het nummer is lager dan {guess}"
        else:
            os.system('cls')
            return f"Gefeliciteerd! Het nummer was inderdaad {guess}"
    
    # Check if the player has any guesses left
    def hasGuesses(self):
        return self.attempts < self.maxAtt

    # Define the start function to execute the game
    def startNumberGuesser(self):
        print(f"Welkom bij number guesser! Je hebt {self.maxAtt} pogingen om een cijfer tussen de {self.minNum} en {self.maxNum} te raden.")

        # As long as the player has guesses left make the game run
        while self.hasGuesses():
            try:
                guess = int(input("raad nummer: "))
                result = self.guess(guess)

                print(result)

                if (result == f"Gefeliciteerd! Het nummer was inderdaad {guess}"):
                    self.guessed = True
                    break

            except ValueError:
                print("Je hebt iets anders dan een nummer ingevuld! Probeer het opnieuw.")
        
        if (self.attempts == self.maxAtt and not self.guessed):
            print(f"Je hebt het nummer helaas niet geraden.... Het nummer was {self.numberToGuess}")
        
        input("(Druk op enter om door te gaan)")
        os.system('cls')