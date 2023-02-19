from turtle import Turtle

FONT = ('Helvetica', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 260)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align='center', font=FONT)
