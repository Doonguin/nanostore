# Imports
import os
import random

# Public variables
def load_words(file_name):
        with open(file_name, 'r') as file:
            words = file.read().splitlines()
        return words

def choose_word(words):
    # Select a random word from the words file
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    # Give the user feedback about the length of the word and whether a letter is in the word or not
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display))

def hangman():
    # Load the words file
    words = load_words('modules/dict.txt')
    
    # Check if the words from the file were loaded correctly, otherwise exit the aplication
    if not words:
        return False

    # Set the needed variables for the game to work
    word = choose_word(words).lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_tries = 6
    tries_left = max_tries

    print(f"Welcome to Hangman! Het woord heeft {len(word)} letters.")
    display_current_progress(word, guessed_letters)

    while tries_left > 0:
        print(f"\nPogingen: {tries_left}")
        print(f"Geraden letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        guess = input("Raad een letter: ").lower()
        os.system('cls')

        # Check if the guesses character is a letter and not something else
        if len(guess) != 1 or not guess.isalpha():
            os.system('cls')
            print("Vul alsjeblieft een letter in!")
            continue
        
        # Check if the player has already guessed this letter otherwise add the letter to the guessed letters
        if guess in guessed_letters:
            os.system('cls')
            print("Je hebt deze letter al geraden!")
            continue

        guessed_letters.add(guess)

        # If the guessed letter is not in the word at take away one try
        if guess not in word:
            os.system('cls')
            print(f"{guess} zit niet in het woord")
            incorrect_guesses += 1
            tries_left = max_tries - incorrect_guesses

        # Show the current progress of the word with its guessed and unguessed letters
        display_current_progress(word, guessed_letters)

        # Check if the user guessed all the letters and end the game if so
        if all(letter in guessed_letters for letter in word):
            os.system('cls')
            print(f"\nJe hebt het woord geraden: {word}!")
            input("(Druk op enter om door te gaan)")

            return False
            
    # If the user doesn't have any tries left end the game with a loss
    else:
        os.system('cls')
        print(f"\nJe hebt helaas geen pogingen meer over... Het woord was: {word}")
        input("(Druk op enter om door te gaan)")

        return False