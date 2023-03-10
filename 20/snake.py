from turtle import Turtle

DIRECTIONS = {
    'UP': 90,
    'DOWN': 270,
    'LEFT': 180,
    'RIGHT': 0
}


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])
