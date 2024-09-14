import turtle
from turtle import Turtle
import random
turtle.colormode(255)  # impoting or printing  all colour in python avilable 
asl=Turtle()
asl.width(10)
for i in range(100):
    r=random.randint(0,255)  # colour method 
    g=random.randint(0,255)  # colour method 
    b=random.randint(0,255)   # colour method 
    asl.setheading(random.randrange(0,360,90)) # used to randomely select the angle (in the  intreavels of 90 )
    asl.pencolor(r,g,b)
    asl.forward(40)
asl.screen.mainloop()
