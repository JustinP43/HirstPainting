import turtle
from colors import color_list
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
screen = turtle.Screen()

number_of_dots = 400

timmy.penup()
timmy.setheading(180)
timmy.forward(500)
timmy.setheading(270)
timmy.forward(450)
timmy.setheading(0)

for dot in range(1,21):
    for _ in range(1,21):
        timmy.pendown()
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(1000)
    timmy.setheading(0)

screen.exitonclick()



