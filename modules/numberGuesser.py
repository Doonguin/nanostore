# Imports
import os
import random

# Number guesser game
def numberGuesser():
    # Set "guessed" flag to False
    guessed = False

    # Set "guesses left" to the maximum of 4
    guesses = 4

    # Generate number to guess
    numberToGuess = random.randint(1, 50)

    print("Dit is nummer rader. Raad een getal tussen 1 en 50.")

    # Check if the user guessed the number or not
    while guessed == False:
        guess = input("Raad getal: ")

        # Check if the user input is valid
        if (guess == ''):
            while guess == '':
                os.system('cls')
                print('Vul eerst een getal in voordat je op enter drukt')
                guess = input('Raad getal: ')
        
        guess = int(guess)

        # Check if the user has guesses left
        if (guesses == 0):
            os.system('cls')
            print(f"Helaas! Het getal was {numberToGuess}")
            input("Klik op enter om terug te gaan")

            os.system('cls')
            break

        # Handle guesses made by the user
        if (numberToGuess == guess):
            guessed = True
            print(f"Het getal was inderdaad {guess}!")
            exit()
        elif (numberToGuess > guess):
            os.system('cls')
            print(f"Het getal is hoger dan {guess}")
            guesses = guesses - 1
        elif (numberToGuess < guess):
            os.system('cls')
            print(f"Het getal is lager dan {guess}")
            guesses = guesses - 1
            
    return False