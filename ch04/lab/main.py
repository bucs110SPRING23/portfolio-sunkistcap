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
tScreen=pygame.display.set_mode()
size= screen.get_size()
width=size[0]/2
height=size[1]/2
radius= min(width,height)
screen.fill("gray")
#circle and lines (lab 3)``
def boardgame():
    pygame.draw.circle(screen,"burlywood3",[(width),(height)],radius)
    pygame.draw.circle(screen,"black",[(width),(height)],radius,5)
    pygame.draw.line(screen,"black",[(width+height),(height)],[width-height,height],5)
    pygame.draw.line(screen,"black",[width,height//radius],[height,width*radius],5)
    pygame.display.flip()
    pygame.time.wait(1500)
#initalize event
event_exit = False
user_bet = None
#Part B 
boardgame()
option_p1 = pygame.draw.rect(tScreen,"red",((width*1.2),(height/1.2),(radius/2),(radius/4)))
option_p2 = pygame.draw.rect(tScreen,"blue",((width/2),(height/1.2),(radius/2),(radius/4)))
font=pygame.font.Font(None,80)
text=font.render("Player 1",True,"black")
tScreen.blit(text,((width*1.2),(height/1.2)))
text=font.render("Player 2",True,"black")
tScreen.blit(text,((width/2),(height/1.2)))

pygame.display.flip()
while not event_exit:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if option_p1.collidepoint(mouse_pos):
                user_bet = option_p1
                event_exit = True
            elif option_p2.collidepoint(mouse_pos):
                user_bet = option_p2
                event_exit = True
boardgame()
#for loop of dart throws
text_rect = text.get_rect(topleft=(0,height//radius))
font=pygame.font.Font(None,64)
for i in range(10):
    text=font.render(f"Round {i}",True,"white")
    pygame.draw.rect(screen,"gray",text_rect)
    screen.blit(text,(0,(height//radius)))
    pygame.display.flip()
    pygame.time.wait(1000)
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
        distance= math.hypot((width-dTX), (height-dTY)) 
        inCircle = (distance <= radius) #screen width
        #if statment for dart color
        #red = miss
        #green = hit
        if inCircle:
            color=[r,g,b]
            if (j==0):
                p1+=1
            else:
                p2+=1
        else:
            color=[wr,wg,wb]
        pygame.draw.circle(screen,color,[(dTX),(dTY)],9)
        pygame.display.flip()
#print winner
if(p1>p2):
    text=font.render("player 1 wins!",True, "red")
    if user_bet == option_p1:
        bet=font.render("you guessed correctly!",True,"Green")
    else:
        bet=font.render("you guessed wrong :(",True,"Red")
elif(p1<p2):
    text=font.render("player 2 wins!",True,"blue")
    if user_bet == option_p2:
        bet=font.render("you guessed correctly!",True,"Green")
    else:
        bet=font.render("you guessed wrong :(",True,"Red")
else:
    text=font.render("It's a tie!",True,"black")
    bet=font.render("close call!",True,"Red")
screen.blit(text,((width/1.1),(height/4)))
screen.blit(bet,((width/1.1),(height/3)))
pygame.display.flip()
pygame.time.wait(5000)
#quit
pygame.quit() 