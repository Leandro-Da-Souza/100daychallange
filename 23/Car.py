from turtle import Turtle, colormode
from random import randint

colormode(255)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.velocity = 10
        self.create()

    def create(self):
        self.shape('square')
        self.penup()
        self.start_position()
        self.car_color()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def car_color(self):
        self.color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

    def start_position(self):
        self.sety(randint(-260, 260))
        self.setx(randint(-260, 260))

    def move_car(self):
        new_x = self.xcor() - self.velocity
        if self.xcor() < -300:
            self.reset()
        else:
            self.setx(new_x)

    def reset(self):
        self.sety(randint(-260, 260))
        self.setx(300)

    def increase_velocity(self):
        self.velocity += 10
