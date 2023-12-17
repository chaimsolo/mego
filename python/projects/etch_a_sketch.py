from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def turn_right():
    pen.right(10)

def turn_left():
    pen.left(10)

def go_forward():
    pen.forward(10)

def go_backward():
    pen.backward(10)

def clean_screen():
    pen.home()
    pen.clear()


screen.listen()

screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="c", fun=clean_screen)

screen.exitonclick()