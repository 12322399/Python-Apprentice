"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("light blue")
window.setup(width=600, height=600, startx=0, starty=0)

colors = ("red", "orange", "yellow", "green", "blue","purple","red", "orange", "yellow", "green", "blue","purple")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(0)

sides = 5
angle = 360 / sides

for i in range(80000000):
    if i == 100:
        myTurtle.width(2)
    if i == 200:
        myTurtle.width(3)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle + 1)

myTurtle.hideturtle()

turtle.done()
