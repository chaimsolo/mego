from turtle import Turtle, Screen
from random import *


screen = Screen()
screen.setup(width=500, height=400, startx=400, starty=100)
colors = ["green", "blue",  "yellow",  "purple", "orange"]
turtles = []
for i in range(-2, 3):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color(colors[i-1])
    timmy.goto(-240, 180 / 2 * i)
    timmy.pendown()
    turtles.append(timmy)
user_guess = screen.textinput(title="Hello!  Enter your guess", prompt="which turtle will win? (enter a color)")
flag = 1
while flag:
    for i in range(5):
        turtles[i].forward(randint(10, 30))
        turtles[i].speed(randint(1, 10))
        if turtles[i].xcor() > 205:
            winner = turtles[i].pencolor()
            flag = 0
            break
if winner == user_guess:
    print(f"You guessed right. the turtle {winner} is the winner.")
else:
    print(f"You didn't guessed right. you guesse {user_guess}, and the {winner} turtle  is the winner ")

screen.exitonclick()



