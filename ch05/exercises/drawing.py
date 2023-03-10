#import modules
import math
import turtle

def draw_eq_shape(tShape,nSides,sLen):
    iAngle=int(360/nSides)
    window=turtle.Screen()
    for i in range(nSides):
        tShape.fd(sLen)
        tShape.right(iAngle)
    #quit game
    window.exitonclick()

tShape=turtle.Turtle()
tShape.shape("turtle")
tShape.color("red")
nSides= int(input("please enter a number of sides: "))
sLen= int(input("please enter the length of each side: "))
draw_eq_shape(tShape,nSides,sLen)