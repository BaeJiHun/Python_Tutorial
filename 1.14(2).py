# tkinter 가지고놀기
from tkinter import *

def OK():
    print("OK")

def Hi():
    print("안녕하세요")


window = Tk()
window.title("TK연습")
label = Label(window, text="안녕하세요" )
frame = Frame(window)
bt1 = Button(window, text="OK버튼.", command=OK)
bt2 =Button(window, text="Hi버튼.", command=Hi)
frame.pack()
label.pack()
bt1.pack()
bt2.pack()

window.mainloop()

