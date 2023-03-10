#import modules
import pygame
import random
import math
#Part A
#initalize scores
p1=0
p2=0
#initalize screen (lab 3)
pygame.init()
screen=pygame.display.set_mode()
size= screen.get_size()
width=size[0]/2
height=size[1]/2
radius= min(width,height)
screen.fill("gray")
#circle and lines (lab 3)
pygame.draw.circle(screen,"burlywood3",[(width),(height)],radius)
pygame.draw.circle(screen,"black",[(width),(height)],radius,5)
pygame.draw.line(screen,"black",[(width+height),(height)],[width-height,height],5)
pygame.draw.line(screen,"black",[width,height//radius],[height,width*radius],5)
pygame.display.flip()
pygame.time.wait(1500)
#Part B 
#for loop of dart throws
for i in range(10):
    #font=pygame.font.Font(None,64)
    #text=font.render(f"Round {i}",True,"white")
    #screen.blit(text,(0,height//radius))
    #first for loop P1 , second for loop P2
    for j in range(2):
        #circle dart color 
        r=(119/(j+1))
        g=(247/(j+1))
        b=(147/(j+1))
        #OOB dart color
        wr=(200/(j+1))
        wg=0
        wb=0
        #dart throw location
        dTX=random.randint(0,width*2)
        dTY=random.randint(0,height*2)
        distance= math.hypot((width-dTX), (height-dTY)) #the distance formula
        inCircle = (distance <= radius) #screen width
        #if statment for dart color
        #red = miss
        #green = hit
        if (inCircle==True):
            color=[r,g,b]
            if (j==0):
                p1+=1
            else:
                p2+=1
        else:
            color=[wr,wg,wb]
        pygame.draw.circle(screen,color,[(dTX),(dTY)],9)
        pygame.display.flip()
        pygame.time.wait(1500)
#print winner
font=pygame.font.Font(None,64)
if(p1>p2):
    text=font.render("player 1 wins!",True,"red")
elif(p1<p2):
    text=font.render("player 2 wins!",True,"blue")
else:
    text=font.render("It's a tie!",True,"black")
screen.blit(text,((width-radius),height))
pygame.display.flip()
pygame.time.wait(2000)
#quit
pygame.quit()