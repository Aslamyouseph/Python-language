import turtle
from turtle import Turtle
import random
turtle.colormode(255)  
asl=Turtle()
asl.speed(12) #used for increasss peed 
while True:
    r=random.randint(0,255)  # colour method 
    g=random.randint(0,255)  # colour method 
    b=random.randint(0,255)
    asl.circle(100)
    asl.left(5)
    asl.pencolor(r,g,b)
    if asl.heading()==0:
        break
asl.screen.mainloop()