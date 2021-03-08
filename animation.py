import pygame, sys, time
from pygame.locals import *

# Pygame installation.
pygame.init()

# Window setting.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# Variables of direction.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Color setting.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Data structure.
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect': pygame.Rect(100, 1500, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# First game cycle start.
while True:
	# Check of QUIT event.
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# Creating white background.
	windowSurface.fill(WHITE)

	for b in boxes:
		# Moving data structure.
		if b['dir'] == DOWNLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == DOWNRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == UPLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top -= MOVESPEED
		if b['dir'] == UPRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top -= MOVESPEED

	# Check if the block touches window border.
		if b['rect'].top < 0:
			# Upper border.
			if b['dir'] == UPLEFT:
				b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
				b['dir'] = DOWNRIGHT
		if b['rect'].bottom > WINDOWHEIGHT:
			# Lower border.
			if b['dir'] == DOWNLEFT:
				b['dir'] == UPLEFT
			if b['dir'] == DOWNRIGHT:
				b['dir'] = UPRIGHT
		if b['rect'].left < 0:
			# Left border.
			if b['dir'] == DOWNLEFT:
				b['dir'] = DOWNRIGHT
			if b['dir'] == UPLEFT:
				b['dir'] = UPRIGHT
		if b['rect'].right > WINDOWWIDTH:
			# Right border.
			if b['dir'] == DOWNRIGHT:
				b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
				b['dir'] = UPLEFT

		# Create block on the surface.
		pygame.draw.rect(windowSurface, b['color'], b['rect'])

	# Display.
	pygame.display.update()
	time.sleep(0.02)
