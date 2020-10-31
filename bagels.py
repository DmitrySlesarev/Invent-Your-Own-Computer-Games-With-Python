import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
	# Returns string of distinct figures, which is of length of NUM_DIGITS.
	numbers = list(range(10))
	random.shuffle(numbers)
		secretNum = ''
		for i in range(NUM_DIGITS):
			secretNum += str(numbers[i])
		return secretNum

def getClues(guess, secretNum):
	# Retursn string with hints 'Warm', 'Hot', 'Cold'.
	if guess == secretNum:
		return 'You\'ve guessed!'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Hot.')
		elif guess[i] in secretNum:
			clues.append('Warm.')
	if len(clues) == 0:
		return 'Cold.'

	clues.sort()
	return ' '.join(clues)

def isOnlyDigits(num):
	# Returns True, if num is string, consisting of figures only. Otherwise, returns False.
	if num == '':
		return False

	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False

		return True

	print('Let me make a %s-digit number.' % (NUM_DIGITS))
	print('Will give some hints...')
	print('When I say:   It means:')
	print(' Cold		 None of the figues are guessed.')
	print(' Warm 		 One of the figures is correct.')
	print(' Hot			 One of the figures is correct and in its place.')

	while True:
		secretNum = getSecretNum()
		print('So, I thought of the figure. You\'ve got %s attempts to guess it.' % (MAX_GUESS))

		guessesTaken = 1
		while guessesTaken <= MAX_GUESS:
			guess = ''
			while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
				print('Attempt #%s: ' % (guessesTaken))
				guess = input()

			print(getClues(guess, secretNum))
			guessesTaken +=1

			if guess == secretNum:
				break
			if guessesTaken > MAX_GUESS:
				print ('No more attempts are left. I thought of %s.' % (secretNum))
	print('Do you want to play again? Yes or no?')
	if not input().lower().startswith('y'):
		break