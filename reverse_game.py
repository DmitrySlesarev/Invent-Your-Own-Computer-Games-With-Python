# Reverse
import random
import sys
WIDTH = 8 # Game field has 8 cells in width.
HEIGHT = 8 # Game field has 8 cells in height.
def drawBoard(board):
	# Display game field, don't return anything.
	print('   12345678')
	print(' +---------+')
	for y in range(HEIGHT):
		print('%s|' % (y+1), end='')
		for x in range(WIDTH):
			print(board[x][y], end='')
		print('|%s' % (y+1))
	print(' +---------+')
	print('   12345678')

def getNewBoard():
	# Create new data structure of game field.
	board = []
	for i in range(WIDTH):
		board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
	return board

def isValidMove(board, tile, xstart, ystart):
	# Return False, if move to 'xstart', 'ystart' is not allowed.
	# OR return list of all cells, which would be assigned on Player, if he maded a move.
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False

		if tile == 'X':
			otherTile = 'O'
		else:
			otherTile = 'X'

	tilesToFlip = []
	for xdirection, ydirection in [[0,1], [1,1], [1,0], [1, -1], [-1, -1], [-1, 0], [-1, 1]]:
