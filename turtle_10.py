import turtle
from turtle import Turtle,Screen 
import random
s1=Screen()
asl=Turtle()
s1.screensize(600,600)  # it is used to increes  the screen size 
print(s1.screensize())  #used to check  the screen size and printing the screen size 
asl.penup()
turtle.colormode(255) 
asl.speed(5)
for i in range(6000):  
    asl.dot(20)   # used to print a dot in 100 radious 
    r=random.randint(0,255)  # colour method 
    g=random.randint(0,255)  # colour method 
    b=random.randint(0,255)   # colour method
    asl.goto(random.randrange(-300,300),random.randint(-400,400))  # randomly choose a possition 
    asl.pencolor(r,g,b)
asl.screen.mainloop()