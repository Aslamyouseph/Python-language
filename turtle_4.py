from turtle import Turtle,Screen
s1=Screen()
asl=Turtle()

for i in range (1,15):
    asl.pendown()
    asl.color("red")
    asl.begin_fill()
    asl.forward(5)
    asl.end_fill()
    asl.penup()
    asl.forward(5)
    
    asl.pendown()
    asl.color("black")
    asl.begin_fill()
    asl.forward(5)
    asl.end_fill()
    asl.penup()
    asl.forward(5)

s1.mainloop()