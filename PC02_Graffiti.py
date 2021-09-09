#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.goto(85,-80)
turtle.forward(25)
turtle.left(100)
turtle.color("LavenderBlush2")
turtle.left(5)
turtle.right(10)
turtle.down()
turtle.pensize(10)
turtle.forward(70)
turtle.backward(140)
turtle.up()
turtle.goto(110,80)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(30)
turtle.color("HotPink")
turtle.left(100)
turtle.forward(15)
turtle.down()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.up()
turtle.goto(24, 84)
turtle.forward(30)
turtle.right(100)
turtle.forward(40)
turtle.left(130)
turtle.forward(10)
turtle.pensize(4)
turtle.color("brown1")
turtle.down()
turtle.begin_fill()
turtle.forward(80)
turtle.left(40)
turtle.forward(20)
turtle.left(30)
turtle.forward(20)
turtle.left(40)
turtle.forward(20)
turtle.left(60)
turtle.forward(20)
turtle.left(20)
turtle.forward(20)
turtle.left(20)
turtle.forward(20)
turtle.forward(20)
turtle.forward(10)
turtle.left(40)
turtle.forward(30)
turtle.end_fill()
turtle.up()
turtle.goto(-25, 185)
turtle.forward(40)
turtle.right(20)
turtle.color("MediumVioletRed")
turtle.begin_fill()
turtle.down()
turtle.right(40)
turtle.forward(60)
turtle.left(120)
turtle.forward(60)
turtle.left(130)
turtle.forward(60)
turtle.forward(60)
turtle.right(120)
turtle.forward(70)
turtle.right(130)
turtle.forward(60)
turtle.left(30)
turtle.forward(10)
turtle.end_fill()
turtle.up()
turtle.color("maroon1")
turtle.right(50)
turtle.forward(15)
turtle.backward(30)
turtle.right(50)
turtle.forward(20)
turtle.right(80)
turtle.forward(10)
turtle.right(100)
turtle.forward(20)
turtle.right(100)
turtle.forward(20)
turtle.right(100)
turtle.forward(20)
turtle.right(200)
turtle.forward(15)
turtle.down()
turtle.begin_fill()
turtle.circle(12)
turtle.end_fill()
turtle.hideturtle()





#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
