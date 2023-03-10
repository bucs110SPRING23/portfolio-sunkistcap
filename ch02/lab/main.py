#modules
import random
import math
import turtle
import pygame
#Part A setup
turtle1= turtle.Turtle()
turtle1.shape("turtle")
turtle2= turtle.Turtle()
turtle2.shape("turtle")
screen=turtle.Screen()
turtle1.up()
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
turtle1.pendown()
turtle2.pendown()

#Race 1
turtle1.color("red")
turtle2.color("blue")
turtle1.forward(random.randint(1,100))
turtle2.forward(random.randint(1,100))
turtle1.up()
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
#Race 2
turtle1.color("purple")
turtle2.color("green")
turtle1.pendown()
turtle2.pendown()
for i in range(10):
    turtle2.fd(random.randrange(1,10))
    turtle1.fd(random.randrange(1,10))
turtle1.up()
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)
#exit
screen.exitonclick()

#Part B
#initialize
pygame.init()
window = pygame.display.set_mode()
xpos=750
ypos=500
num_sides=[3,4,6,20,100,360]
side_length=250
#creating shapes
for i in range(6):
    points=[]
    n = num_sides[i]
    for j in range(n):
        iAngle=360/n
        radians= math.radians(iAngle*j+30)
        x= xpos+side_length*math.cos(radians)
        y= ypos+side_length*math.sin(radians)
        points.append([x, y])
    #draw and reset
    pygame.draw.polygon(window,"red",points)
    pygame.display.flip()
    pygame.time.wait(500)
    window.fill((0,0,0))
    pygame.display.flip()
#exit pygame
pygame.quit()



# we had talked in class on 2/27 about this assignment coming in late
# I'm just writing this as you had told me to remind you.