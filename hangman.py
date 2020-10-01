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
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Please, enter letter.')
        else:
            return guess

def playAgain():
    # This function returns True, if Player wants do it again. Otherwise, False.
    print('Do you want to play again? Yes or not.')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Allows Player to type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
   
        # Check, if Player won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes. The secret word is ' + secretWord + '! You guessed.')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check, if Player runs over limit of attempts and looses.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You ran out of all attempts.\n Not guessed:' + str(len(missedLetters)) + 'guessed letters ' + str(len(correctLetters)) + '. The word was: ' + secretWord +'.')
            gameIsDone = True
        
        # Check, if Player wants to try again (for the gameover only).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
