import random
from words import words
import string
import sys


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    print(display_hangman(lives))

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is  (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in the word.', display_hangman(lives))

        elif user_letter in used_letters:
            print('You have already user that letter')

        else:
            print('Invalid Character')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('He dead... The word was', word)
    else:
        print('You guessed the word!')


def display_hangman(lives):
    stages = [  # final state: 6 attempts
        """
            ________
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            --------------
        """,
        # 5 attempts
        """
            ________
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            --------------
        """,
        # 4 attempts
        """
            ________
            |      |
            |      O
            |     \\|/
            |      |
            |      
            --------------
        """,
        # 3 attempts
        """
            ________
            |      |
            |      O
            |     \\|
            |      |
            |     
            --------------
        """,
        # 2 attempts
        """
            ________
            |      |
            |      O
            |      |
            |      |
            |     
            --------------
        """,
        # 1 attempts
        """
            ________
            |      |
            |      O
            |    
            |      
            |     
            --------------
        """,
        # initial empty state
        """
            ________
            |      |
            |      
            |    
            |      
            |     
            --------------
        """
    ]
    return stages[lives]


hangman()

again = (input("Play again (Y/N)?").upper())
if again == "Y":
    hangman()
else:
    sys.exit()
