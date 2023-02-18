from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.create(position)

    def create(self, position):
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
