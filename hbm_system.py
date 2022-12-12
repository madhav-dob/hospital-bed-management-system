import gspread
from tkinter import *
#from PIL import ImageFont
import pyautogui

#title_font = ImageFont.truetype('NoToSerif-Bold.ttf', 25)

# google sheets setup
sa = gspread.service_account(filename="E:/arjun/hospital system/service_account.json")
sheet = sa.open("hospital_database")
wks = sheet.worksheet("Sheet1")
wks2 = sheet.worksheet("Sheet2")

user_name = ''


def bed_display(n, p):
    bed_status = wks.col_values(2)

    bed1 = n
    bed2 = p

    y = 0
    x = ((len(wks.col_values(1)) // 7) * 2) + 2
    for i in range(2, x, 2):
        for j in range(7):
            if bed_status[y] == '1':
                Label(icon_grid, image=bed2, bd=0, padx=0, pady=0).grid(row=i + 1, column=j)
                Label(icon_grid, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0,
                      pady=0).grid(row=i + 2,
                                   column=j)
            elif bed_status[y] == '0':
                Label(icon_grid, image=bed1, bd=0, padx=0, pady=0).grid(row=i + 1, column=j)
                Label(icon_grid, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0,
                      pady=0).grid(row=i + 2,
                                   column=j)
            y += 1

    for m in range(len(wks.col_values(1)) % 7):
        if bed_status[y] == '1':
            Label(icon_grid, image=bed2, bd=0, padx=0, pady=0).grid(row=x + 1, column=m)
            Label(icon_grid, text='Room ' + str(y + 1), font=('verdana', 11), bg='white', bd=0, padx=0, pady=0).grid(
                row=x + 2,
                column=m)
        elif bed_status[y] == '0':
            Label(icon_grid, image=bed1, bd=0, padx=0, pady=0).grid(row=x + 1, column=m)
            Label(icon_grid, text='Room ' + str(y + 1), font=('verdana', 11), bg='white', bd=0, padx=0, pady=0).grid(
                row=x + 2,
                column=m)
        y += 1


def bed_display2(n, p):
    bed_status = wks.col_values(2)

    btns = []
    bed1 = n
    bed2 = p

    y = 0
    x = ((len(wks.col_values(1)) // 7) * 2) + 2
    for i in range(2, x, 2):
        for j in range(7):
            if bed_status[y] == '1':
                b = Button(icon_grid2, image=bed2, highlightthickness=0, bd=0, cursor='hand2',
                           command=lambda r=y: update(r + 1), padx=0, pady=0)
                b.grid(row=i + 1, column=j)
                btns.append(b)
                Label(icon_grid2, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0,
                      pady=0).grid(row=i + 2,
                                   column=j)
            elif bed_status[y] == '0':
                b = Button(icon_grid2, image=bed1, highlightthickness=0, bd=0, cursor='hand2',
                           command=lambda r=y: update(r + 1), padx=0, pady=0)
                b.grid(row=i + 1, column=j)
                btns.append(b)
                Label(icon_grid2, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0,
                      pady=0).grid(row=i + 2,
                                   column=j)
            y += 1

    for m in range(len(wks.col_values(1)) % 7):
        if bed_status[y] == '1':
            b = Button(icon_grid2, image=bed2, highlightthickness=0, bd=0, cursor='hand2', padx=0,
                       command=lambda y=y: update(y + 1), pady=0)
            b.grid(row=x + 1, column=m)
            btns.append(b)
            Label(icon_grid2, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0, pady=0).grid(
                row=x + 2,
                column=m)
        elif bed_status[y] == '0':
            b = Button(icon_grid2, image=bed1, highlightthickness=0, bd=0, cursor='hand2', padx=0,
                       command=lambda y=y: update(y + 1), pady=0)
            b.grid(row=x + 1, column=m)
            btns.append(b)
            Label(icon_grid2, text='Room ' + str(y + 1), font=('verdana', 11), bd=0, bg='white', padx=0, pady=0).grid(
                row=x + 2,
                column=m)
        y += 1


def head():
    global button_frame
    global icon_grid
    global window

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry("%dx%d" % (width, height))
    window.configure(bg='white')

    window.title('hospital bed management system')
    button_frame = Frame(window, bg='#545454', width=250, height=715)
    button_frame.pack(side='left')

    icon_grid = Frame(window, bg='white', width=1116, height=715)
    icon_grid.pack(side='right', anchor='n')

    # importing photos
    logo = PhotoImage(file="E:/arjun/hospital system/logo.png")
    blank = PhotoImage(file="E:/arjun/hospital system/blank.png")
    acc_logo = PhotoImage(file="E:/arjun/hospital system/4.png")
    # acc_logo2 = PhotoImage(file="E:/arjun/hospital system/5.png")
    account = PhotoImage(file="E:/arjun/hospital system/1.png")
    about = PhotoImage(file="E:/arjun/hospital system/2.png")
    contact_us = PhotoImage(file="E:/arjun/hospital system/3.png")
    about_logo = PhotoImage(file="E:/arjun/hospital system/8.png")
    # about_logo2 = PhotoImage(file="E:/arjun/hospital system/9.png")
    contact_logo = PhotoImage(file="E:/arjun/hospital system/7.png")
    # contact_logo2 = PhotoImage(file="E:/arjun/hospital system/6.png")
    mtl_logo = PhotoImage(file="E:/arjun/hospital system/18.png")
    main_banner = PhotoImage(file="E:/arjun/hospital system/27.png")
    bed1 = PhotoImage(file="E:/arjun/hospital system/31.png")
    bed2 = PhotoImage(file="E:/arjun/hospital system/32.png")
    refresh = PhotoImage(file="E:/arjun/hospital system/30.png")

    Label(button_frame, image=logo, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=2)
    Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=2, column=0, columnspan=2)
    Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=6, column=0, columnspan=2)
    Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=7, column=0, columnspan=2)
    Label(button_frame, image=mtl_logo, padx=0, pady=0, bd=0).grid(row=8, column=0, columnspan=2)
    Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=9, column=0, columnspan=2)
    Label(button_frame, image=acc_logo, highlightthickness=0, bd=0).grid(row=3, column=0, padx=0, pady=0)
    button1 = Button(button_frame, image=account, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [login()])
    button1.grid(row=3, column=1, padx=0, pady=0)
    Label(button_frame, image=about_logo, highlightthickness=0, bd=0).grid(row=4, column=0, padx=0, pady=0)
    button2 = Button(button_frame, image=about, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [about_win(window, button_frame)])
    button2.grid(row=4, column=1, padx=0, pady=0)
    Label(button_frame, image=contact_logo, highlightthickness=0, bd=0).grid(row=5, column=0, padx=0, pady=0)
    button3 = Button(button_frame, image=contact_us, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [contact_win(window, button_frame)])
    button3.grid(row=5, column=1, padx=0, pady=0)
    Label(icon_grid, image=main_banner, width=1116, padx=0, pady=10, bd=0).grid(row=0, column=0, columnspan=7)
    Button(icon_grid, image=refresh, cursor="hand2", highlightthickness=0, bd=0,
           command=lambda: [bed_display(bed1, bed2)]).grid(row=1, column=5, columnspan=2)
    bed_display(bed1, bed2)

    window.mainloop()


def admin():
    window.destroy()
    global icon_grid2
    global button_frame2
    global window2

    window2 = Tk()
    window2.geometry("{0}x{1}+0+0".format(window2.winfo_screenwidth(), window2.winfo_screenheight()))
    window2.configure(bg='white')
    window2.title('hospital bed management system')

    button_frame2 = Frame(window2, bg='#545454', width=250, height=715)
    button_frame2.pack(side='left', anchor='n')

    icon_grid2 = Frame(window2, bg='white', width=1116, height=715)
    icon_grid2.pack(side='right', anchor='n')

    logo = PhotoImage(file="E:/arjun/hospital system/logo.png")
    blank = PhotoImage(file="E:/arjun/hospital system/blank.png")
    acc_logo = PhotoImage(file="E:/arjun/hospital system/4.png")
    # acc_logo2 = PhotoImage(file="E:/arjun/hospital system/5.png")
    account = PhotoImage(file="E:/arjun/hospital system/1.png")
    about = PhotoImage(file="E:/arjun/hospital system/2.png")
    contact_us = PhotoImage(file="E:/arjun/hospital system/3.png")
    mtl_logo = PhotoImage(file="E:/arjun/hospital system/18.png")
    about_logo = PhotoImage(file="E:/arjun/hospital system/8.png")
    # about_logo2 = PhotoImage(file="E:/arjun/hospital system/9.png")
    contact_logo = PhotoImage(file="E:/arjun/hospital system/7.png")
    # contact_logo2 = PhotoImage(file="E:/arjun/hospital system/6.png")
    main_banner = PhotoImage(file="E:/arjun/hospital system/27.png")
    bed1 = PhotoImage(file="E:/arjun/hospital system/31.png")
    bed2 = PhotoImage(file="E:/arjun/hospital system/32.png")

    Label(icon_grid2, image=main_banner, padx=0, width=1116, pady=0, bd=0).grid(row=0, column=0, columnspan=7)
    Label(button_frame2, image=logo, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=2, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=6, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=7, column=0, columnspan=2)
    Label(button_frame2, image=mtl_logo, padx=0, pady=0, bd=0).grid(row=8, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=9, column=0, columnspan=2)
    Button(button_frame2, image=acc_logo, highlightthickness=0, bd=0).grid(row=3, column=0, padx=0, pady=0)
    btn1 = Button(button_frame2, image=account, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [my_self()])
    btn1.grid(row=3, column=1, padx=0, pady=0)
    Label(button_frame2, image=about_logo, highlightthickness=0, bd=0).grid(row=4, column=0, padx=0, pady=0)
    btn2 = Button(button_frame2, image=about, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [about_win(window2, button_frame2)])
    btn2.grid(row=4, column=1, padx=0, pady=0)
    Label(button_frame2, image=contact_logo, highlightthickness=0, bd=0).grid(row=5, column=0, padx=0, pady=0)
    btn3 = Button(button_frame2, image=contact_us, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [contact_win(window2, button_frame2)])
    btn3.grid(row=5, column=1, padx=0, pady=0)
    bed_display2(bed1, bed2)
    window2.mainloop()


def display_logo(n, m, p):
    Label(p, image=m, padx=0, pady=0, bd=0).grid(row=n, column=0)


def close():
    pass


def login():
    global window

    def login_final():

        def close():
            error.destroy()
            entry1.config(fg='black')
            entry2.config(fg='black')

        global user_name
        entry1.config(fg='black')
        entry2.config(fg='black')
        u = user.get()
        p = password.get()
        if u in users:
            index = users.index(u)

            if passwords[index] == p:
                print("values matched")
                user_name = u
                admin()
            else:
                entry2.config(fg='red')
                error = Toplevel(main)
                error.title("Error")
                error.geometry('250x150+500+400')
                error.config(bg='#F4AB90')
                error.protocol("WM_DELETE_WINDOW", close)
                error.resizable(0, 0)
                Label(error, text='WRONG', image=wrn1, bd=0).pack()


        else:
            entry1.config(fg='red')
            error = Toplevel(main)
            error.title("Error")
            error.geometry('250x150+500+400')
            error.config(bg='#F4AB90')
            error.protocol("WM_DELETE_WINDOW", close)
            error.resizable(0, 0)
            Label(error, text='WRONG', image=wrn2, bd=0).pack()


    users = wks2.col_values(1)
    passwords = wks2.col_values(2)
    password = StringVar()
    user = StringVar()

    main = Toplevel(window)
    main.geometry('650x500+260+133')
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)

    banner_login = PhotoImage(file="E:/arjun/hospital system/10.png")
    arrow = PhotoImage(file="E:/arjun/hospital system/17.png")
    user_pass = PhotoImage(file="E:/arjun/hospital system/12.png")
    close_button = PhotoImage(file="E:/arjun/hospital system/13.png")
    login_btn = PhotoImage(file="E:/arjun/hospital system/14.png")
    grad = PhotoImage(file="E:/arjun/hospital system/15.png")
    wrn2 = PhotoImage(file="E:/arjun/hospital system/22.png")
    wrn1 = PhotoImage(file="E:/arjun/hospital system/26.png")
    acc_logo2 = PhotoImage(file="E:/arjun/hospital system/33.png")
    acc_logo = PhotoImage(file="E:/arjun/hospital system/4.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='left', anchor='n')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), display_logo(3, acc_logo, button_frame)]).grid(row=0,
                                                                                           column=1)
    Label(entry_frame, image=arrow, padx=0, pady=0, bd=0).grid(row=1, column=0)
    Label(entry_frame, image=grad, padx=0, pady=0, bd=0).grid(row=4, column=0, rowspan=2)

    Label(entry_frame, image=user_pass, padx=0, pady=0, bd=0).grid(row=2, column=0, rowspan=2)
    entry1 = Entry(entry_frame, text=user, width=12, font=('verdana', 25), fg='black', bg='white')
    entry1.grid(row=2, column=1)

    entry2 = Entry(entry_frame, text=password, width=12, show="*", fg='black', font=('verdana', 25), bg='white')
    entry2.grid(row=3, column=1)

    Button(entry_frame, image=login_btn, cursor='hand2', width=200, height=60, highlightthickness=0, bd=0,
           command=lambda: [login_final()]).grid(padx=4, row=4, column=1)
    display_logo(3, acc_logo2, button_frame)
    main.mainloop()


def my_self():
    global button_frame2
    global user_name

    main = Toplevel(window2)
    main.geometry('650x500+260+133')
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)

    banner_login = PhotoImage(file="E:/arjun/hospital system/19.png")
    arrow = PhotoImage(file="E:/arjun/hospital system/17.png")
    close_button = PhotoImage(file="E:/arjun/hospital system/13.png")
    grad = PhotoImage(file="E:/arjun/hospital system/15.png")
    hello = PhotoImage(file="E:/arjun/hospital system/20.png")
    face = PhotoImage(file="E:/arjun/hospital system/23.png")
    logout_btn = PhotoImage(file="E:/arjun/hospital system/24.png")
    logout_btn2 = PhotoImage(file="E:/arjun/hospital system/25.png")
    acc_logo2 = PhotoImage(file="E:/arjun/hospital system/33.png")
    acc_logo = PhotoImage(file="E:/arjun/hospital system/4.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), display_logo(3, acc_logo, button_frame2)]).grid(row=0,
                                                                                            column=1,
                                                                                            columnspan=2)

    Label(entry_frame, text="       " + user_name, bg='#D1D1D1', font=('verdana', 27), bd=0).grid(row=3, column=0)
    Label(entry_frame, image=hello, bd=0).grid(row=2, column=0)
    Label(entry_frame, image=face, bd=0).grid(row=2, column=1, rowspan=2, columnspan=2)
    Label(entry_frame, image=arrow, padx=0, pady=0, bd=0).grid(row=1, column=0)
    Button(entry_frame, image=logout_btn, padx=0, pady=0, highlightthickness=0,
           command=lambda: [main.destroy(), window2.destroy(), head()],
           bd=0, cursor='hand2').grid(row=5, column=2)
    Label(entry_frame, image=logout_btn2, padx=0, pady=0, bd=0).grid(row=5, column=1)
    Label(entry_frame, image=grad, padx=0, pady=0, bd=0).grid(row=4, column=0, rowspan=2)
    display_logo(3, acc_logo2, button_frame2)
    main.mainloop()


def update(m):
    def change(j):

        if c[j - 1] == '1':
            wks.update_cell(j, 2, '0')
        elif c[j - 1] == '0':
            wks.update_cell(j, 2, '1')
        bed_display2(bed1, bed2)
        root.destroy()

    bed1 = PhotoImage(file="E:/arjun/hospital system/31.png")
    bed2 = PhotoImage(file="E:/arjun/hospital system/32.png")
    x, y = pyautogui.position()
    pos = '220x280+' + str(x) + '+' + str(y)
    c = wks.col_values(2)
    root = Tk()
    root.geometry(pos)

    # root.overrideredirect(True)
    Label(root, text='Room ' + str(m)).pack()
    btn = Button(root, text='Change Status', command=lambda: [change(m)])
    btn.pack()

    root.mainloop()


def about_win(win, frm):
    main = Toplevel(win)
    main.geometry('650x500+260+133')
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)

    banner_login = PhotoImage(file="E:/arjun/hospital system/34.png")
    blank = PhotoImage(file="E:/arjun/hospital system/38.png")
    close_button = PhotoImage(file="E:/arjun/hospital system/37.png")
    about_logo = PhotoImage(file="E:/arjun/hospital system/8.png")
    about_logo2 = PhotoImage(file="E:/arjun/hospital system/9.png")
    main_pic = PhotoImage(file="E:/arjun/hospital system/40.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Label(entry_frame, image=blank, padx=0, pady=0, bd=0).grid(row=0, column=1)
    Label(entry_frame, image=main_pic, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=3)

    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), display_logo(4, about_logo, frm)]).grid(row=0, column=2)

    display_logo(4, about_logo2, frm)
    main.mainloop()


def contact_win(win, frm):
    main = Toplevel(win)
    main.geometry('650x500+260+133')
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)
    banner_login = PhotoImage(file="E:/arjun/hospital system/35.png")
    close_button = PhotoImage(file="E:/arjun/hospital system/37.png")
    blank = PhotoImage(file="E:/arjun/hospital system/38.png")
    contact_logo = PhotoImage(file="E:/arjun/hospital system/7.png")
    contact_logo2 = PhotoImage(file="E:/arjun/hospital system/6.png")
    main_pic = PhotoImage(file="E:/arjun/hospital system/36.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Label(entry_frame, image=main_pic, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=3)
    Label(entry_frame, image=blank, padx=0, pady=0, bd=0).grid(row=0, column=1)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), display_logo(5, contact_logo, frm)]).grid(row=0, column=2)

    display_logo(5, contact_logo2, frm)
    main.mainloop()


head()
