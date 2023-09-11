from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
# read the wrods from the csv file.
try:
    data = pd.read_csv("Flash_Card_Project/data/english_words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("Flash_Card_Project/data/english_words.csv")
finally:
    word_dict = data.to_dict(orient="records")

# angela's version:(I think they works the same,but this however seems better.)
# word_dict = {}
# try:
#     data = pd.read_csv("Flash_Card_Project/data/english_words_to_learn.csv")
# except FileNotFoundError:
#     data = pd.read_csv("Flash_Card_Project/data/english_words.csv")
#     word_dict = data.to_dict(orient="records")
# else:
#     word_dict = data.to_dict(orient="records")


# 3sec flash the card, used in the function-next_card
def flip_card():
    canvas.itemconfig(canvas_background, image=card_back_img)
    canvas.itemconfig(title_text, text="Chinese", fill="white")
    canvas.itemconfig(word_text, text=current_word["Chinese"], fill="white")


# next_card function
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_word["English"], fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def known_card():   
    word_dict.remove(current_word)
    # print(len(word_dict)) # can see the list is become shorter and shorter.
    pd.DataFrame(word_dict).to_csv("Flash_Card_Project/data/english_words_to_learn.csv", index=False)
    next_card()


# UI setup
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card) # flip the card after 3000ms,can not use time.sleep()

# canvas画布
canvas = Canvas(width=820, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Flash_Card_Project/images/card_front.png")
card_back_img = PhotoImage(file="Flash_Card_Project/images/card_back.png")
canvas_background = canvas.create_image(410, 270, image=card_front_img)
title_text = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 270, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="Flash_Card_Project/images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="Flash_Card_Project/images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
