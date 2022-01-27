import colorgram
from turtle import Turtle, Screen
import turtle as turtle_moudle
import random
turtle_moudle.colormode(255)
rgb_colors = []

# colors = colorgram.extract('download.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
print(rgb_colors)
color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148)]
turtle = Turtle()
screen = Screen()
turtle.penup()

turtle.shape("turtle")
turtle.color("green")
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)
number_of_dots = 100
turtle.showturtle()
for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count %10 ==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
turtle.hideturtle()
screen.exitonclick()
