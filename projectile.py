import pygame
import math
import numpy

class projectile:


	def __init__(self,vspeed,hspeed,gravity):
		self.vspeed = vspeed
		self.initialvspeed= vspeed
		self.hspeed = hspeed
		self.gravity=gravity
		self.moving = True
		self.equations = [[]]
		self.oldx =[0]
		self.t=0
		self.time = 0
		self.height=0
		self.back = False
		
	def launch(self,coords,screen,lastposx,lastposy,pause):
		if self.moving:
			self.back = False
			RED      = ( 255,   0,   0)
			BLACK    = (   0,   0,   0)
			pos=self.equation()
			#self.t = 0
			x=coords[0]
			y=coords[1]
			pygame.draw.circle(screen,RED,(x+50,int(((-(pos[0]*math.pow(x,2)))-(pos[1])*x+(pos[2])))+600),10,0)
			
			if not pause:
				step = int(self.calculateenddistance(self.hspeed,self.initialvspeed,self.gravity)/self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed))
				x=x+step
				step = int(self.initialvspeed/(self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)/2))
				self.vspeed=self.vspeed-step
				self.time = self.time+1
				self.calculateheight()
			y=((-int(pos[0])*math.pow(x,2))-int(pos[1])*x+int(pos[2]))
			
			coords = [x,y]	
		return coords

	def launchback(self,coords,screen,lastposx,lastposy,pause):
		if self.moving:
			self.back = True
			RED      = ( 255,   0,   0)
			BLACK    = (   0,   0,   0)
			pos=self.equation()
			#self.t = 0
			x=coords[0]
			y=coords[1]
			pygame.draw.circle(screen,RED,(x+50,int(((-pos[0]*math.pow(x,2))-pos[1]*x+pos[2]))+600),10,0)

			if not pause:
				step = int(self.calculateenddistance(self.hspeed,self.initialvspeed,self.gravity)/self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed))
				x=x-step
				step = int(self.initialvspeed/(self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)/2))
				self.vspeed=self.vspeed+step
				self.time = self.time-1
				self.calculateheight()
			y=((-pos[0]*math.pow(x,2))-pos[1]*x+pos[2])
			
			coords = [x,y]	
		return coords


	
	def line(self,screen, lastposx,lastposy,coords,):
		BLACK    = (   0,   0,   0)
		lastposx.append(coords[0])
		lastposy.append(coords[1])
		points=[[50,600]]
		lines = self.equation()
		

		for i in range(0, coords[0]+1):
			x=i+50
			y1 = int((((((-(lines[0])*math.pow(i,2))-((lines[1]))*i)-(lines[2]))+600)))
			y2 = int(((((-(lines[0])*math.pow(i-1,2))-((lines[1]))*(i-1)-(lines[2]))+600)))
			#pygame.draw.circle(screen, BLACK, [x,y1], 1,)
			pygame.draw.aaline(screen, BLACK, (x-1,y2),(x,y1), 2)
			

		

	def calculateendtime(self,initialvspeed,gravity,hspeed):
		endtime=(self.initialvspeed)/math.ceil((self.gravity))
		endtime=endtime*2
		return endtime 

	def calculateenddistance(self,hspeed,initialvspeed,gravity):
		time = self.calculateendtime(initialvspeed,gravity,hspeed)
		distance = time * self.hspeed
		return distance

	def calculatevdistance(self,hspeed,initialvspeed,graviy):
		time =  self.calculateendtime(initialvspeed,self.gravity,hspeed)
		halftime = time/2
		vdistance = initialvspeed*halftime- (1/2)*self.gravity*math.pow(halftime,2) 
		return vdistance


	def calculatespeed(self,distance,time,gravity):
		halftime=self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)/2

		if time<halftime:
			vspeed=(math.ceil(self.initialvspeed-(self.gravity*self.time)))
		else:
			vspeed=(math.ceil(self.gravity*self.time)- self.initialvspeed)/2
		speedsquared=math.pow(self.hspeed,2)+math.pow(self.vspeed,2)
		speed= math.sqrt(speedsquared)
		return speed


	def calculatetime(self,vspeed,hspeed,gravity,initialvspeed,delay,pause):
		return self.time

	def calculatehdistance(self,hspeed,time):
		distance = hspeed*time
		return distance

	def calculateheight(self):
		maxheight = self.calculatevdistance(self.hspeed,self.initialvspeed,self.gravity)
		halftime=self.calculateendtime(self.initialvspeed,self.gravity,self.hspeed)/2
		step = maxheight/halftime
		if self.time<halftime:
			if self.back:
				self.height=self.height-step
			else:
				self.height=self.height+step
		else:
			if self.back:
				self.height=self.height+step
			else:
				self.height=self.height-step

		if self.height < 0:
			self.height = 0
		
		

	def equation(self):
		hdistance = self.calculateenddistance(self.hspeed,self.initialvspeed,self.gravity)
		vdistance = self.calculatevdistance(self.hspeed,self.initialvspeed,self.gravity) /2
		first = [0,0]
		second = [(hdistance/2),vdistance]
		third = [(hdistance),0]
		a = [[math.pow(first[0],2), first[0],1], [math.pow(second[0],2), second[0],1], [math.pow(third[0],2),third[0],1]]
		b = [[first[1]],[second[1]],[third[1]]]
		c = self.invert(a)
		d = self.dotproduct(c,b)
		return d

	def dotproduct(self,a,b):
		c=[0,0,0]
		for j in range(len(c)):
			c[j] = sum((a[j][i])*(b[i][0]) for i in range(len(a[j])))
		return c

	def invert(self,a):
		b = [[0,0,0],[0,0,0],[0,0,0]]
		if self.det3x3(a) != 0:
			overdet = 1/self.det3x3(a)
			b = self.transpose(b)
			b[0][0]=overdet*self.det2x2([[a[1][1],a[1][2]],[a[2][1],a[2][2]]])
			b[0][1]=overdet*self.det2x2([[a[0][2],a[0][1]],[a[2][2],a[2][1]]])
			b[0][2]=overdet*self.det2x2([[a[0][1],a[0][2]],[a[1][1],a[1][2]]])
			b[1][0]=overdet*self.det2x2([[a[1][2],a[1][0]],[a[2][2],a[2][0]]])
			b[1][1]=overdet*self.det2x2([[a[0][0],a[0][2]],[a[2][0],a[2][2]]])
			b[1][2]=overdet*self.det2x2([[a[0][2],a[0][0]],[a[1][2],a[1][0]]])
			b[2][0]=overdet*self.det2x2([[a[1][0],a[1][1]],[a[2][0],a[2][1]]])
			b[2][1]=overdet*self.det2x2([[a[0][1],a[0][0]],[a[2][1],a[2][0]]])
			b[2][2]=overdet*self.det2x2([[a[0][0],a[0][1]],[a[1][0],a[1][1]]])
		elif self.calculateenddistance(self.hspeed,self.initialvspeed,self.gravity) < 10:
			self.hspeed = self.hspeed-1
			b = self.equation()
			
		elif self.calculatevdistance(self.hspeed,self.initialvspeed,self.gravity) /2 < 10:
			self.vspeed=self.vspeed-1
			b = self.equation()
			

		return b

	def det2x2(self,a):
		return ((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))

	def det3x3(self,a):
		return (a[0][0]*(((a[1][1])*a[2][2])-(a[1][2]*a[2][1]))-(a[0][1]*((a[1][0]*a[2][2])-(a[1][2]*a[2][0])))+(a[0][2]*((a[1][0]*a[2][1])-(a[1][1]*a[2][0]))))

	def transpose(self,a):
		for i in range(0, len(a)-2):
			for j in range(i+1, len(a)-1):
				temp = a[i][j]
				a[i][j] = a[j][i]
				a[j][i] = temp
		return a 






       
                        
                        
                        
                












