from tkinter import *


window = Tk()
window.minsize(width=500, height=300)
window.title("My First GUI Program")
window.config(padx=50, pady=50) # add space around sth

# Label
my_label = Label(text="I am a label.", font=("Arial", 18))
my_label.grid(column=0, row=0)  # use this to show the label.
my_label.config(padx=50, pady=50)

# config or change sth.
# my_label["text"] = "New text"
# my_label.config(text="New text")

# Botton
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="new button")
new_button.grid(column=2, row=0)


input = Entry(width=10)
input.grid(column=3, row=2)
# print(input.get())  # get method can get what you input.

# text spinbox checkbutton radiobutton listbox scale

window.mainloop()


"""
pack, place, grid：
pack順番にものを配置する、簡単、シンプル
place位置を指定できる(X,Y)、使いにくい、位置設定がむず
grid(column,row)ものの相関位置を指定できる、よく使う
三種類一緒に使うことができない
"""
