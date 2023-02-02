#modules
import random
import math
import turtle
#Part A
turtle1= turtle.Turtle()
turtle1.shape("turtle")
turtle2= turtle.Turtle()
turtle2.shape("turtle")
screen=turtle.Screen()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)

#Race 1
ranMove=random.randint(1,100)
turtle1.forward(ranMove)
ranMove=random.randint(1,100)
turtle2.forward(ranMove)
turtle1.goto(-100.20)
turtle2.goto(-100,-20)
#Race 2


screen.exitonclick()
#Part B
