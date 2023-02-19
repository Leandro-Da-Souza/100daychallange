from turtle import Screen
from time import sleep
from Player import Player
from CarManager import CarManager
from ScoreBoard import ScoreBoard

game_screen = Screen()
game_screen.title('Turtle Crossing')
game_screen.setup(width=600, height=600)
game_screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = ScoreBoard()

game_screen.listen()
game_screen.onkey(key='w', fun=player.move_up)
game_screen.onkey(key='d', fun=player.move_right)
game_screen.onkey(key='a', fun=player.move_left)
is_game_on = True


while is_game_on:
    sleep(0.1)
    game_screen.update()
    for car in cars.all_cars:
        car.move_car()

        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() > 290:
        player.start_position()
        cars.increase_cars()
        scoreboard.level_up()


game_screen.exitonclick()
