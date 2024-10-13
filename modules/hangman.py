import os
import random

# Define class for hangman game
class Hangman:
    # Initialize class and its variables
    def __init__(self, wordFile, maxTries=6):
        self.wordFile = wordFile
        self.maxTries = maxTries
        self.word = ""
        self.guessedLetters = set()
        self.incorrectGuesses = 0
        self.triesLeft = maxTries

    # Load words from the dict.txt file
    def loadWords(self):
        with open(self.wordFile, 'r') as file:
            return file.read().splitlines()

    # Select a random word from the loaded words
    def chooseWord(self):
        words = self.loadWords()
        if not words:
            return None
        self.word = random.choice(words).lower()

    # Display the current progress of the word (guessed vs unguessed letters)
    def displayCurrentProgress(self):
        display = [letter if letter in self.guessedLetters else '_' for letter in self.word]
        print(' '.join(display))

    # Check if the guessed letter is valid and update guessed letters and tries
    def checkGuess(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            print("Vul alsjeblieft een geldige letter in!")
            return False
        
        if guess in self.guessedLetters:
            print("Je hebt deze letter al geraden!")
            return False

        self.guessedLetters.add(guess)

        if guess not in self.word:
            print(f"{guess} zit niet in het woord")
            self.incorrectGuesses += 1
            self.triesLeft = self.maxTries - self.incorrectGuesses

        return True

    # Check if the player has guessed the word correctly
    def hasWon(self):
        return all(letter in self.guessedLetters for letter in self.word)

    # Start the game
    def startHangman(self):
        input("Uw naam: ")

        self.chooseWord()
        if not self.word:
            print("Fout bij het laden van woordenbestand.")
            return

        print(f"Welkom bij Hangman! Het woord heeft {len(self.word)} letters.")
        self.displayCurrentProgress()

        while self.triesLeft > 0:
            print(f"\nPogingen: {self.triesLeft}")
            print(f"Geraden letters: {', '.join(sorted(self.guessedLetters)) if self.guessedLetters else 'None'}")
            
            guess = input("Raad een letter: ").lower()
            os.system('cls')

            if not self.checkGuess(guess):
                self.displayCurrentProgress()
                continue

            self.displayCurrentProgress()

            if self.hasWon():
                print(f"\nJe hebt het woord geraden: {self.word}!")
                input("(Druk op enter om door te gaan)")
                os.system('cls')
                return
            
        # If the player doesn't have any guesses left
        print(f"\nJe hebt geen pogingen meer... Het woord was: {self.word}")
        input("(Druk op enter om door te gaan)")
        os.system('cls')