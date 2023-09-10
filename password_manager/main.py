from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # message box
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                           f"Email: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("password_manager/data.json", mode="r") as f:
                    # Reading the old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("password_manager/data.json", mode="w") as f:
                    json.dump(new_data, f, indent=4) 
            else:
                # Updating old data with new data
                data.update(new_data)
                # Saving updated data
                with open("password_manager/data.json", mode="w") as f:
                    json.dump(data, f, indent=4) 
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
        else:
            pass


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_input.get()
    try:
        with open("password_manager/data.json", mode="r") as f:
            # Reading the data
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No data file found.")
    else:
        # Search the key
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Oops!", message=f"No details for {website} exsits.")
        # when you can use if-else,then use it.If you can not easily handle with some error.then use try-except.


    # # do by myself.this works well too.But I use try-except too much.
    # website = website_input.get()
    # try:
    #     with open("password_manager/data.json", mode="r") as f:
    #         # Reading the data
    #         data = json.load(f)
    #         # Search the key
    #         try:
    #             email = data[website]["email"]
    #             password = data[website]["password"]
    #             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    #             pyperclip.copy(password)
    #         except KeyError:
    #             messagebox.showerror(title="Oops!", message="No details for the website.")
    # except FileNotFoundError:
    #     messagebox.showerror(title="Oops!", message="No data file found.")

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
website_input = Entry(width=30)
website_input.grid(row=1, column=1)
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
search_button = Button(text=" Search Password ", command=search_password)  # width=xx is ok
search_button.grid(column=2, row=1)

window.mainloop()
