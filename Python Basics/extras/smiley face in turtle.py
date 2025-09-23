from turtle import *
# gonna try to draw a smiley face

def Head():
    penup()
    right(90)
    forward(250)
    left(90)
    pendown()
    fillcolor("Yellow")
    begin_fill()
    pencolor("Black")
    circle(250)
    end_fill()

def EyeBalls():
    penup()
    left(90)
    forward(300)
    right(90)
    forward(100)
    fillcolor("Black")
    begin_fill()
    pencolor("Black")
    circle(40)
    end_fill()
    penup()
    left(180)
    forward(200)
    pendown
    begin_fill()
    circle(-40)
    end_fill()

def Mouth():
    penup()
    left(180)
    forward(100)
    right(90)
    forward(100)
    left(90)
    pendown()
    fillcolor("Black")
    begin_fill()
    pencolor("Black")
    forward(150)
    right(180)
    forward(300)
    right(90)
    circle(-150, -180)
    # makes a semicircle, the -150 and -180 makes it go the way it needs (150 is radius, 180 is the degrees it draws)
    end_fill()
    exitonclick()
    
def Smiley():
    Head()
    EyeBalls()
    Mouth()
    
Smiley()