#-*-coding:utf-8-*-
import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
        ===''', '''
    +---+
    0   |
        |
        |
        ===''', '''
    +---+
    0   |
    |   |
        |
        ===''', '''
    +---+
    0   |
   /|   |
        |
        ===''', '''
    +---+
    0   |
   /|\  |
        |
        ===''', '''
    +---+
    0   |
   /|\  |
   /    |
        ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
        ===''']

words = 'shark monkey ram badger biver bull camel wolf sparrow raven pigeon snake goat cow cat rabbit rat chicken lion fox salmon moose bear mouse ape ship deer donkey spider python parrot dog tiger duck turtle hawk lizard'.split()

def getRandomWord(wordList):
    # This function takes random string from the list.
    wordIndex = random. randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Wrong letters:', end=' ')
    for letter in missedLetters:
    	print(letter, end=' ')
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)): # changes skips for guessed letters
    if secretWord[i] in correctLetters:
    	blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # shows secret word with whitespaces between letters
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns letter, entered by Plaler. The function checks, that Player enters single letter only, nothing more.
    while True:
    	print("Enter a letter.")
    	guess = input()
    	guess = guess.lower()
    	if len(guess) != 1:
    		print("Just one letter, please!")
    	elif guess in alreadyGuessed:
    		print("You've alredy tried it. Enter another character, please!")
    	elif guees not in 'qwertyuiopasdfghjklzxcvbnm':
    		print('Please, enter letter.')
    	else:
    		return guess


