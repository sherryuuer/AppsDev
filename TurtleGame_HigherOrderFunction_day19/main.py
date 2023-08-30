# higher order function is a function take a function as a paramater.do not need to write ().
from turtle import Turtle, Screen

tim = Turtle()
my_playground = Screen()


def move_forward():
    tim.forward(50)


my_playground.listen()
my_playground.onkey(key="space", fun=move_forward)
my_playground.exitonclick()
