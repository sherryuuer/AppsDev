# higher order function is a function take a function as a paramater.do not need to write ().
from turtle import Turtle, Screen

tim = Turtle()
my_playground = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.forward(10)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_playground.listen()
my_playground.onkey(key="w", fun=move_forward)
my_playground.onkey(key="s", fun=move_backward)
my_playground.onkey(key="a", fun=turn_left)
my_playground.onkey(key="d", fun=turn_right)
my_playground.onkey(key="c", fun=clear)

my_playground.exitonclick()
