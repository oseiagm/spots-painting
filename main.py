import turtle as turtle_module
import random

turtle_module.colormode(255)
kojo = turtle_module.Turtle()
kojo.speed("fastest")
kojo.penup()
colors = [(252, 186, 3), (3, 252, 123), (144, 3, 252), (252, 3, 123), (116, 247, 104), (104, 206, 247), (255, 211, 110), (252, 69, 3), (252, 3, 74), (106, 104, 247), (125, 219, 167), (240, 106, 29), (142, 227, 77), (79, 166, 247), (201, 54, 184)]

kojo.setheading(225)
kojo.fd(300)
kojo.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    kojo.dot(20, random.choice(colors))
    kojo.fd(50)

    if dot_count % 10 == 0:
        kojo.setheading(90)
        kojo.fd(50)
        kojo.setheading(180)
        kojo.fd(500)
        kojo.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
