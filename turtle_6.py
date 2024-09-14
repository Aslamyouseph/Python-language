import random
from turtle import Turtle
asl=Turtle()
colors=["red","blue","black","green","yellow","pink","orange","brown","gray","alice blue",]
for i in range(3,10):
    angle=360 / i
    asl.pencolor(random.choice(colors))
    for _ in range (i):
        asl.forward(100)
        asl.right(angle)
asl.screen.mainloop()