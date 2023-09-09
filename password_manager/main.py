from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


FONT_NAME = "Courier"
FONT_SIZE = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    random_list = [choice(letters) for i in range(0, randint(8, 10))]
    random_list += [choice(symbols) for i in range(0, randint(2, 4))]
    random_list += [choice(numbers) for i in range(0, randint(2, 4))]
    shuffle(random_list)

    password = "".join(random_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # message box
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                           f"Email: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password_manager/data.txt", mode="a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
        else:
            pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas画布
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Lables
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_label.grid(column=0, row=3)

# Entrys
website_input = Entry(width=49)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=49)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "sherryuuer@gmail.com")
password_input = Entry(width=30)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
