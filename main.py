import turtle

import pandas

screen = turtle.Screen()
screen.title("States Name Game")
us_map = "blank_states_img.gif"
screen.addshape(us_map)
simon = turtle.Turtle()
simon.penup()
simon.hideturtle()
turtle.shape(us_map)

# counter for the game
ticker = 0

# data import
data = pandas.read_csv("50_states.csv")

game_on = True
correct_answers = []


def write_state(f_answer):
    """this function will write the state name on the map"""
    working_data = data[data.state == f"{f_answer}"]
    print(working_data)
    simon.goto(int(working_data.x), int(working_data.y))
    simon.write(f_answer)


while game_on:
    answer = screen.textinput(title=f"{ticker}/50 States Correct", prompt="Guess Another State")
    format_answer = answer.title()

    if format_answer == "Exit":
        break

    for state in data.state:
        if state == format_answer:
            print(state)
            ticker += 1
            correct_answers.append(state)
            write_state(format_answer)
    print(correct_answers)

    if ticker == 50:
        break

# below logic handles end of game behavior, either from success or typing exit
if ticker == 50:
    simon.goto(0, 0)
    simon.write("You WIN!")
else:
    missed = []
    for state in data.state.to_list():
        if state not in correct_answers:
            missed.append(state)
    missed_data = pandas.DataFrame(missed)
    missed_data.to_csv("need_to_learn.csv")

screen.exitonclick()

