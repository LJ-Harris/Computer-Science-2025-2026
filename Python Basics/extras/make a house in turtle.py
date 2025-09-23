from turtle import *

def square(length, degrees):
    for counter in range(4):
        forward(length)
        right(degrees)
        
def triangle(lenght):
    for counter in range(3):
        forward(lenght)
        left(120)

def house(length):
    square(length, degrees)
    triangle(length)
    penup()
    forward(length / 3)
    right(90)
    forward(length)
    left(90)
    pendown()
    square((length / 3), (degrees * -1))

degrees = 90
length = int(input("Enter an amount for the sides of the shapes	"))
house(length)



exitonclick()