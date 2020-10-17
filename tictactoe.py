# Tic-tac-toe

import random

def drawBoard(board):
	# This function displays empty game field.

	# 'board' - is just a list of 10 lines (index '0' gets disregarded).
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
	# Permission to enter the chosen letter.
	# Returns list, where the first letter belongs to User, the second one belongs to CPU.
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you prefer X or O?')
		letter = input().upper()

		# CPU checks letter.
		if letter == 'X':
			return ['X', 'O']
		else:
			return['O', 'X']

def whoGoesFirst():
	# The choice of who goes first.
	if random.randint(0,1) == 0:
		return 'Computer.'
	else:
		return 'Human.'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	# The decision who wins.
	# 'bo' is used instead of 'board' and 'le' is instead of 'letter' :)
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # accross the top
		(bo[4] == le and bo[5] == le and bo[6] == le) or # accross the center
		(bo[1] == le and bo[2] == le and bo[3] == le) or # accross the bottom
		(bo[7] == le and bo[4] == le and bo[1] == le) or # across the bottom left side
		(bo[8] == le and bo[5] == le and bo[2] == le) or # accross the cener
		(bo[9] == le and bo[6] == le and bo[3] == le) or # accross the bottom right side
		(bo[7] == le and bo[5] == le and bo[3] == le) or # diagonally
		(bo[9] == le and bo[5] == le and bo[1] == le) or # diagonally