import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < len(states):
    user_answer = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct",
                                   prompt="What's another state's name?").title()

    if user_answer == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_answer in states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(user_answer)

