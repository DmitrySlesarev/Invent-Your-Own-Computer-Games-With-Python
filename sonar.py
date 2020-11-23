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

	# Display each of 15 rows.
	for row in range(15):
	# A space should be added to each single-character number.
		if row < 10:
			extraSpace = " "
		else:
			extraSpace = " "

		# Create string for this row on play field.
		boardRow = " "
		for column in range(60):
			boardRow +=board[column][row]

print('%s%s %s %s' % (extraSpace, row, boardRow, row))

	# Display numbers in the in the bottom.
	print()
	print(" " + ("012345678" * 6))
	print(tensDigitsLine)

def getRandomChests(numChests):
	# Create list of data structures.
		chests = []
		while len(chests) < numChests:
			newChest = [random.randint(0, 59), random.randint(0, 14)]
	if newChest not in chests: # Make sure, that the chest is not here.
			chests.append(newChest)
		return chests

	def isOnBoard(x, y):
		# Returns True, if x and y are present on the field. Otherwise, False.
			return x >= 0 and x <= 59 and y >= 0 and y <=14 

		def makeMove(board, chests, x, y):
			# Change data structure, using sonar symbol. Delete chests,
			# as soon as you got them. Return False, if the move is
			# not possible. Otherwise, return string with result.
			smallestDistance = 100 # All the chest will be placed nearer, than 100 items.
			for cx, cy in chests:
				distance = math.sqrt((cx-x)*(cx-x) + (cy-y)*(cy-y))

if distance < smallestDistance: # We need the nearest chest.
	smallestDistance = distance

	smallestDistance = round(smallestDistance)
# XY belongs to the chest of treasures.
	chest.remove([x, y])
return 'You\'ve found chest with treasures.'
	else:
		if smallestDistance < 10:
			board[x][y] = str(smallestDistance)
return 'Chest with treasures can be seen at a distance of %s from the sonar' % (smallestDistance)
	else:
		board[x][y] = 'X'
return 'Sonar has found nothing. All the chests with treasures are not reachable now.'

def enterPlayerMove(previousMoves):
	# Allow Player to make a a move. Return list of 2 elements with x and y coordinates.
	print("Where should we put the sonar? Coordinates: 0-59 0-14. Or exit.)")
	while True:
		move = input()
		if move.lower() == 'exit':
			print('Thanks for the game!')
			sys.exit()

		move = move.split()
if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
		if [int(move[0]), int(move[1])] in previousMoves:
			print("You've already put the sonar here.")
				continue

			print('Enter number from 0 to 59, then space, and then the number from 0 to 14.')

def showInstructions():
	print('''Instructions
You're a captain of the ship. Your purpose is to find
treasures using sonars.
But sonars are very simple andcan detect just the distance,
but not the direction.
Enter coordinates so that to put sonar into water. The
map will show number, where the chest is . Or
a letter 'X' will be shown, which means that there are no
chests in locator's vision area.
May with 'C' - chests.

Press 'Enter' to proceed.
''')
	input()

	print()

					
