import pygame
import projectile
import slider
import line
import question
import math


def calculatespeed(speed, angle):
    speed = (speed)
    angle = (angle)*(10*math.pi/2000)
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
    GREEN    = (   0, 255,   0)
    BLUE     = (   0, 100, 255)
    img_launch1 = pygame.image.load("Launch_1.png")
    img_launch2 = pygame.image.load("Launch_2.png")
    imagerect = img_launch1.get_rect(center=[825,175])
    img_pause = pygame.image.load("Pause.png")
    img_play = pygame.image.load("Play.png")
    imagerect2 = img_pause.get_rect(center=[825,75])
    img_check1= pygame.image.load("Check1.png")
    img_check2= pygame.image.load("Check2.png")
    imagerect3 = img_check1.get_rect(center=[600,125])
    img_forward1 =pygame.image.load("Forward1.png")
    img_forward2 =pygame.image.load("Forward2.png")
    imagerect4 = img_check1.get_rect(center=[925,75])
    img_back1 =pygame.image.load("Back1.png")
    img_back2 =pygame.image.load("Back2.png")
    imagerect5 = img_check1.get_rect(center=[775,75])
    img_cannon = pygame.image.load("Cannon.png")
    img_origonal = pygame.image.load("Cannon.png")
    imagerect6 = img_cannon.get_rect(center=[50,600])
    img_wheel = pygame.image.load("Wheel.png")
    imagerect7 = img_wheel.get_rect(center=[50,600])
    img_grass = pygame.image.load("Grass.png")
    imagerect8 = img_grass.get_rect(center=[850,700])
    img_uppergrass = pygame.image.load("UpperGrass.png")
    imagerect9 = img_grass.get_rect(center=[850,695])
    img_sky =pygame.image.load("Sky.png")
    imagerect10 = img_sky.get_rect(center=[850,300])
    img_box =pygame.image.load("Box.png")
    imagerect11 = img_box.get_rect(center=[355,105])
    img_start1 =pygame.image.load("Start1.png")
    img_start2 =pygame.image.load("Start2.png")
    imagerect12 = img_start1.get_rect(center=[850,275])
    img_quit1 =pygame.image.load("Quit1.png")
    img_quit2 =pygame.image.load("Quit2.png")
    imagerect13 = img_quit1.get_rect(center=[850,475])
    img_menu = pygame.image.load("Menu.png")
    imagerect14 = img_menu.get_rect(center=[850,400])
    img_menu1 = pygame.image.load("Menu1.png")
    img_menu2 = pygame.image.load("Menu2.png")
    imagerect15 = img_menu1.get_rect(center=[1645,30])
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
    timedelay=slider.slider("animation",[1340,200],[1340,200])
    quest = question.question()
    coords= [50,600]
    coords2= [50,600]
    lastposx = [50]
    lastposy = [600]
    speeds=calculatespeed(speed.pos2[1],angle.pos2[1])
    coords1= [50,600]
    projectile1=projectile.projectile(speeds[0],speeds[1],gravity.pos2[1])
    launched=False
    pause = False
    score = 0
    tries = 0
    back = False
    equationsa = [1]
    equationsb = [1]
    equationsc = [1]
    equations = [1,1,1]
    oldx= []
    speed.moving = False
    angle.moving = False
    gravity.moving = False
    timedelay.moving=False
    menu = True
    correct = False
    incorrect = False
    while not done:
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                speed.moving = True
                angle.moving = True
                gravity.moving=True
                timedelay.moving=True
                mousex=pygame.mouse.get_pos()[0]
                mousey=pygame.mouse.get_pos()[1]
                if (mousey>150 and mousey<=200) and (mousex>=750 and mousex<=850):
                    if launch == False:
                        speeds=calculatespeed(speed.value,angle.value)
                        projectile1=projectile.projectile(speeds[0],speeds[1],gravity.value)
                        line1=line.line()
                        coords= [50,600]
                        lastposx = [50]
                        lastposy = [600]
                        launched = True
                    launch= True
                if (mousey>50 and mousey<=100) and (mousex>=800 and mousex<=850):
                    if pause:
                        pause = False
                    else:
                        pause = True
                if (mousey>100 and mousey<=150) and (mousex>=550 and mousex<=650):
                    quest.error=False
                    if quest.check():
                        score = score + 1
                        quest.new()
                        correct = True
                    elif not quest.error:
                        incorrect = True
                    if not quest.error:
                        tries = tries + 1
                if (mousey>50 and mousey<=100) and (mousex>=875 and mousex<=925):
                    if pause and launch:
                        pause=False
                        projectile1.moving = True
                        projectile1.line(screen, lastposx,lastposy,coords)
                        coords=projectile1.launch(coords,screen,lastposx,lastposy,pause)
                        pause=True
                if (mousey>50 and mousey<=100) and (mousex>=725 and mousex<=775):
                    if projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,timedelay.value,pause) > 0:
                        back = True
                if (mousey>200 and mousey<=350) and (mousex>=550 and mousex<=1150):
                    menu = False
                if (mousey>400 and mousey<=550) and (mousex>=550 and mousex<=1150) and menu:
                    done = True
                if (mousey>5 and mousey<=55) and (mousex>=1595 and mousex<=1695):
                    menu = True
                

            if event.type == pygame.MOUSEBUTTONUP:
                speed.moving = False
                angle.moving = False
                gravity.moving = False
                timedelay.moving=False
            
        mousex=pygame.mouse.get_pos()[0]
        mousey=pygame.mouse.get_pos()[1]
        speed.getvalue(-speed.pos2[1]+201)
        angle.getvalue(-angle.pos2[1]+201)
        gravity.getvalue(int((-gravity.pos2[1]+201)/5.1)+1)
        timedelay.getvalue(-timedelay.pos2[1]+201)
        screen.fill(BLACK)
        if angle.value>99:
            angle.value = 99
        

        screen.blit(img_grass,imagerect8)
        screen.blit(img_uppergrass,imagerect9)
        screen.blit(img_sky,imagerect10)
        screen.blit(img_box,imagerect11)
        quest.draw(screen)  
        speed.draw(screen)
        angle.draw(screen)
        gravity.draw(screen)
        timedelay.draw(screen)
        
        if (mousey>50 and mousey<=100) and (mousex>=875 and mousex<=925):
            screen.blit(img_forward2, imagerect4)
        else:
            screen.blit(img_forward1, imagerect4)
        if (mousey>50 and mousey<=100) and (mousex>=725 and mousex<=775):
            screen.blit(img_back2, imagerect5)
        else:
            screen.blit(img_back1, imagerect5)
        if pause:
            screen.blit(img_play,imagerect2)
        else:
            screen.blit(img_pause,imagerect2) 
        if (mousey>150 and mousey<=200) and (mousex>=775 and mousex<=875):
            screen.blit(img_launch2,imagerect)
        else:
            screen.blit(img_launch1,imagerect)
        if (mousey>100 and mousey<=150) and (mousex>=550 and mousex<=650):
            screen.blit(img_check1,imagerect3)
        else:
            screen.blit(img_check2,imagerect3)
        if (mousey>5 and mousey<=55) and (mousex>=1595 and mousex<=1695):
            screen.blit(img_menu2,imagerect15) 
        else:
            screen.blit(img_menu1,imagerect15)                
        if back:
            pause=False
            projectile1.moving = True
            projectile1.line(screen, lastposx,lastposy,coords)
            coords=projectile1.launchback(coords,screen,lastposx,lastposy,pause)
            back = False
            launch = True
            pause=True
            
        if launch:
            
            
            if coords[0] < projectile1.calculateenddistance(projectile1.hspeed,projectile1.initialvspeed,projectile1.gravity):
                projectile1.moving = True
                projectile1.line(screen, lastposx,lastposy,coords)
                coords=projectile1.launch(coords,screen,lastposx,lastposy,pause)
                
                
            else:   
                projectile1.moving = False
                launch = False
                
        screen.blit(img_grass,imagerect8)
        screen.blit(img_uppergrass,imagerect9)
        
        
        if not projectile1.moving and not back:
            projectile1.line(screen, lastposx,lastposy,coords)
            screen.blit(img_grass,imagerect8)
            screen.blit(img_uppergrass,imagerect9)
            pygame.draw.circle(screen,RED,(int(projectile1.calculateenddistance(projectile1.hspeed,projectile1.initialvspeed,projectile1.gravity)+50),600),10,0)
            


        

        words= "Time: "+str(projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,timedelay.value,pause))
        if launch and not pause:
            pygame.time.delay(int(timedelay.value*2))
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 55
        screen.blit(text, textpos)
        words= "Horizontal Distance: "+str(math.ceil(projectile1.calculatehdistance(projectile1.hspeed,projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,timedelay.value,pause))))
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 75
        screen.blit(text, textpos)
        words= "Speed: "+str(math.ceil(projectile1.calculatespeed(projectile1.calculateenddistance(projectile1.hspeed,projectile1.initialvspeed,projectile1.gravity),projectile1.calculatetime(projectile1.vspeed,projectile1.hspeed,projectile1.gravity,projectile1.initialvspeed,0,pause),projectile1.gravity,)))
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 95
        screen.blit(text, textpos)
        words= "Height: "+str(projectile1.height)
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 115
        screen.blit(text, textpos)
        words= "Vertical velocity: "+str(projectile1.vspeed)
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 135
        screen.blit(text, textpos)
        words= "Horizontal velocity: "+str(projectile1.hspeed)
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 1200
        textpos.centery = 155
        screen.blit(text, textpos)
        if correct and not quest.error:
            words= "Correct!"
            font = pygame.font.Font(None, 26)
            text = font.render(words, 1, GREEN)
            textpos = text.get_rect()
            textpos.centerx = 400
            textpos.centery = 55
            screen.blit(text, textpos)
        elif incorrect and not quest.error:
            words= "Incorrect!"
            font = pygame.font.Font(None, 26)
            text = font.render(words, 1, RED)
            textpos = text.get_rect()
            textpos.centerx = 400
            textpos.centery = 55
            screen.blit(text, textpos)
        if quest.error:
            words= "Enter a number only!"
            font = pygame.font.Font(None, 26)
            text = font.render(words, 1, RED)
            textpos = text.get_rect()
            textpos.centerx = 400
            textpos.centery = 65
            screen.blit(text, textpos)
        
        words= str(score)+"/"+str(tries)
        font = pygame.font.Font(None, 26)
        text = font.render(words, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = 600
        textpos.centery = 75
        screen.blit(text, textpos)
        img_cannon=pygame.transform.rotate(img_origonal,(angle.value)*0.9)
        imagerect6 = img_cannon.get_rect(center=[50,600])
        screen.blit(img_cannon,imagerect6)
        screen.blit(img_wheel,imagerect7)

        if menu:
            screen.blit(img_menu,imagerect14)
            if (mousey>200 and mousey<=350) and (mousex>=550 and mousex<=1150):
                screen.blit(img_start2,imagerect12)
            else:
                screen.blit(img_start1,imagerect12)
            if (mousey>400 and mousey<=550) and (mousex>=550 and mousex<=1150):
                screen.blit(img_quit2,imagerect13)
            else:
                screen.blit(img_quit1,imagerect13)
            
        
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()
pygame.quit





















