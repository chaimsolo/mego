
from turtle import Turtle, Screen

from color_of_turtle import Color



tim = Turtle()

screen = Screen()
tim.shape("turtle")
screen.colormode(255)
tim.pensize(2)


for j in range(0, 1000):
    if j % 4 == 0:
        color = Color()
        rgb = color.rgb
    for i in range(4):
        tim.speed(0)
        tim.pencolor(rgb)
        tim.forward(10 + j)
        tim.right(90)
    tim.left(90)
    tim.forward(10 + j)

screen.exitonclick()