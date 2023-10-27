from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import Employee
import AccountSystem


class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(
            f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        dashboard_window.resizable(False, False)
        # window Icon
        icon = PhotoImage(file='images\\replace_this.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        logoIcon = Image.open('images\\replace_this.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(homepage, image=photo)
        logo.image = photo
        logo.place(x=0, y=0)

        menuBar_line = Canvas(homepage, width=1500,
                              height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        admIcon = Image.open('images\\feeling.png')
        photo = ImageTk.PhotoImage(admIcon)
        adm = Label(homepage, image=photo, bg='#ffffff')
        adm.image = photo
        adm.place(x=1280, y=5)

        admLabel = Label(homepage, text='ADMIN', font=(
            'yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#ffffff')
        admLabel.place(x=1180, y=11)

        home_bgImg = Image.open('images\\whisk.jpg')
        photo = ImageTk.PhotoImage(home_bgImg, width=500, height=200)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

        # brandIcon = Image.open('images\\replace_this.png')
        # photo = ImageTk.PhotoImage(brandIcon)
        # brandlogo = Label(homepage, image=photo, bg='black')
        # brandlogo.image = photo
        # brandlogo.place(x=1085, y=83)

        # heading = Label(homepage, text='DRINK BAR',fg='#036553', font=("yu gothic ui", 19, "bold"))
        # heading.place(x=770, y=90)

        heading2 = Label(homepage, text='Trending',
                         fg='#036553', font=("", 19, "bold"))
        heading2.place(x=150, y=95)

        # Coffee Image
        coffeeImage = Image.open('images\\menu-6.png')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffeeImg = Label(homepage, image=photo)
        coffeeImg.image = photo
        coffeeImg.place(x=50, y=150)

        coffeeImage2 = Image.open('images\\menu-5.png')
        photo = ImageTk.PhotoImage(coffeeImage2)
        coffeeImg2 = Label(homepage, image=photo)
        coffeeImg2.image = photo
        coffeeImg2.place(x=180, y=150)

        coffeeImage3 = Image.open('images\\menu-4.png')
        photo = ImageTk.PhotoImage(coffeeImage3)
        coffeeImg3 = Label(homepage, image=photo)
        coffeeImg3.image = photo
        coffeeImg3.place(x=310, y=150)

        coffeeImage4 = Image.open('images\\menu-3.png')
        photo = ImageTk.PhotoImage(coffeeImage4)
        coffeeImg4 = Label(homepage, image=photo)
        coffeeImg4.image = photo
        coffeeImg4.place(x=50, y=300)

        coffeeImage5 = Image.open('images\\menu-2.png')
        photo = ImageTk.PhotoImage(coffeeImage5)
        coffeeImg5 = Label(homepage, image=photo)
        coffeeImg5.image = photo
        coffeeImg5.place(x=180, y=300)

        coffeeImage6 = Image.open('images\\menu-1.png')
        photo = ImageTk.PhotoImage(coffeeImage6)
        coffeeImg6 = Label(homepage, image=photo)
        coffeeImg6.image = photo
        coffeeImg6.place(x=310, y=300)

        heading3 = Label(homepage, text='TEQUILA', font=("", 11, "bold"))
        heading3.place(x=50, y=245)

        heading4 = Label(homepage, text='MARGARITA', font=("", 11, "bold"))
        heading4.place(x=175, y=245)

        heading5 = Label(homepage, text='LIGHT BEER', font=("", 11, "bold"))
        heading5.place(x=310, y=245)

        heading6 = Label(homepage, text="PINA COLADA", font=("", 11, "bold"))
        heading6.place(x=40, y=400)

        heading7 = Label(homepage, text='LONG ICELAND', font=("", 11, "bold"))
        heading7.place(x=167, y=400)

        heading8 = Label(homepage, text='DIRTY MARTINI', font=("", 11, "bold"))
        heading8.place(x=305, y=400)

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#036553', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#036553', activeforeground='white')
        home_button.place(x=70, y=15)

        def manage():
            dashboard_window.withdraw()
            os.system("python admin.py")
            dashboard_window.destroy()

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#036553', activeforeground='white',
                               command=manage)
        manage_button.place(x=150, y=15)

        # ========== PRODUCTS BUTTON =======
        # product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
        #                         cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
        #                         command=manage)
        # product_button.place(x=250, y=15)

        # ========== HELP BUTTON =======

        def help():
            win = Toplevel()
            window_width = 1366
            window_height = 768
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(
                f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Forgot Password')
            # win.configure(background=('images/hel'))
            win.resizable(0, 0)

            # Coffee Image
            bgImage = Image.open('images\\help.png')
            photo = ImageTk.PhotoImage(bgImage)
            Img = Label(win, image=photo)
            Img.image = photo
            Img.place(x=0, y=0)

        # help_button = Button(homepage, text='Help', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
        #                      cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=help)
        # help_button.place(x=360, y=15)

        def logout():
            win = Toplevel()
            AccountSystem.AccountPage(win)
            dashboard_window.withdraw()
            win.deiconify()
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=250, y=15)


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
