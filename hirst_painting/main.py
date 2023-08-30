import colorgram
from turtle import Turtle, Screen, colormode
import random

poly = Turtle()
my_screen = Screen()
colormode(255)

colors = colorgram.extract('hirst_painting/image.jpg', 25)

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

# poly.pencolor("")
# poly.color = ""
poly.penup()
# hide the turtle
poly.ht()
poly.setheading(225)
poly.fd(300)
poly.setheading(0)

# for i in range(10):
#     for _ in range(10):
#         poly.dot(20, random.choice(color_list))
#         poly.fd(50)
#     poly.left(90)
#     poly.fd(50)
#     poly.left(90)
#     poly.fd(500)
#     poly.right(180)
# another answer
number_of_dots = 100
for _ in range(1, number_of_dots + 1):
    poly.dot(20, random.choice(color_list))
    poly.fd(50)
    if _ % 10 == 0:
        poly.left(90)
        poly.fd(50)
        poly.left(90)
        poly.fd(500)
        poly.right(180)
