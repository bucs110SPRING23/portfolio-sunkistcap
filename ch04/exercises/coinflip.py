#import modules
import turtle
import random
#initalization
player=turtle.Turtle()
screen=turtle.Screen()
player.shape("turtle")
player.color("purple")
player.penup()
player.goto(500,500)
player.pendown()

while (player.isvisible()==True):
    coin=random.randint(1,100)
    if (coin>=50):
        player.left(90)
        player.fd(50)
    if(coin<=50):
        player.right(90)
        player.fd(50)