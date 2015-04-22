import pygame
import main_loop

class slider:


	def __init__(self,variable,pos1,pos2):
		self.variable = variable
		self.pos1 = pos1
		self.pos2 = pos2
		self.moving = False
		self.value = 0
		
	def move(self):
		mousex=pygame.mouse.get_pos()[0]
		mousey=pygame.mouse.get_pos()[1]
		if (mousey>100 and mousey<=200) and (mousex>=self.pos1[0]-5 and mousex<=self.pos1[0]+5) and self.moving == True:
			return mousey
		else:
			return self.pos2[1]
		
	def draw(self,screen):
		RED      = ( 255,   0,   0)
		BLACK    = (   0,   0,   0)
		WHITE    = ( 255, 255,255)
		self.pos2[1] = self.move()
		if self.pos2[1]<100:
			self.pos2[1]=100
		if self.pos2[1]>200:
			self.pos2[1]=200
		words= str(self.value)
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = self.pos1[0]
		textpos.centery = self.pos1[1]-120
		screen.blit(text, textpos)
		words2= self.variable
		font = pygame.font.Font(None, 18)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = self.pos1[0]
		textpos.centery = self.pos1[1]-140
		screen.blit(text, textpos)
		pygame.draw.line(screen,BLACK,(self.pos1[0],self.pos1[1]),(self.pos1[0],self.pos1[1]-100),5)
		pygame.draw.line(screen,BLACK,(self.pos1[0]-5,self.pos2[1]),(self.pos1[0]+5,self.pos2[1]),5)
		

	def getvalue(self,value):
		self.value = value


