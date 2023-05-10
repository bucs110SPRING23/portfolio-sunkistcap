import pygame

#pygame.init()
screen=pygame.display.set_mode()
screen.fill("red")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill("green")
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.rect(screen,"pink",[10,10,100,100])
pygame.display.flip()
pygame.time.wait(5000)
#[x,y,width,height]
dimensions=[300,300,250,250]
pygame.draw.rect(screen,"blue",dimensions)

pygame.display.flip()