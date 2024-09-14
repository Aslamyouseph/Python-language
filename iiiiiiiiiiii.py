from turtle import Turtle,Screen
screen=Screen()
tom=Turtle()
def move_forward():
    tom.forward(20)
def move_backward():
    tom.backward(20)
def turn_left():
    new_heading=tom.heading()+20  #used to move in a specific possition to left 
    tom.setheading(new_heading)
    tom.forward(10)
def turn_right():
    new_heading=tom.heading()-20  #used to move in a specific possition in to right 
    tom.setheading(new_heading)
    tom.forward(10)
def clear_screen():
    tom.clear() 
    tom.penup()
    tom.home()  
    tom.pendown()

screen.listen()  
screen.onkey(fun=move_forward,key="f")  
screen.onkey(fun=move_backward,key="b")
screen.onkey(fun=turn_left,key="l")
screen.onkey(fun=turn_right,key="r")
screen.onkey(fun=clear_screen,key="c")  

screen.exitonclick()

