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
missing_states = data

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{correct_answers_amount}/50 States correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        print("EXIT")
        break

    if answer_state in states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        answer_values = data[data["state"] == answer_state]

        pos = (float(answer_values["x"].to_numpy()[0]), float(answer_values["y"].to_numpy()[0]))

        turtle_writer = turtle.Turtle()

        turtle_writer.hideturtle()
        turtle_writer.penup()
        turtle_writer.goto(pos)
        turtle_writer.write(answer_state, font=("Verdana", 8, "normal"))

        correct_answers_amount += 1

    for guess in correct_guesses:
        missing_states = missing_states.drop(missing_states[missing_states["state"] == guess].index)

    missing_states.to_csv("./missing_states.csv")

screen.exitonclick()

# TODO:
# 1. Convert the guess to Title case
# 2. Check if the guess is among the 50 states
# 3. Write correct guesses onto the map
# 4. Use a loop to allow the user to keep guessing
# 5. Record the correct guesses in a list
# 6. Keep track of the score
# 7. Make csv file with all missing states
