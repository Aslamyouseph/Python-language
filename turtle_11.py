import random
from turtle import Turtle, Screen

WIDTH, HEIGHT = 400, 400
color_list = ["red", "green", "blue", "yellow", "orange", "brown", "pink", "black", "violet"]


def no_of_turtle():
    count = 0
    while True:
        count = input("How many turtles do you want to practice in the race: 2 - 10 ")
        if count.isdigit():
            count = int(count)
        else:
            print("Please enter a numeric value between 2 and 10: ")
            continue
        if 2 <= count <= 10:
            return count
        else:
            print("Input is not in the given range, please try again")


turtles = no_of_turtle()
print(turtles)

s1 = Screen()
s1.setup(400, 400)

x_spacing = WIDTH // (turtles + 1)
turtle_list = []

for i in range(1, turtles + 1):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.pencolor(color_list[i % len(color_list)])  # Set turtle color
    new_turtle.fillcolor(color_list[i % len(color_list)])  # Set fill color
    new_turtle.left(90)
    new_turtle.penup()
    new_turtle.goto(-WIDTH // 2 + (i * x_spacing), -HEIGHT // 2 + 10)
    turtle_list.append(new_turtle)


def race():
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randrange(1, 20)
            t.begin_fill()  # Begin filling the turtle
            t.forward(distance)
            x, y = t.pos()
            if y >= HEIGHT // 2 - 20:
                print(f"Winner is {t.pencolor()} turtle")
                is_race_on = False
            t.end_fill()  # End filling the turtle


race()
s1.exitonclick()
