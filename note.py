import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
from tkinter import messagebox

root = Tk()


def start_work(colorparam, frame_file_content):
    global file_content
    file_content = Text(frame_file_content, bg='white', fg='black', width='50', height='20', wrap=WORD, font='Times 10')
    return file_content


def edit_click():
    messagebox.showinfo("About", "кря")


def click_exit():
    if fn == 'nullnemesorry':
        MsgBox = tkinter.messagebox.askquestion('?????', 'Сохранить файл?',
                                                icon='question')
        if MsgBox == 'yes':
            save_as()
    sys.exit()


def open_file():
    file_name = fd.askopenfilename(defaultextension=".txt")
    f = open(file_name)
    insert_text(f)
    global fn
    fn = file_name


def insert_text(text):
    file_content.delete(1.0, END)
    file_content.insert(1.0, text.read())


def lighttheme():
    file_content.config(bg='white', fg='black')


def darktheme():
    file_content.config(bg='black', fg='white')


def strangetheme():
    file_content.config(bg='green', fg='yellow')


def welldone():
    file_content.config(font='Times 20')


def medium():
    file_content.config(font='Times 10')


def rare():
    file_content.config(font='Times 5')


def white():
    file_content.config(bg='white')


def grey():
    file_content.config(bg='grey')


def pink():
    file_content.config(bg='pink')


def other():
    clr = colorchooser.askcolor(title='Выберите цвет')
    file_content.configure(background=clr[1])


def save_as():
    file_name = asksaveasfilename(defaultextension=".txt")
    if file_name:
        f = open(file_name, 'a')
        contents = file_content.get(1.0, 'end')
        f.write(contents)
        f.close()
        global fn
        fn = file_name


def save_open():
    file_name = fn
    print(fn)
    if fn == 'nullnemesorry':
        save_as()
    else:
        f = open(file_name, 'w')
        contents = file_content.get(1.0, 'end')
        f.write(contents)
        f.close()


def create():
    if fn == 'nullnemesorry':
        MsgBox = tkinter.messagebox.askquestion('?????', 'Сохранить файл?',
                                                icon='question')
        if MsgBox == 'yes':
            save_as()
    file_content.delete(1.0, END)


fn = 'nullnemesorry'
main_menu = Menu()

file_menu = Menu()

file_menu.add_command(label="Create", command=create)

file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="Save as...", command=save_as)

file_menu.add_command(label="Save", command=save_open)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=click_exit)

file_view = Menu()

theme = Menu()

file_view.add_cascade(label='Theme', menu=theme)
theme.add_radiobutton(label='Light theme', command=lighttheme)
theme.add_radiobutton(label='Dark theme', command=darktheme)
theme.add_radiobutton(label="Break your eyes", command=strangetheme)

color_bg = Menu()

file_view.add_cascade(label="Background", menu=color_bg)
color_bg.add_radiobutton(label="White", command=white)
color_bg.add_radiobutton(label="Grey", command=grey)
color_bg.add_radiobutton(label="Pink", command=pink)
color_bg.add_radiobutton(label="Other", command=other)

file_view.add_separator()

size = Menu()

file_view.add_cascade(label="Size", menu=size)
size.add_command(label="Well done", command=welldone)
size.add_command(label="Medium", command=medium)
size.add_command(label="Rare", command=rare)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="View", menu=file_view)
main_menu.add_cascade(label="About", command=edit_click)

root.config(menu=main_menu)

root.title('NOTE by Sergeev')

frame = Frame()
frame_file_content = Frame()
colorparam = 0
file_content = start_work(colorparam, frame_file_content)

Yscroll = Scrollbar(frame_file_content, command=file_content.yview)
Xscroll = Scrollbar(orient=HORIZONTAL, command=file_content.xview)
file_content.configure(yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set)
frame.pack()
frame_file_content.pack(fill=BOTH, expand=1)
file_content.pack(side=LEFT, fill=BOTH, expand=1)
Yscroll.pack(side=LEFT, fill=Y)
Xscroll.pack(side=BOTTOM, fill=X)

root.mainloop()
