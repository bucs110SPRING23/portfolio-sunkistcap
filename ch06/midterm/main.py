#import modules
import turtle
import random
# constants
BLANK = "#000000"
VISOR_GLASS = "#aedbfc"
CREWMATES = ["#aa00ff","#00ff04","#fffb00","#ff0033","#ffffff"]
NUMBER_OF_CREWMATES = 5
NUMBER_OF_STARS = 100
STAR_SIZE = 2
STAR_COLOR = "white"
TURN_ANGLE_1 = 90
TURN_ANGLE_2 = 180
TURN_ANGLE_3 = 100
TURN_ANGLE_4 = 25
TURN_ANGLE_5 = 114
TURN_ANGLE_6 = 15
TURN_ANGLE_7 = 45
TURN_ANGLE_8 = 70
TURN_ANGLE_9 = 55
TURN_ANGLE_10 = 155
TURN_ANGLE_11 = 30
TURN_ANGLE_12 = 105
MOVE_DISTANCE_1 = 25
MOVE_DISTANCE_2 = 100
MOVE_DISTANCE_3 = 50
MOVE_DISTANCE_4 = 30
MOVE_DISTANCE_6 = 45
MOVE_DISTANCE_7 = 40
MOVE_DISTANCE_8 = 65
MOVE_DISTANCE_9 = 8
MOVE_DISTANCE_10 = 20
MOVE_DISTANCE_11 = 2
MOVE_DISTANCE_12 = 55
MOVE_DISTANCE_13 = 9
MOVE_DISTANCE_14 = 10
MOVE_DISTANCE_15 = 5
MOVE_DISTANCE_16 = 36
MOVE_DISTANCE_17 = 150
MOVE_DISTANCE_18 = 75
MOVE_DISTANCE_19 = 85
MOVE_DISTANCE_20 = 155
MOVE_DISTANCE_21 = 70
CIRCLE_RADIUS_1 = 20
HEAD_RADIUS = 50
CIRCLE_ANGLE_1 = -180
WAIST_RADIUS = 17.5
HEADING_EAST = 0
HEADING_NORTH = 90
HEADING_SOUTH = 270
HEADING_WEST = 180
HEADING_NORTHEAST = 75
HEADING_SOUTHEAST_1 = 285
HEADING_SOUTHEAST_2 = 280
BACKPACK_RADIUS = 150
BACKPACK_ANGLE = -30
IMPOSTER_RADIUS_1 = -15
IMPOSTER_RADIUS_2 = 15
IMPOSTER_RADIUS_3= -5
IMPOSTER_ANGLE_1 = 80
IMPOSTER_ANGLE_2 = -80
LETTER_O = 70
LETTER_G_X_AXIS = 200
LETTER_U_X_AXIS = 425
G_CURVE_RADIUS = -60
G_CURVE_ANGLE = 270
LETTER_U_RADIUS = 60
LETTER_U_ANGLE = -180
LETTER_S_RADIUS_1 = 30
LETTER_S_RADIUS_2 = -30
LETTER_S_ANGLE = 180
def logo(tDraw,window):
    '''
    draws the among us logo at the top of the screen
    Args: 
        tDraw (turtle): used to draw the logo
        window (turtle):obtains the floor for the logo writing
    '''
    #logo floor set up
    tDraw.penup()
    logoFloorX=(-window.window_width()*0.15)
    logoFloorY=(window.window_height() * 0.26)
    tDraw.goto(logoFloorX,logoFloorY)
    tDraw.pendown()
    #Logo drawing begin
    # letter M
    tDraw.setheading(HEADING_NORTHEAST)
    tDraw.fd(MOVE_DISTANCE_17)
    tDraw.setheading(HEADING_SOUTHEAST_1)
    tDraw.fd(MOVE_DISTANCE_18)
    tDraw.setheading(HEADING_NORTHEAST)
    tDraw.fd(MOVE_DISTANCE_18)
    tDraw.setheading(HEADING_SOUTHEAST_1)
    tDraw.fd(MOVE_DISTANCE_17)
    tDraw.pu()
    # letter O
    tDraw.setheading(HEADING_EAST)
    tDraw.fd(MOVE_DISTANCE_18)
    tDraw.pd()
    tDraw.circle(LETTER_O)
    tDraw.pu()
    # letter N
    tDraw.fd(MOVE_DISTANCE_19)
    tDraw.setheading(HEADING_NORTH)
    tDraw.pd()
    tDraw.fd(MOVE_DISTANCE_17)
    tDraw.setheading(HEADING_SOUTHEAST_1) 
    tDraw.fd(MOVE_DISTANCE_20)
    tDraw.setheading(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_17)
    tDraw.pu()
    # letter G
    tDraw.goto(LETTER_G_X_AXIS,logoFloorY)
    tDraw.setheading(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_21)
    tDraw.pd()
    tDraw.setheading(HEADING_EAST)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.right(TURN_ANGLE_12)
    tDraw.fd(MOVE_DISTANCE_9)
    tDraw.circle(G_CURVE_RADIUS,G_CURVE_ANGLE)
    tDraw.pu()
    # letter U
    tDraw.goto(LETTER_U_X_AXIS,(logoFloorY+150))
    tDraw.pd()
    tDraw.seth(HEADING_SOUTHEAST_2)
    tDraw.fd(MOVE_DISTANCE_3)
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(LETTER_U_RADIUS,LETTER_U_ANGLE)
    tDraw.seth(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_3)
    tDraw.pu()
    # letter S
    tDraw.goto(500,(logoFloorY+150))
    tDraw.seth(HEADING_EAST)
    tDraw.pd()
    tDraw.bk(MOVE_DISTANCE_1)
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(LETTER_S_RADIUS_1,LETTER_S_ANGLE)
    tDraw.right(TURN_ANGLE_2)
    tDraw.bk(MOVE_DISTANCE_1)
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(LETTER_S_RADIUS_2,LETTER_S_ANGLE)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.ht()

def charaOutline(tDraw,wWidth,wHeight):
    '''
    creating the 'A' in the logo using a crewmates body, 
    meant as a extension to the crewmateBody function assisting in color change and positioning
    args: 
        tDraw (turtle): used to draw the 'A' which is in the shape of a crewmate
        wWidth (int): used for the correct X axis of the turtles beginning position
        wHeight (int): used for the correct Y axis of the turtles beginning position
    '''
    #value assignments
    outline_size = 2
    #chara logo drawing
    tDraw.up()
    tDraw.goto((-wWidth*0.2),(wHeight * 0.3))
    tDraw.color("white")
    tDraw.setheading(HEADING_EAST)
    tDraw.pensize(outline_size)
    tDraw.down()
    crewmateBody(tDraw,BLANK)

def imposter(tDraw,pos_imposter):
    '''
    randomnly chooses a crewmate, besides the one at the front.
    args: 
        tDraw (turtle): used to draw imposters eye spark and knife
        pos_imposter(list): using the list randomly chooses one of the imposters to draw the eye, within the list is the X and Y position of the eye in the visor
    '''
    #value assignemnts
    logo_size= 2
    blade_color = ("#e6e6e6")
    hilt_color = ("#adadad")
    handle_color = ("brown")
    outline = ("black")
    glare_color = ("red")
    #imposter selection and drawing
    randImp=random.randint(0,3)
    (x,y)=pos_imposter[randImp]
    tDraw.color(outline)
    tDraw.fillcolor(glare_color)
    tDraw.pensize(logo_size)
    tDraw.up()
    tDraw.goto((x-40),y)
    #top left
    tDraw.setheading(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_8)
    knifeX,knifeY=tDraw.pos()
    tDraw.down()
    tDraw.begin_fill()
    tDraw.setheading(HEADING_SOUTH)
    tDraw.left(TURN_ANGLE_6)
    tDraw.fd(MOVE_DISTANCE_9)
    tDraw.setheading(HEADING_SOUTH)
    tDraw.fd(MOVE_DISTANCE_7)
    tDraw.circle(IMPOSTER_RADIUS_1, IMPOSTER_ANGLE_1)
    tDraw.fd(MOVE_DISTANCE_10)
    #left point
    tDraw.setheading(HEADING_SOUTH)
    tDraw.fd(MOVE_DISTANCE_11)
    tDraw.right(TURN_ANGLE_1)
    tDraw.backward(MOVE_DISTANCE_10)
    tDraw.circle(IMPOSTER_RADIUS_2, IMPOSTER_ANGLE_2)
    #bottom 
    tDraw.backward(MOVE_DISTANCE_7)
    tDraw.right(TURN_ANGLE_6)
    tDraw.fd(MOVE_DISTANCE_9)
    tDraw.setheading(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_7)
    #right 
    tDraw.circle(IMPOSTER_RADIUS_3,IMPOSTER_ANGLE_1)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.setheading(HEADING_NORTH)
    tDraw.fd(MOVE_DISTANCE_11)
    tDraw.setheading(HEADING_WEST)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.circle(IMPOSTER_RADIUS_3,IMPOSTER_ANGLE_1)
    tDraw.fd(MOVE_DISTANCE_12)
    tDraw.end_fill()
    #knife position
    tDraw.up()
    tDraw.goto((knifeX+47),(knifeY+15))
    tDraw.color(handle_color)
    tDraw.fillcolor(handle_color)
    tDraw.left(TURN_ANGLE_7)
    tDraw.down()
    tDraw.begin_fill()
    #handle
    for i in range(2):
        tDraw.fd(MOVE_DISTANCE_10)
        tDraw.right(TURN_ANGLE_1)
        tDraw.fd(MOVE_DISTANCE_14)
        tDraw.right(TURN_ANGLE_1)
    tDraw.end_fill()
    tDraw.color(hilt_color)
    tDraw.fillcolor(hilt_color)
    tDraw.begin_fill()
    tDraw.right(TURN_ANGLE_8)
    tDraw.backward(MOVE_DISTANCE_13)
    for i in range(2):
        tDraw.fd(MOVE_DISTANCE_14)
        tDraw.right(TURN_ANGLE_11)
        tDraw.fd(MOVE_DISTANCE_15)
    tDraw.end_fill()
    #blade
    tDraw.up()
    tDraw.backward(MOVE_DISTANCE_15)
    tDraw.color(blade_color)
    tDraw.fillcolor(blade_color)
    tDraw.begin_fill()
    tDraw.right(TURN_ANGLE_9)
    tDraw.down()
    tDraw.fd(MOVE_DISTANCE_4)
    tDraw.right(TURN_ANGLE_10)
    tDraw.fd(MOVE_DISTANCE_16)
    tDraw.end_fill()

def crewmateLocation(tDraw,newCharaX,turtY):
    '''
    used to prepare for the drawing of another crewmate on the same Y axis as the other crewmate but moved moved over on the X axis
    args: 
        tDraw (turtle): to set the turtle in the proper position
        turtY (int): used to return to the beginning position of the next crewmate drawing 
    return: 
        newCharaX (int): returns the X position of the new crewmate to properly space the next crewmate
    '''
    #value assignment
    crewmate_spacing_x = 180
    #new crewmate drawing
    tDraw.up()
    tDraw.goto(newCharaX+(crewmate_spacing_x),turtY)
    tDraw.setheading(HEADING_EAST)
    tDraw.down()
    newCharaX=tDraw.xcor()
    return newCharaX

def backpack(tDraw,bodyColor):
    '''
    This function makes the backpack for the crewmates
    args: 
        tDraw (turtle): to draw the backpack
    '''
    #drawing backpack
    tDraw.up()
    tDraw.right(TURN_ANGLE_3)
    tDraw.fd(MOVE_DISTANCE_6)
    tDraw.right(TURN_ANGLE_1)
    tDraw.fd(MOVE_DISTANCE_7)
    tDraw.fillcolor(bodyColor)
    tDraw.begin_fill()
    tDraw.down()
    tDraw.fd(MOVE_DISTANCE_4)
    tDraw.left(TURN_ANGLE_5)
    tDraw.circle(BACKPACK_RADIUS, BACKPACK_ANGLE)
    tDraw.left(TURN_ANGLE_3)
    tDraw.fd(MOVE_DISTANCE_4)
    tDraw.end_fill() 

def visor(tDraw,VISOR_GLASS):
    '''
    this function makes the visor on the head of the crewmates suit, returning the placement for the possible imposter drawing
    args: 
        tDraw (turtle): to draw the visor
    return: 
        visorX (int): returns the x axis of the crewmates visor, to be stored for potential imposter
        visorY (int): returns the y axis of the crewmates visor, to be stored for potential imposter
    '''
    #Visor curves
    visor_radius = 25
    visor_angle = 190
    #visor drawing
    tDraw.up()
    tDraw.right(TURN_ANGLE_3)
    tDraw.fd(MOVE_DISTANCE_3)
    tDraw.left(TURN_ANGLE_1)
    tDraw.down()
    tDraw.fillcolor(VISOR_GLASS)
    tDraw.begin_fill()
    tDraw.circle((-(visor_radius)),visor_angle)
    tDraw.left(TURN_ANGLE_4)
    tDraw.fd(MOVE_DISTANCE_4)
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(visor_radius,(-(visor_angle)))
    tDraw.setheading(HEADING_NORTH)
    tDraw.up()
    tDraw.fd(MOVE_DISTANCE_1)
    visorX,visorY=tDraw.pos()
    tDraw.backward(MOVE_DISTANCE_1)
    tDraw.down()
    tDraw.setheading(HEADING_EAST)
    tDraw.backward(MOVE_DISTANCE_3)
    tDraw.end_fill()
    return visorX,visorY

def crewmateBody(tDraw,bodyColor):
    '''
    this function creates the crewmates body.
    args: 
        tDraw (turtle): draws the crewmates body
        bodyColor(list): a list of all the crewmates body color, goes through a for loop to change the color everytime
    '''
    #draw body  
    tDraw.fillcolor(bodyColor)
    tDraw.begin_fill()
    #Right
    tDraw.right(TURN_ANGLE_1)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(CIRCLE_RADIUS_1, CIRCLE_ANGLE_1)
    tDraw.right(TURN_ANGLE_2)
    tDraw.fd(MOVE_DISTANCE_2)
    #Head
    tDraw.right(TURN_ANGLE_2)
    tDraw.circle(HEAD_RADIUS, CIRCLE_ANGLE_1)
    #Left
    tDraw.backward(MOVE_DISTANCE_2)
    #Waist
    tDraw.circle(WAIST_RADIUS, CIRCLE_ANGLE_1)
    tDraw.right(TURN_ANGLE_2)
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.up()
    tDraw.left(TURN_ANGLE_1)
    tDraw.down()
    tDraw.fd(MOVE_DISTANCE_1)
    tDraw.end_fill()

def stars(tDraw,wWidth,wHeight):
    '''
    creates background of stars for picture
    args: 
        tDraw (turtle): to draw the stars
        wWidth (int): to keep the stars within the seeable X axis
        wHeight (int): to keep the stars within the seeable Y axis
    '''
    #star creation
    for i in range(NUMBER_OF_STARS):
        tDraw.up()
        tDraw.color(STAR_COLOR)
        screenWidth=(wWidth//2)
        screenHeight=(wHeight//2)
        # randomly selected location for stars
        randWidth=random.randint((-screenWidth),screenWidth)
        randHeight=random.randint((-screenHeight),screenHeight)
        tDraw.goto(randWidth,randHeight)
        tDraw.down()
        tDraw.dot(STAR_SIZE,STAR_COLOR)

def main():
    #value assignments
    screen_floor_x_axis = 0.2
    screen_floor_y_axis = 0.4
    pen_size = 7.5
    drawing_speed = 0
    #initalize
    window=turtle.Screen()
    window.setup(width=1.0,height=1.0)
    pos_imposter=[]
    window.bgcolor("black")
    tDraw=turtle.Turtle()
    tDraw.shape("turtle")
    tDraw.speed(drawing_speed)
    wWidth=window.window_width()
    wHeight=window.window_height()
    #drawing begins
    stars(tDraw,wWidth,wHeight)
    tDraw.up()
    tDraw.goto((-wWidth*screen_floor_x_axis),(-wHeight * screen_floor_y_axis))
    turtX,turtY=tDraw.pos()
    tDraw.color("black")
    tDraw.pd()
    #loop for all 5 crewmates
    for i in range(NUMBER_OF_CREWMATES):
        bodyColor=CREWMATES[i]
        tDraw.pensize(pen_size)
        crewmateBody(tDraw,bodyColor)
        (x,y)=visor(tDraw,VISOR_GLASS)
        pos_imposter.append((x,y))
        backpack(tDraw,bodyColor)
        turtX=crewmateLocation(tDraw,turtX,turtY)
    #drawing for logo
    imposter(tDraw,pos_imposter)
    charaOutline(tDraw,wWidth,wHeight)
    visor(tDraw,BLANK)
    backpack(tDraw,BLANK)
    logo(tDraw,window)
    #exit
    window.exitonclick()


#begin program
if __name__=="__main__":
    main()