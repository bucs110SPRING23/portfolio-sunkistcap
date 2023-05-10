#import modules
import pygame
import random
import math
#Part A
#initalize screen
pygame.init()
screen=pygame.display.set_mode()
size= screen.get_size()
width=size[0]/2
height=size[1]/2
radius= min(width,height)
screen.fill("powderblue")
#circle and lines
pygame.draw.circle(screen,"purple",[(width),(height)],radius)
pygame.draw.circle(screen,"black",[(width),(height)],radius,5)
pygame.draw.line(screen,"black",[(width+height),(height)],[width-height,height],5)
pygame.draw.line(screen,"black",[width,height//radius],[height,width*radius],5)
pygame.display.flip()
pygame.time.wait(1500)
#Part B 
#for loop of dart throws
for i in range(10):
    #dart throw location
    dTX=random.randint(0,width*2)
    dTY=random.randint(0,height*2)
    distance= math.hypot((width-dTX), (height-dTY)) #the distance formula
    inCircle = (distance <= radius) #screen width
    #if statment for dart color
    #red = miss
    #green = hit
    if (inCircle==True):
        color="green"
    else:
        color="red"
    pygame.draw.circle(screen,color,[(dTX),(dTY)],5)
    pygame.display.flip()
    pygame.time.wait(1500)
pygame.quit()