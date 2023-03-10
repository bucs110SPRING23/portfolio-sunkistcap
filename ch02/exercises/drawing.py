#import modules
import turtle
#user input
sides= int(input("please enter a number of sides: "))
length= int(input("please enter the length of each side: "))
#initalize
window=turtle.Screen()
aTurtle=turtle.Turtle()
aTurtle.shape("turtle")
aTurtle.color("blue")
iAngle=int(360/sides)
#screen
aTurtle.goto(0,0)
for i in range(sides):
    aTurtle.fd(length)
    aTurtle.left(iAngle)
#exit
window.exitonclick()