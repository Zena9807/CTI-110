# Janzena Montague
# November 4, 2023
# P4LAB1 - Turtle Graphics

# Pseudocode:
# Import the Turtle library
# Setup the drawing window
# Change the background color to light blue
# Create a turtle object
# Change the turtle's color
# Use a for loop to draw a square
# Move the turtle to the top of the square
# Use a for loop to draw a triangle for the roof
# Keep the window open

import turtle

window = turtle.Screen()
window.bgcolor("lightblue")

house = turtle.Turtle()
house.color("navy")
house.pensize(3)
house.speed(3)
for side in range(4):
    house.forward(150)
    house.left(90)

house.penup()
house.forward(150)
house.left(90)
house.forward(150)
house.pendown()
count=0
house.left(30)
house.fillcolor("brown")
house.begin_fill()

while count < 3:
    house.forward(150)
    house.left(120)
    count += 1

house.end_fill()

turtle.done()


