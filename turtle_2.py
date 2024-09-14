from turtle import Turtle,Screen  #importing creen also
s1=Screen()  # creating the screen object also  
tom=Turtle()      # creating a object for the turtle 
tom.shape("turtle")
tom.color("black","green") # black is the outline colour amd green is the insid colure 
tom.begin_fill()
tom.circle(100)
tom.end_fill()
#tom.hideturtle()   used to hide the title picture 


tom.right(90)
tom.penup() # used to up the pen 
tom.forward(100)
tom.pendown() # used to down the pen 
tom.color("blue","red")  
tom.begin_fill()
tom.circle(100)
tom.end_fill()
#tom.hideturtle()


tom.right(90)
tom.penup()
tom.forward(100)
tom.pendown()
tom.color("black","green")
tom.begin_fill()
tom.circle(100)
tom.end_fill() 
#tom.hideturtle()


tom.right(90)
tom.penup()
tom.forward(100)
tom.pendown()
tom.color("blue","red")
tom.begin_fill()
tom.circle(100)
tom.end_fill()
#tom.hideturtle()

s1.mainloop() # used to hold the screen 
