#import module
import pygame
#intialize
pygame.init()
screen=pygame.display.set_mode()
screen.fill("brown")
#create snowman
dimensions=[750,750]
pygame.draw.circle(screen,"white",dimensions,200)
dimensions=[750,500]
pygame.draw.circle(screen,"white",dimensions,150)
dimensions=[750,280]
pygame.draw.circle(screen,"white",dimensions,100)
pygame.display.flip()
pygame.time.wait(1000)