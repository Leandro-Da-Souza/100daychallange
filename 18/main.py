import colorgram
from turtle import Turtle, Screen
import random

tom = Turtle()
tom.speed("fastest")

screen = Screen()
screen.mode("World")
screen.colormode(255)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

extracted = colorgram.extract("hirst.jpeg", 100)
colors = []

for x in extracted:
    colors += [(x.rgb.r, x.rgb.g, x.rgb.b)]


def make_hirst_painting():
    screen_size = int((screen.window_width() * screen.window_height()) / 100)
    y_ = 0
    for _ in range(screen_size):
        if tom.xcor() > screen.window_width():
            tom.hideturtle()
            tom.setx(0)
            y_ += 100
            tom.sety(y_)
            tom.showturtle()
        if tom.ycor() > screen.window_height():
            break
        tom.pendown()
        tom.dot(20, random.choice(colors))
        tom.penup()
        tom.forward(100)


make_hirst_painting()
screen.exitonclick()

