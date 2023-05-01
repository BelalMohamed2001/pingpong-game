import turtle # for the design of shapes
wind=turtle.Screen() # for build screen from turtle module
wind.title("ping pong by belal") # to give title to this window
wind.bgcolor("black") # fore color of screen
wind.setup(width=800,height=600) # setup is function to give screen width and height
wind.tracer(0) # to control of speed of game /stop updata auto 

# first paddle of ping pong
paddle1=turtle.Turtle() # to take shape create object from turtle
paddle1.speed(0) # to select speed of build shape
paddle1.shape("square") # type of shape
paddle1.color("red") # color of shape
paddle1.penup() #   no drawing any line during moveing
paddle1.goto(-350,0) # to select position of first paddle in screen
paddle1.shapesize(stretch_wid=5,stretch_len=1) # to select size of shape // the dafult size is 20 so 20 * 5 is 100

# second paddle of ping pong
paddle2=turtle.Turtle() # to take shape
paddle2.speed(0) # to select speed of build shape
paddle2.shape("square") # type of shape
paddle2.color("green") # color of shape
paddle2.penup() #   no drawing any line during moveing
paddle2.goto(350,0) # to select position of first paddle in screen  / the coordinates width =800 so the screen will divide 400 and -400
paddle2.shapesize(stretch_wid=5,stretch_len=1) # to select size of shape // the dafult size is 20 so 20 * 5 is 100

# ball
ball=turtle.Turtle() # to take shape
ball.speed(0) # to select speed of build shape
ball.shape("square") # type of shape
ball.color("white") # color of shape
ball.penup() #   no drawing any line during moveing
ball.goto(0,0) # to select position of first paddle in screen  / the coordinates width =800 so the screen will divide 400 and -400
ball.dx=0.1 # to move (speed 2.5) diagonal to up
ball.dy=0.1










# function to move the game
def paddle1_up():
    y=paddle1.ycor() # function in turtle to select position of paddle1
    y+=20 # to move up 20 pixel
    paddle1.sety(y) # to get new y

def paddle1_down():
    y=paddle1.ycor() # function in turtle to select position of paddle1
    y-=20 # to move down 20 pixel
    paddle1.sety(y) # to get new y

def paddle2_up():
    y=paddle2.ycor() # function in turtle to select position of paddle1
    y+=20 # to move up 20 pixel
    paddle2.sety(y) # to get new y

def paddle2_down():
    y=paddle2.ycor() # function in turtle to select position of paddle1
    y-=20 # to move down 20 pixel
    paddle2.sety(y) # to get new y
        
    

# keyboards bindings
wind.listen() # function to give screen information about keyboard
wind.onkeypress(paddle1_up,"w") # give screen when user press w move up
wind.onkeypress(paddle1_down,"s")
wind.onkeypress(paddle2_up,"Up") # give screen when user press w move up
wind.onkeypress(paddle2_down,"Down")


while True:  # for never stop game / ball never stop
    wind.update() # to updata screen  everytime  loop run
    ball.setx(ball.xcor()+ball.dx) # to get position of ball and move it up by dx
    ball.sety(ball.ycor()+ball.dy)
    # border check to return the ball size 20 pixel and y coor is 300  and x coor is 400
    if ball.ycor()>290: # When the ball is in position 290, touch a y coor return why 290 because ball size is 20 pixel
        ball.sety(290) # set position of ball at 290
        ball.dy*=-1  # to return from y coor 2.5 * -1 (reverse)

    if ball.ycor()<-290: 
        ball.sety(-290)
        ball.dy*=-1  

    if ball.xcor()>390: # samy y same x
       #ball.goto(0,0)  #if you would like to return ball to the center
       ball.dx*=-1

    if ball.xcor()<-390: # samy y same x
       #ball.goto(0,0)  #if you would like to return ball to the center
       ball.dx*=-1




    # tasadom paddle and ball
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()<paddle2.ycor()+40 and ball.ycor()> paddle2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1     

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle1.ycor()+40 and ball.ycor()> paddle1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1                   