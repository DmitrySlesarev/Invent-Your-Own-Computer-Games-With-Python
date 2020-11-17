# Treasure hunter.

import random
import sys
import math

def getNewBoard():
	# creating data structure for the field of 60x15.
	board = []
	for x in range(60): # The main list, which contains of 60 lists.
		board.append([])
	for y in range(15): # Each list contains 15 single-variable line.
	# Let's make the ocean various, so that to make it real.
		if random.randint(0, 1) == 0:
			board[x].append('^')
		else:
			board[x].append('\'')
	return board

def drawBoard(board):
	# Represent data structure of play field.
	tensDigitsLine = ' ' # Create place for numbers down the left side of the playfield.
	for i in range(1, 6):
		tensDigitsLine += (' ' * 9) + str(i)

	# Reflect the numbers in the upper part of play field.
	print(tensDigitsLine)
	print(' ' + ('0123456789' * 6))
	print()	