# Create the snake.
# Make the snake move. here create the snake class.
# Control the snake.
# Detect collision with food.
# Create a scoreboard. here create the scoreboard class.
# Detect collision with wall.
# Detect collision with tail.
# where to create the screen class?
from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Timmy Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
