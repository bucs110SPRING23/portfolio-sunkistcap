#import modules
import turtle
#initalizing screen and turtle
window=turtle.Screen()
eTurtle=turtle.Turtle()
#turtle shape & color
eTurtle.shape("turtle")
eTurtle.color("purple")
#first square
eTurtle.goto(0,0)
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
#second square
eTurtle.up()
eTurtle.goto(100,20)
eTurtle.color("red")
eTurtle.down()
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
eTurtle.left(90)
eTurtle.fd(50)
#exit program
window.exitonclick()