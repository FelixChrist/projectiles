import pygame
import math

class projectile:


	def __init__(self,vspeed,hspeed,gravity):
		self.vspeed = vspeed*2
		self.initialvspeed= vspeed*2
		self.hspeed = hspeed*2
		self.gravity=((-gravity+200)/4)+1
		self.moving = True
	def launch(self,coords,screen,lastposx,lastposy):
		if self.moving:
			RED      = ( 255,   0,   0)
			BLACK    = (   0,   0,   0)
			x=coords[0]
			y=coords[1]
			x=x+self.hspeed
			y=y-self.vspeed
			self.vspeed=self.vspeed-self.gravity
			coords = [x,y]
			pygame.draw.circle(screen,RED,(coords[0],coords[1]),10,0)
		
		return coords
	def line(self,screen, lastposx,lastposy,coords):
		BLACK    = (   0,   0,   0)
		lastposx.append(coords[0])
		lastposy.append(coords[1])
		points=[[50,600]]
		for i in range(len(lastposx)):
			points.append([lastposx[i],lastposy[i]])

		pygame.draw.aalines(screen, BLACK,False, points,1)

	def calculateendtime(self,initialvspeed,gravity,hspeed):
		endtime=(initialvspeed)/math.ceil((gravity))
		endtime=endtime*2
		return endtime

	def calcualtedistance(self,hspeed,initialvspeed,gravity):
		time = self.calculateendtime(initialvspeed,gravity,hspeed)
		distance = time * hspeed
		return distance

	def calculatespeed(self,distance,time,gravity):
		hspeed=distance/self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)
		halftime=self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)/2
		if time<halftime:
			vspeed=math.ceil(self.initialvspeed-(gravity*time))
		else:
			vspeed=math.ceil(gravity*time)- self.initialvspeed
		speedsquared=math.pow(hspeed,2)+math.pow(vspeed,2)
		speed= math.sqrt(speedsquared)
		return speed

	def calculategravity(self,vspeed,time):
		halftime=time/2
		gravity=-vspeed/halftime
		return gravity

	def calculatetime(self,vspeed,hspeed,gravity,initialvspeed,delay):
		time=-((vspeed-initialvspeed)/gravity)
		pygame.time.delay(int(delay))
		return time










