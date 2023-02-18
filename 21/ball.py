from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def create(self):
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self, height):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)
        if self.ycor() < -(height / 2) or self.ycor() > height / 2:
            self.y_move = -self.y_move
            self.sety(self.ycor() + self.y_move)

    def bounce(self):
        self.x_move = -self.x_move
        self.setx(self.xcor() + self.x_move)
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce()
        self.move_speed = 0.05
