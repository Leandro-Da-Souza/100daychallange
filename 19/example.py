from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

screen.listen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def move_clockwise():
    tom.right(10)


def move_counter_clockwise():
    tom.left(10)


screen.onkey(key="w", fun=move_forwards)

screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="a", fun=move_counter_clockwise)

screen.onkey(key="d", fun=move_clockwise)

screen.exitonclick()
