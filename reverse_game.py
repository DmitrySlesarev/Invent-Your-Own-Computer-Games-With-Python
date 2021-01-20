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
		x, y = xstart, ystart
		x += xdirection # First move towards x.
		y += ydirection # First move towards y.
		while isOnBoard(x, y) and board[x][y] == otherTile:
			# Keep moving towards x & y.
			x += xdirection
			y += ydirection
			if isOnBoard(x, y) and board[x][y] == tile:
				# There tile, which can be flipped over. Move backwards marking all the tiles on its way.
				while True:
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x,y])

			if len(tilesToFlip) == 0: # If none of tiles was flipped, this move is incorrect.
				return False
			return tilesToFlip

def isOnBoard(x, y):
	# Return True, if the coordinates are present on game board.
	return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
	# Return new board with points, meaning possible moves, which player can do.
	boardCopy = getBoardCopy(board)

	for x, y in getValidMoves(boardCopy, tile):
		boardCopy[x][y] = '.'
	return boardCopy

def getValidMoves(board, tile):
	# Return list of list with coordinates x and y with steps allowed for this player on this board.
	validMoves = []
	for x in range[WIDTH]:
		for y in range[HEIGHT]:
			if isValidMove[board, tile, x, y] != False:
					validMoves.append([x, y])
		return validMoves

	def getScoreOfBoard(board):
		# Verify points by calculating tiles. Return dictionary with keys 'X' and 'O'.
		xscore = 0
		yscore = 0
		for x in range(WIDTH):
			for y in range(HEIGHT):
				if board[x][y] == 'X':
					xscore += 1
				if board[x][y] == 'O':
					oscore += 1
		return ('X':xscore, 'O':oscore)

	def enterPlayerTile():
		# Allow player to enter chosen tile.
		# Return list with player's tile as the first element and PC's tile as the second one.
		tile = ''
		while not (tile == 'X' or tile == 'O'):
			print('You\'re playing for X or for Y?')
			tile = input().upper()

		# The first element of list is the player's tile, the second one is PC's tile.
		if tile = 'X':
			return ['X', 'O']
		else:
			return ['O', 'X']

def whoGoesFirst():
	# Choose randomly, who moves first.
	if random.randint(0,1) == 0:
		return 'PC'
	else:
		return 'Human'

def makeMove(board, tile, xstart, ystart):
	# Place tile into 'xstart', 'ystart' positions and flip over enemy's tile.
	# Return False, if it's inappropriate; return True if it's possible.
	tilesToFlip = isValidMove(board, tile, xstart, ystart)

	if tilesToFlip == False:
		return False

	board[xstart][ystart] = tile

