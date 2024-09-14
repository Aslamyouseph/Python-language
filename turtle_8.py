from turtle import Turtle,Screen
s1=Screen()
asl=Turtle()

print(asl.heading())  # this is used to find the where us the arrow is situated  
asl.speed(10)
asl.begin_fill()
asl.color("red","blue")
asl.penup()
asl.goto(+200,+180)
asl.pendown()
while True:
    asl.forward(200)
    asl.left(170)
    if asl.heading()==0:  # giving the condition (when turtlr came in the orginal possition then  it stop )
        break
asl.end_fill()

asl.begin_fill()
asl.color("yellow","green")
asl.penup()
asl.goto(+200,-200)
asl.pendown()
while True:
    asl.forward(200)
    asl.left(170)
    if asl.heading()==0:
        break
asl.end_fill()

asl.begin_fill()
asl.color("red","blue")
asl.penup()
asl.goto(-200,-200)
asl.pendown()
while True:
    asl.forward(200)
    asl.left(170)
    if asl.heading()==0:
        break
asl.end_fill()

asl.begin_fill()
asl.color("yellow","green")
asl.penup()
asl.goto(-200,+180)
asl.pendown()
while True:
    asl.forward(200)
    asl.left(170)
    if asl.heading()==0:
        break
asl.end_fill()

asl.begin_fill()
asl.color("red","yellow")
asl.penup()
asl.goto(0,0)
asl.pendown()
while True:
    asl.forward(200)
    asl.left(170)
    if asl.heading()==0:
        break
asl.end_fill()

s1.exitonclick()