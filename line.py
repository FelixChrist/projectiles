import pygame
import math
import projectile
import main_loop

class line:
	def __init__ (self):
		self.xcoords= []
		self.ycoords= []

	def draw(self,screen,coords):
		BLACK    = (   0,   0,   0)
		while coords[1] < 601:
			coords2 = projectile1.launch(coords)
			pygame.draw.line(screen,BLACK,(coords[0],coords[1]),(coords2[0],coords2[1]),1)
			coords=coords2






