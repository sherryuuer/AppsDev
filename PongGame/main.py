# Create the screen.
# Create and move a paddle.
# Create another paddle.
# Create the ball and make it move.
# Detect collision with wall and bounce.
# Detect collision with paddle.
# Detect when paddle misses.
# Keep score.
from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game by Sally")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
