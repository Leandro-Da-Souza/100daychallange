from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = [
    'red',
    'green',
    'blue',
    'yellow',
    'purple',
    'orange'
]

turtles = []


def make_turtle(not_yet_turtle: str):
    new_turtle = vars()[not_yet_turtle] = Turtle('turtle')
    new_turtle.color(not_yet_turtle)
    return new_turtle


def move_to_start(combatant: Turtle, y_pos: int):
    combatant.penup()
    combatant.goto(x=-240, y=y_pos)


start_y = 0

for x in colors:
    turtles.append(make_turtle(x))

for turtle in turtles:
    move_to_start(turtle, start_y)
    start_y += 30


def race():
    is_on = True
    winner = None

    while is_on:
        for z in turtles:
            z.forward(randint(10, 20))
            if z.xcor() >= ((screen.window_width() / 2) - 20):
                winner = z.pencolor()
                is_on = False
    return winner


winning_turtle = race()

print(f"Winner is {winning_turtle}")
if user_bet.lower() == winning_turtle.lower():
    print('You guessed it! Good job!')
else:
    print('You guessed wrong. Bad job.')

screen.exitonclick()
