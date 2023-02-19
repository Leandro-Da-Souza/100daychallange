from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.start_x = 0
        self.start_y = -280
        self.velocity = 15
        self.create_player()
        self.start_position()

    def create_player(self):
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()

    def start_position(self):
        self.goto(self.start_x, self.start_y)

    def move_up(self):
        new_y = self.ycor() + self.velocity
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - self.velocity
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + self.velocity
        self.goto(new_x, self.ycor())

    # def move_down(self):
    #     new_y = self.ycor() - self.velocity
    #     self.goto(self.xcor(), new_y)



