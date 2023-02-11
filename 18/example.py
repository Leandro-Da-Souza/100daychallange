from turtle import Turtle, Screen
from random import randint

UI = Turtle()

UI.shape("turtle")
UI.color("burlywood", "DarkSlateGray")

screen = Screen()
screen.colormode(255)

"""Draw a square"""
# for _ in range(0, 4):
#     UI.forward(100)
#     UI.right(90)

"""Draw a straight dashed line"""
# for _ in range(0, 15):
#     UI.pendown()
#     UI.forward(10)
#     UI.penup()
#     UI.forward(10)


def draw_shape(shape: str, distance: int, color: str):
    angles = {
        "triangle": 360 / 3,
        "square": 360 / 4,
        "pentagon": 360 / 5,
        "hexagon": 360 / 6,
        "heptagon": 360 / 7,
        "octagon": 360 / 8,
        "nonagon": 360 / 9,
        "decagon": 360 / 10,
        "hendecagon": 360 / 11
    }

    UI.color(color)

    if shape.lower() == 'all':
        for x in angles:
            for _ in range(int(360 / angles[x])):
                UI.forward(distance)
                UI.right(int(angles[x]))
    else:
        for _ in range(int(360 / angles[shape])):
            UI.forward(distance)
            UI.right(int(angles[shape]))


# draw_shape(shape='all', distance=50, color='blue')


def random_walk(distance: int, loop: int, width: int):
    directions = {
        0: 180,
        1: 0,
        2: 90,
        3: 270,
    }
    for _ in range(loop):
        UI.color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )
        UI.pensize(width)
        UI.setheading(directions[randint(0, 3)])
        UI.forward(distance)
        UI.speed("fastest")


# random_walk(distance=30, loop=300, width=10)

def draw_spirograph(radius: int, step: int):
    UI.speed("fastest")
    for x in range(0, 360, step):
        UI.setheading(x)
        UI.color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )

        UI.circle(radius)


draw_spirograph(radius=100, step=6)

screen.exitonclick()
