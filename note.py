import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename

root = Tk()

def start_work(colorparam, frame_file_content):
    global file_content
    file_content = Text(frame_file_content, bg='white', fg='black', width='50', height='20', wrap=WORD, font='Times 10')
    return file_content

def edit_click():
    messagebox.showinfo("About", "кря")

def click_exit():
    sys.exit()

def open_file():
    file_name = fd.askopenfilename()
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

def save_file():

    file_name = asksaveasfilename()

    if file_name:
        f = open(file_name, 'a')
        contents = file_content.get(1.0, 'end')
        f.write(contents)
        f.close()

def savejust():
    file_name = fn
    f = open(file_name, 'w')
    contents = file_content.get(1.0, 'end')
    f.write(contents)
    f.close()

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="Save as...", command=save_file)

file_menu.add_command(label="Save", command=savejust)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=click_exit)

file_view = Menu()

file_view.add_command(label='light theme', command=lighttheme)
file_view.add_command(label='dark theme', command=darktheme)
file_view.add_command(label="break your eyes", command=strangetheme)
file_view.add_separator()
file_view.add_command(label="well done", command=welldone)
file_view.add_command(label="medium", command=medium)
file_view.add_command(label="rare", command=rare)

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