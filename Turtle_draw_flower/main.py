from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.color("blue")
timmy.shape("turtle")

my_screen = Screen()

# # draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# --------
# # import a package by installing it
# import heroes
# print(heroes.gen())

# -------
# # draw a dashed line
# for _ in range(10):
#     timmy.forward(5)
#     timmy.up()
#     timmy.forward(5)
#     timmy.down()

# -------
# # draw a loop flower.ww
# colors = ["blue", "red", "yellow", "black", "chartreuse", "hot pink", "dark magenta", "salmon"]
# for n in range(3, 10):
#     angle = 360 / n
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.right(angle)
#         timmy.pencolor(random.choice(colors))

# -------

# colors = ["blue", "red", "yellow", "black", "chartreuse", "hot pink", "dark magenta", "salmon"]
colormode(255)


def choice_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# # draw a random walk
# timmy.pensize(10)
# angle = [0, 90, 180, 270]
# for n in range(100):
#     # pencolor = random.choice(colors)
#     speeds = range(0, 10)
#     timmy.pencolor(choice_color())
#     timmy.speed(random.choice(speeds))
#     timmy.forward(30)
#     # timmy.right(random.choice(angle))
#     timmy.setheading(random.choice(angle))


# draw spirogragh
timmy.speed(9)


def draw_spirogragh(n):
    for _ in range(int(360 / n)):
        timmy.circle(50)
        timmy.setheading(timmy.heading() + n)
        timmy.pencolor(choice_color())


draw_spirogragh(10)
