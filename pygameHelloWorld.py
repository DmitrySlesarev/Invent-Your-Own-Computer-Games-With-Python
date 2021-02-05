import pygame, sys
from pygame.locals import *

# Adjust pygame.
pygame.init()

# Adjust window.
windowSurface = pygame.display.set_mode((500, 400), 0 , 32)
pygame.display.set_caption('Hello, world!')

# Assign colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Assign fonts.
basicFont = pygame.font.sysFont(None, 48)

# Adjust text.
text = basicFont.render('Hello, World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centrex = windowSurface.get_rect().centrex
textRect.ecntrey = windowSurface.get_rect().centery

# Make background color white.
windowSurface.fill(WHITE)

# Add green triangle.
pygame.draw.polygon(windowSurface, GREEN, ((146, 0),(291, 106), (236, 277), (56, 277), (0, 106)))

# Add blue lines.
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)

# Add blue circle.
pygame.draw.circle(windowSurface, BLUE, (300, 500), 20, 0)

# Add red ellipse.
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Add rectange with text block.
pygame.draw.rect(windowSurface, RED, (textRect.left-20, textRect.top-20, textRect.width+40, textRect.height+40))

# Get surface of pixels.
pixArreay = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Add text to the surface.
windowSurface.blit(text, textRect)

# Display.
pygame.display.update()

# Start play circle.
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
