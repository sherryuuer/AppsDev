# my thinking memo:(after thinking I made my own main.py and saw the video and write Angela's answer here)
# 1,convert the guess to title case.
# correct_ans_num = 0
# correct_ans_num += 1
# user_answer = screen.textinput(title=f"{correct_ans_num}/50 States Correct",
#                                prompt="What's another state's name?").lower()

# 2,chect if the guess is among the 50 states.

# 3,write correct guesses onto the map.

# 4,use a loop to allow the user to keep guessing.
# is_game_on = True
# while is_game_on:

# 5,record the correct guesses in a list.
# correct_guess = []
# if user_answer in answer_list and user_answer not in correct_guess:
#     correct_guess.append(user_answer)

# 6,keep track of the score.
# if correct_ans_num == 50:


import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "UsStatesGame_day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("UsStatesGame_day25/50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() 
    if answer_state == "Exit":
        # use list's one line code
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("UsStatesGame_day25/missing_states_list.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # state_data.state.item() also works.


# # Save the missing states to a .csv.
# data_to_save = data[~data["state"].isin(guessed_states)]
# data_to_save.to_csv("UsStatesGame_day25/missing_states.csv")
