from turtle import Turtle,Screen
screen=Screen()
tom=Turtle()
def up():
    tom.setheading(90)
    tom.forward(20)
def down():
    tom.setheading(270)
    tom.forward(20)
def left():
    tom.setheading(180)
    tom.forward(20)
def right():
    tom.setheading(0)
    tom.forward(20)
def clear_screen():
    tom.clear()  #used to clear the creen if we click on c 
    tom.penup()
    tom.home()    # move to the head (0,0) coordinate 
    tom.pendown()

screen.listen()  # it is used to to invock the bellow written funtion 
screen.onkey(fun=up,key="Up")  # use to call the up(), funtion (when we click on the upward arrow then it automatically call this funtion)
screen.onkey(fun=down,key="Down")
screen.onkey(fun=left,key="Left")
screen.onkey(fun=right,key="Right")
screen.onkey(fun=clear_screen,key="c")   # calling the clear screen funtion 

screen.exitonclick()

#this program which is like when we click the particular key then it automatically call the particular funtion 
# eg if we click the "c" then it call the clear screen fintion and it clear the screen automatically 
# up used to move head on upward direction 
#like  exetra all 