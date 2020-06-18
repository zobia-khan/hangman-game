import random, sys
from typing import List

WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) # lets randomize single word from the list
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

# Utility functions

def print_word_to_guess(letters: List):
    """Utility function to print the current word to guess"""
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int):
    """Prints how many chances the player has used"""
    print(f"You are on guess {current}/{total}.")
def print_warnings(current: int, total: int):
    """Prints how many chances the player has used"""
    print(f"You are on warning {current}/{total}.")

# Game functions

def beginning():
    """Starts the game"""
    print("Hello Mate!\n")
    while True:
        name = input("Please enter Your name\n").strip()
        if name == '':
            print("You can't do that! No blank lines")
        else:
            break
def prepare_secret_word():
    """Prepare secret word and inform user of it"""
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("Ok, so the word You need to guess has", LENGTH_WORD, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing():
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    guess_taken = 0
    MAX_GUESS = 6
    MAX_WARNINGS=3
    warnings_left=0
    hanger=['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''','''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                
                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 
                                       
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS :
        guess = input("Pick a letter\n").lower()
        list_of_alpha=list(ALPHABET)
        list_of_alpha.remove(guess)
        alpha=str(list_of_alpha)
        if not guess in ALPHABET and warnings_left!=3:#checking input
            print("Enter a letter from a-z ALPHABET")
            warnings_left+=1
            print_warnings(warnings_left,MAX_WARNINGS)
        elif warnings_left==3 and not guess in ALPHABET :
            print('you have no warnings left so you lose one guess')
            guess_taken += 1
            print_guesses_taken(guess_taken, MAX_GUESS)
            if guess_taken == 6 :
                print(f" Sorry Mate, You lost :<! The secret word was {SECRET_WORD}")
        elif guess in letter_storage and warnings_left!=3: #checking if letter has been already used
            print("You have already guessed that letter!")
            warnings_left+=1
            print_warnings(warnings_left,MAX_WARNINGS)
            print(alpha)
        elif warnings_left==3 and guess in letter_storage  :
            print('you have no warnings left so you lose one guess')
            guess_taken += 1
            print_guesses_taken(guess_taken, MAX_GUESS)
            print(alpha)
            if guess_taken == 6 :
                 print(f" Sorry Mate, You lost :<! The secret word was {SECRET_WORD}")
        elif len(guess)!=1:
            print('enter one character at a time')
        else: 
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print(alpha)
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:    #winning condition
                    print(hanger[7])
                    print("You won!")
                    print("Game Over!")
                    break
            else: #losing condition
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print(hanger[guess_taken])
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 6 :
                    print(f" Sorry Mate, You lost :<! The secret word was {SECRET_WORD}")
beginning()
prepare_secret_word()
guessing()

    
        
        
    
    
