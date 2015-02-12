import random
import pygame
import math
class question:
	def __init__(self):
		self.speed = random.randint(1,100)
		self.angle = random.randint(1,100)
		self.gravity = random.randint(1,10)
		self.find = random.randint(1,2)


	def draw(self,screen):
		BLACK    = (   0,   0,   0)
		if self.find == 1:
			words= str("Calculate distance")
		else:
			words = str("Calculate time")
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 20
		screen.blit(text, textpos)
		words2 = "Speed= "+str(self.speed)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 40
		screen.blit(text, textpos)
		words2 = "Angle= "+str(self.angle)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 60
		screen.blit(text, textpos)
		words2 = "Gravity= "+str(self.gravity)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 80
		screen.blit(text, textpos)
	def answer(self):
		if self.find == 1:
			initialvspeed = self.speed*math.sin(self.angle)
			time=(initialvspeed)/math.ceil((self.gravity))
			time=time*2
			return time
		

