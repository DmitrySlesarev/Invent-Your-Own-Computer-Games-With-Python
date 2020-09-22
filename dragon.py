import random
import time

def displayIntro():
	print ("""You're in front of 2 cages with dragons.
The first one is going to eat you, while
the second cant share some treasures.
Choose wisely & good luck!""")
	print()

def chooseCave():
	cave = ""
	while cave != "1" and cave != "2":
		cave = str(input("Type '1' or '2' to choose cave: "))
	return cave

def checkCave(value1):
	print("You're coming to the cave.")
	time.sleep(2)
	print("You're shivering with fear.")
	time.sleep(2)
	print()
	value2 = str(random.randint(1,2))
	if value1 == value2:
		print ("The dragon shares its treasures!")
	else:
		print ("The dragon eats you!")

playAgain="Yes"
displayIntro()
while playAgain == "Yes" or playAgain == "y" or playAgain == "yes":
	choice = chooseCave()
	checkCave(choice)
	playAgain = input("Do you want to play again? Yes or no? ")