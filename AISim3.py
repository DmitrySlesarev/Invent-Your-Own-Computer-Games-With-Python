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
		for x, y in tilesToFlip:
			board[x][y] = tile
		return

def getBoardCopy(board):
	# Copy board list and return it.
	boardCopy = getNewBoard()

	for x in range(WIDTH):
		for y in range(HEIGHT):
				boardCopy[x][y] = board[x][y]

	return boardCopy

def isOnCorner(x, y):
	# Return True, if the position is in one of the corners.
	return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getPlayerMove(board, playerTile):
	# Allow Player make a move.
	# Return move like [x, y] or return 'hint' or 'exit'.
	DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
	while True
	print('Type your move, \'exit\' or \'hint\'.')
		move = input().lower()
		if move == 'exit' or move == 'hint':
			return move

		if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
			x = int(move[0]) - 1
			y = int(move[1]) - 1
			if isValidMove(board, playerTile, x, y) == False
				continue
			else:
				break
		else:
			print('It is unacceptable. Enter column number (1-8) and row number (1-8).')
			print('For example, value 81 move to the upper right corner.')

	return [x, y]

def getCornerBestMove[board, computerTile]
	# Bearing in mind the current game board, check
	# where to move and return this move like [x, y].
	possibleMoves = getValidMoves(board, computerTile)
	random.shuffle(possibleMoves) # Make moves random.

	# Always make move to the corner, whenever it's possible.
	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]

	# Find a move with the most possible amount of points.
	bestScore = -1
	for x, y in possibleMoves:
		boardCopy = getBoardCopy(board)
		makeMove(boardCopy, computerTile, x, y)
		score = getScoreOfBoard(boardCopy)[computerTile]
		if score > bestScore:
			bestMove = [x, y]
			bestScore = score
	return bestMove

def getWorstMove(board, tile):
	# Return move, which flips the most amount of tiles.
	possibleMoves = getValidMoves(board, tile)
	random.shuffle(possibleMoves) # randomize order of moves.

	# Find a move with the least possible score.
	worstScore = 64
	for x, y in possibleMoves:
			boardCopy = getBoardCopy(board)
			makeMove(boardCopy, tile, x, y)
			score = getScoreOfBoard(boardCopy)[tile]
			if score < worstScore:
				worstMove = [x, y]
				worstScore = score

	return

def getRandomMove(board, tile):
	possibleMoves = getValidMoves(board, tile)
	return random.choice(possibleMoves)

def isOnSide(x, y):
	return x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1

def getCornerSideBestMoves(board, tile):
	# Return the corner move, boarder move or the best move.
	possibleMoves = getValidMoves(board, tile)
	random.shuffle(possibleMoves) # Randomize order of moves.

	# Always make a move to the corner, where possible.
	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]

	# If corner move is not possible, return border move.
	for x, y in possibleMoves:
		if isOnSide(x, y):
			return [x, y]

	return getCornerBestMove(board, tile) # Do what common AI does.

def printScore(board, playerTile, computerTile):

def playGame(playerTile, computerTile):
	showHints = False
	turn = whoGoesFirst()
	print(turn + ' moves first.')

	# Clean game board and put initial tiles.
	board = getNewBoard()
	board[3][3] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'
	board[4][4] = 'X'

	while True:
		playerValidMoves = getValidMoves(board, playerTile)
		computerValidMoves = getValidMoves(board, computerTile)

		if playerValidMoves = [] and computerValidMoves == []:
			return board # No more moves, game over.

		elif turn == 'Human': # Human's move.
			if playerValidMoves != []:
				#if showHints:
				#	validMovesBoard = getBoardWithValidMoves(board, playerTile)
				#	drawBoard(validMovesBoard)
				#else:
					#drawBoard(board)
				#printScore(board, playerTile, computerTile)

				move = getCornerBestMove(board, playerTile)
				#if move == 'exit':
				#	print('Thank you for the game.')
				#	sys.exit() # End the game.
				#elif move == 'hint':
				#	showHints = not showHints
				#	continue
				#else:
				makeMove(board, playerTile, move[0], move[1])
				turn = 'Computer'

			elif turn == 'Computer': # Computer's move.
				if computerValidMoves != []:
					#drawBoard(board)
					#printScore(board, playerTile, computerTile)

					#input('Press Enter to see Computres\' move.')
					move = getWorstMove(board, computerTile)
					makeMove(board, computerTile, move[0], move[1])
				turn = 'Human'

NUM_GAMES = 250
xWins = oWins = ties = 0
print('Greetings!')

playerTile, computerTile = ['X', 'O'] #enterPlayerTile()

for i in range(NUM_GAMES): # while True:
	finalBoard = playGame(playerTile, computreTile)

	# Show the score.
	#drawBoard(finalBoard)
	print('#%s got %s points. O got %s points.' % (i+1, scores['X'], scores['O']))
	if scores[playerTile] > scores[computerTile]:
		xWins += 1 # print('You won the computer, the gap is  %s points. Congrats!' % (scores[playerTile] - scores[computerTile]))	
	elif scores[playerTile] < scores[computerTile]:
		oWins += 1 # print('You\'ve lost. The gap is %s points.' % (scores[computerTile] - scores[playerTile]))
	else:
		ties += 1 # print('Draw!')

				
	# print('You want to play again? Yes or No.')
	# if not input().lower().startswith('y'):
	#	break

print('Amount of lost games X: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
print('Amount of won games Y: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
print('Amount of draws: %s (%s%%)' % (ties, round(ties/ NUM_GAMES * 100, 1)))


