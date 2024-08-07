import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

correct_answers_amount = 0
correct_guesses = []

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{correct_answers_amount}/50 States correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        answer_values = data[data["state"] == answer_state]

        print(answer_values)

        pos = (float(answer_values["x"].to_numpy()[0]), float(answer_values["y"].to_numpy()[0]))

        turtle_writer = turtle.Turtle()

        turtle_writer.hideturtle()
        turtle_writer.penup()
        turtle_writer.goto(pos)
        turtle_writer.write(answer_state, font=("Verdana", 8, "normal"))

        correct_answers_amount += 1

screen.exitonclick()
