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

def getBoardCopy(board):
	# Creates a copy of play field and returns it.
	boardCopy = []
	for i in board:
		boardCopy.append(i)
		return boardCopy

def isSpaceFree(board, move):
	# Returns True, if the move is made to a free spot.
	retrun board[move] == ' '

def getPlayerMove(board):
	# Permission to make a move.
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('Your next move. (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, moveList):
	# Returns any allowed move, bearing in mind the list of moves made and cells filled in.
	# Returns None, if there are no any allowed moves.
	possibleMoves = []
	for i in moveList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter):
	# Checks next allowed move and returns it.
	if computeLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	# This algorithm is for AI of tictactoe game:
	# We check first if we win by the next move.
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, computerLetter, i)
			if isWinner(boardCopy, computerLetter):
				return i

	# Check if User wins by next move and block it.
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, playerLetter, i)
			if is Winner(boardCopy, playerLetter):
				return i

	# Attempt to occupy one of the corners.
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# Attempt to occupy the center.
	if isSpaceFree(board, 5):
		return 5

	# Move along one of the sides.
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	# Returns True if a cell is occupied. Otherwise, returns False.
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True


print('Tic-tac-toe')

while True:
	# Reloading game board.
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('' + turn ' moves first.')
	gameIsPlaying = True
	
	while gameIsPlaying:
		if turn == 'Human.':
			# Player moves.
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if is Winner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Hooray! You\'ve won!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Draw!')
					break
				else:
					turn = 'Computer.'

	else:
		# Computer moves.
		move = getComputerMove(theBoard, computerLetter)
		makeMove(theBoard, computerLetter, move)

		if isWinnder(theBoard, computerLetter):
			drawBoard(theBoard)
			print('Computer won! You lost.')
			gameIsPlaying = False
		else:
			if isBoardFull(theBoard):
				drawBoard(theBoard)
				print('Draw!')
				break
			else:
				turn = 'Human.'

	print('Let\' play again? Yes or No.')
	if not input().lower().startwith('y'):
		break

