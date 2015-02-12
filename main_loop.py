import pygame
import projectile
import slider
import line
import question
import math

def calculatespeed(speed, angle):
	speed = (-speed+200)/2
	angle = (-angle+ 200)*(10*math.pi/2000)
	speeds=[0,0]
	speeds[0]=int(math.floor(speed*math.sin(angle)))
	speeds[1]=int(math.floor(speed*math.cos(angle)))
	return speeds

def main():
	pygame.init()
	pygame.font.init()
	RED      = ( 255,   0,   0)
	BLACK    = (   0,   0,   0)
	WHITE    = ( 255, 255, 255)
	GREEN	 = (   0, 255,   0)
	BLUE	 = (   0, 100, 255)
	clock=pygame.time.Clock()
	done=False
	
	size=(1700,800)
	screen=pygame.display.set_mode(size)
	pygame.display.set_caption("Projectiles")
	launch=False
	move=False
	speed=slider.slider("speed",[1500,200],[1500,150])
	angle=slider.slider("angle",[1450,200],[1450,150])
	gravity=slider.slider("gravity",[1400,200],[1400,150])
	timedelay=slider.slider("time delay",[1350,200],[1350,150])
	quest = question.question()
	coords= [50,600]
	coords2= [50,600]
	lastposx = [50]
	lastposy = [600]
	speeds=calculatespeed(speed.pos2[1],angle.pos2[1])
	coords1= [50,600]
	projectile1=projectile.projectile(speeds[0],speeds[1],gravity.pos2[1])
	while not done:
		       
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			if event.type == pygame.KEYDOWN:
				if launch == False:
					speeds=calculatespeed(speed.pos2[1],angle.pos2[1])
					projectile1=projectile.projectile(speeds[0],speeds[1],gravity.pos2[1])
					line1=line.line()
					coords= [50,600]
					lastposx = [50]
					lastposy = [600]
				launch= True
			if event.type == pygame.MOUSEBUTTONDOWN:
				speed.moving = True
				angle.moving = True
				gravity.moving=True
				timedelay.moving=True
			if event.type == pygame.MOUSEBUTTONUP:
				speed.moving = False
				angle.moving = False
				gravity.moving = False
				timedelay.moving=False

		speed.getvalue(-speed.pos2[1]+201)
		angle.getvalue(-angle.pos2[1]+201)
		gravity.getvalue(math.ceil((-gravity.pos2[1]+201)/5.1))
		timedelay.getvalue(-timedelay.pos2[1]+201)
		screen.fill(BLACK)

		pygame.draw.rect(screen,GREEN,[0,600,1700,200],0)
		pygame.draw.rect(screen,BLUE,[0,0,1700,600],0)
		pygame.draw.rect(screen,WHITE,[10,10,700,200])
		quest.draw(screen)	
		speed.draw(screen)
		angle.draw(screen)
		gravity.draw(screen)
		timedelay.draw(screen)
		
		if launch:
			
			
			if coords[1] <601:
				projectile1.moving = True

				coords=projectile1.launch(coords,screen,lastposx,lastposy)
				projectile1.line(screen, lastposx,lastposy,coords)
				
			else:	
				projectile1.moving = False
				launch = False

		if not projectile1.moving:
			pygame.draw.circle(screen,RED,(coords[0],coords[1]),10,0)
		words= "Time: "+str(projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,timedelay.value))
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 1300
		textpos.centery = 100
		screen.blit(text, textpos)
		words= "Distance: "+str(math.ceil(projectile1.calcualtedistance(projectile1.hspeed,projectile1.initialvspeed,projectile1.gravity)))
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 1200
		textpos.centery = 100
		screen.blit(text, textpos)
		words= "Speed: "+str(math.ceil(projectile1.calculatespeed(projectile1.calcualtedistance(projectile1.hspeed,projectile1.initialvspeed,projectile1.gravity),projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,0),projectile1.gravity,)))
		font = pygame.font.Font(None, 26)
		text = font.render(words, 1, BLACK)
		textpos = text.get_rect()
		textpos.centerx = 1000
		textpos.centery = 100
		screen.blit(text, textpos)
		pygame.display.flip()	
		clock.tick(60)
		
pygame.quit

if __name__ == "__main__":
	for i in xrange(10000000):
		print("HI FELIX")
	main()



















