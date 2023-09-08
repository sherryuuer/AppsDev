from tkinter import *


def button_clicked():
    mile = input.get()
    result = int(mile) * 1.609344
    result_label.config(text=result)  # or text=f"{result}" to make it a string


window = Tk()
window.minsize()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# 4Label
equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=1)
result_label = Label(text="", font=("Arial", 10))
result_label.grid(column=1, row=1)
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)
km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

# Botton
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
