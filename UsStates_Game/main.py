import turtle
import pandas as pd


def write_answer(user_answer):
    """When user guess the right answer, write it on the map."""
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    state_name = user_answer.capitalize()
    state_cor = answer_list[state_name]
    pen.goto(state_cor)
    pen.write(state_name, align="left", font=('Arial', 8, 'normal'))


def get_input(message):
    """Ask the user the question, and get the user's answer."""
    return screen.textinput(title=message, prompt="What's another state's name?")


screen = turtle.Screen()
screen.title("US States Game")
image = "UsStates_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


correct_answer = []
states_data = pd.read_csv("UsStates_Game/50_states.csv")
states_dict = states_data.to_dict("split")
answer_list = {}
for state in states_dict["data"]:
    answer_list[state[0]] = (state[1], state[2])
states_number = len(answer_list)


is_game_on = True
user_answer = get_input("Guess the States")
while is_game_on:
    if user_answer.capitalize() in answer_list and user_answer.capitalize() not in correct_answer:
        correct_answer.append(user_answer.capitalize())
        write_answer(user_answer=user_answer)
        if len(correct_answer) == states_number:
            is_game_on = False
            screen.exitonclick()
        else:
            user_answer = get_input(f"{len(correct_answer)}/{states_number} States Correct")
    else:
        user_answer = get_input(f"{len(correct_answer)}/{states_number} States Correct")
 