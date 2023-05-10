#import modules
import turtle
import random
#initalization
ranTurt=turtle.Turtle()
screen=turtle.Screen()
ranTurt.shape("turtle")
ranTurt.color("purple")
size=(turtle.screensize())
print(size)
height=(size[0])
width=(size[1])
nHeight=(height-(height*2))
nWidth=(width-(width*2))
#while loop
while (ranTurt.isvisible()==True):
    coin=random.randint(1,100)
    #heads
    if (coin>=50):
        ranTurt.left(90)
        ranTurt.fd(50)
    #tails
    elif(coin<=50):
        ranTurt.right(90)
        ranTurt.fd(50)
    #turtle location check
    turtCheck=(ranTurt.pos())
    print(turtCheck)
    x=(int(turtCheck[0]))
    y=(int(turtCheck[1]))
    if(x>=width):
        ranTurt.ht()
    elif(x<=nWidth):
        ranTurt.ht()
    elif(y>=height ):
        ranTurt.ht() 
    elif(y<=nHeight):
        ranTurt.ht()
#exit
turtle.bye()