from tkinter import *
from tkinter.ttk import Progressbar
import sys
import AccountSystem
import os

root = Tk()
# root.resizable(0, 0)
image = PhotoImage(file='images\\coffeeShop-ico.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
# root.wm_attributes('-alpha', 0.9)
root.wm_attributes('-topmost', True)
root.config(background='#036553')

welcome_label = Label(text='WELCOME TO CHILL DRINK SHOP', bg='#036553', font=(
    "yu gothic ui", 15, "bold"), fg='white')
welcome_label.place(x=80, y=25)

bg_label = Label(root, image=image, bg='#036553')
bg_label.place(x=150, y=85)

progress_label = Label(root, text="Please Wait...", font=(
    'yu gothic ui', 13, 'bold'), fg='white', bg='#036553')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

exit_btn = Button(text='x', bg='#036553', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='#036553', fg='red')
exit_btn.place(x=490, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()


load()


load()
root.mainloop()
