import random
import pygame
import math
import eztext
class question:
	def __init__(self):
		self.speed = random.randint(1,100)
		self.angle = random.randint(20,80)
		self.gravity = random.randint(1,10)
		self.find = random.randint(1,2)
		self.txtbx = eztext.Input(maxlength=45, color=(0,0,0), prompt='Type here: ')
		self.error = False



	def draw(self,screen):
		BLACK    = (   0,   0,   0)
		if self.find == 1:
			words= str("Calculate time")
		else:
			words = str("Calculate distance")
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 25
		screen.blit(text, textpos)
		words2 = "Speed= "+str(self.speed)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 45
		screen.blit(text, textpos)
		words2 = "Angle= "+str(self.angle)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 65
		screen.blit(text, textpos)
		words2 = "Gravity= "+str(self.gravity)
		font = pygame.font.Font(None, 26)
		text = font.render(words2, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 100
		textpos.centery = 85
		screen.blit(text, textpos)

		
		self.txtbx.draw(screen)
		events = pygame.event.get()
		self.txtbx.update(events)
		
		
		
	def answer(self):
		if self.find == 1:
			initialvspeed = self.speed*math.sin(self.angle*math.pi/200)
			time=(initialvspeed)/math.ceil((self.gravity))
			time=time*2
			return time
		if self.find == 2:
                        initialvspeed = self.speed*math.sin(self.angle*math.pi/200)
			time=(initialvspeed)/math.ceil((self.gravity))
			time=time*2
			hspeed = self.speed*math.cos(self.angle*math.pi/200)
			distance = time*hspeed
			return distance
                        


        def check(self):
        	try:
        		int(self.txtbx.value)
        	except:
        		self.error = True
        		self.txtbx.value =""
        	if not self.error:

				if abs(int(self.txtbx.value)-self.answer())<1:
					self.txtbx.value =""
					return True
				else:
					self.txtbx.value =""
					return False
			

        def new(self):
                random.seed()
                self.speed = random.randint(1,100)
		self.angle = random.randint(20,80)
		self.gravity = random.randint(1,10)
		self.find = random.randint(1,2)
                
		

