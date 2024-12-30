"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           
turtle.setup (width=600, height=600)    

tina = turtle.Turtle()                  

tina.shape('turtle')                   
tina.speed(2)                         

tina.pencolor('red')                   
tina.forward(150)                       
tina.left(90)                           
tina.pencolor('green')                
tina.forward(150)
tina.left(90)
tina.pencolor('blue')                   
tina.forward(150)                       
tina.left(90)                           

tina.pencolor('black')                
tina.forward(150)
tina.left(90)



# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.exitonclick()                     # Close the window when we click on it