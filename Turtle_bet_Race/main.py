from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Who do you think will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
x = -230
y = -100
for color in colors:
    the_turtle = Turtle(shape="turtle")
    the_turtle.color(color)
    the_turtle.penup()
    the_turtle.goto(x, y)
    y += 50
    all_turtle.append(the_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You win!The winner is the {winner_turtle}!")
            else:
                print(f"You lose!The winner is the {winner_turtle}!")
        random_step = random.randint(0, 10)
        turtle.forward(random_step)






screen.exitonclick()
