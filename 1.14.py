from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")

# 함수 설정
def save_file():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                            filetypes=(("TXT files", "*.txt"), ("all files", "*.*")))
    # print(filename)
    if filename == '':
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(main_text.get("1.0", END))

def open_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          filetypes=(("TXT files", "*.txt"), ("all files", "*.*")))
    # print(filename)
    if filename == '':
        return
    with open(filename, "r", encoding="utf-8") as f:
        main_text.delete("1.0", END)
        lines = f.readlines()
        for line in lines:
            main_text.insert(END, line)

# 메뉴바
menu = Menu(root)

# 파일 메뉴
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=file_menu)

# 편집 메뉴
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=edit_menu)

# 서식 메뉴
form_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="포맷", menu=form_menu)

# 보기 메뉴
view_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=view_menu)

# 도움말 메뉴
help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말(H)", menu=help_menu)

root.config(menu=menu)

# 메모장
note_frame = Frame(root)
note_frame.pack(fill="both")

scrollbar_height = Scrollbar(note_frame)
scrollbar_height.pack(side="right", fill="y")

main_text = Text(note_frame, yscrollcommand=scrollbar_height.set)
main_text.pack(fill="x")
scrollbar_height.config(command=main_text.yview)

#
# def btn_start():
#     print("시작합니다.")
#
# label = Label(window, text="이것은 라벨입니다")
# label.pack()
# btn1 = Button(window, text="시작", command=btn_start)
# btn1.pack()
#
#
# frame_label = LabelFrame(window, text="라벨 프레임")
# frame_label.pack(fill="x")                          #x축으로 라벨 늘리기
# btn2 = Button(frame_label, text="btn1종료", command= window.quit)
# btn2.pack(side="left")

# 상태바
statusbar = Label(root, text="on the way…", bd=3)
statusbar.pack(side="bottom", fill="x")

root.mainloop()



