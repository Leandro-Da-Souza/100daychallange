from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


DIMENSIONS = {
    'width': 900,
    'height': 600
}

game_screen = Screen()
game_screen.bgcolor('black')
game_screen.setup(width=DIMENSIONS['width'], height=DIMENSIONS['height'])
game_screen.title('Pong')
game_screen.tracer(0)

COORDINATES = {
    'left': (-(DIMENSIONS['width'] / 2 - 40), 0),
    'right': ((DIMENSIONS['width'] / 2 - 40), 0)
}

scoreboard = Scoreboard()
ball = Ball()
l_paddle = Paddle(COORDINATES['left'])
r_paddle = Paddle(COORDINATES['right'])

game_screen.listen()
game_screen.onkey(key="w", fun=l_paddle.go_up)
game_screen.onkey(key="s", fun=l_paddle.go_down)
game_screen.onkey(key='Up', fun=r_paddle.go_up)
game_screen.onkey(key='Down', fun=r_paddle.go_down)

is_game_on = True

while is_game_on:
    sleep(ball.move_speed)
    game_screen.update()
    ball.move(DIMENSIONS['height'] - 10)

    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.xcor() > -390:
        ball.bounce()

    if ball.xcor() > 470:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -470:
        ball.reset()
        scoreboard.r_point()


game_screen.exitonclick()
