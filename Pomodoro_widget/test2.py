#Importing the library
from tkinter import *

#Create an instance of tkinter window or frame
win= Tk()

#Setting the geometry of window
win.geometry("600x350")

#Create a Label
Label(win, text= "Hello World! ",font=('Helvetica bold', 15)).pack(pady=20)

#Make the window jump above all
win.attributes('-topmost',True)

win.mainloop()

# https://www.tutorialspoint.com/how-to-put-a-tkinter-window-on-top-of-the-others
