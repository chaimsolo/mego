from turtle import Turtle, Screen
from random import choice, randint
timmy = Turtle()
color = ["green", "yellow",  "blue", "light blue", "light green"]
# direction = [90, 270]
# timmy.pensize(20)
#
# while True:
#     pen_direction = choice(direction)
#     pen_color = choice(color)
#     steps = randint(20, 150)
#     timmy.color(pen_color)
#     timmy.right(pen_direction)
#     timmy.forward(steps)


for j in range(3, 9):
    pen_color = choice(color)
    for i in range(j):
        timmy.color(pen_color)
        timmy.forward(80)
        timmy.right(180 - (180 * (j - 2) / j))



screen = Screen()

screen.exitonclick()