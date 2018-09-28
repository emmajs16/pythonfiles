# Emma Stoverink
# September 7, 2018
# Problem: Draw four connected circles for the turtle when given a radius

import turtle

# Get radius from turtle
radius = int(input("Please enter a radius for the turtle:"))

# Draw the bottom two circles
turtle.circle(radius)
turtle.penup()
turtle.forward(radius*2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.right(90)
turtle.forward(radius*2)
turn.left(180)
turtle.pendown()
turtle.circle(radius)
    