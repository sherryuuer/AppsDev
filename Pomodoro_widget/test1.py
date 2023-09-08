# 创建弹出窗口
# 导入所需的库
from tkinter import *

# 创建Tkinter框架的实例
win = Tk()

# 设置窗口大小
win.geometry("700x250")
# win.wm_attributes('-topmost', 1)  # 锁定窗口顶置


def open_win():
# 创建用于打开Toplevel窗口的按钮
    top = Toplevel(win)
    top.geometry("700x250")
    top.title("子窗口")
    # 在Toplevel窗口中创建一个标签
    Label(top, text="Hello World!")


Label(win, text = "单击按钮以打开弹出窗口", font = ('Helvetica 18')).place(relx = .5, rely= .5, anchor = CENTER)
Button(win, text = "点击我", background = "white", foreground = "blue", font = ('Helvetica 13 bold'), command = open_win).pack(pady = 50)
win.mainloop()
