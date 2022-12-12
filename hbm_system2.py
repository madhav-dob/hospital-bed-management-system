import gspread
from tkinter import *

# google sheets setup
sa = gspread.service_account(filename="service_account.json")
sheet = sa.open("hospital_database")
wks = sheet.worksheet("Sheet1")
wks2 = sheet.worksheet("Sheet2")
# tkinter setup
window = Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth() - 50, window.winfo_screenheight() - 50))
window.configure(bg='white')
window.title('hospital bed management system')

button_frame = Frame(window, bg='#545454', width=250, height=715)
button_frame.pack(side='left')

# importing photos
logo = PhotoImage(file="logo.png")
blank = PhotoImage(file="blank.png")
acc_logo = PhotoImage(file="4.png")
acc_logo2 = PhotoImage(file="5.png")
account = PhotoImage(file="1.png")
about = PhotoImage(file="2.png")
contact_us = PhotoImage(file="3.png")
about_logo = PhotoImage(file="8.png")
about_logo2 = PhotoImage(file="9.png")
contact_logo = PhotoImage(file="7.png")
contact_logo2 = PhotoImage(file="6.png")

Label(button_frame, image=logo, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=2)
Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=2, column=0, columnspan=2)
Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=6, column=0, columnspan=2)
Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=7, column=0, columnspan=2)
Label(button_frame, image=blank, padx=0, pady=0, bd=0).grid(row=8, column=0, columnspan=2)
Label(button_frame, image=acc_logo, highlightthickness=0, bd=0).grid(row=3, column=0, padx=0, pady=0)
button1 = Button(button_frame, image=account, cursor="hand2", highlightthickness=0, bd=0,
                 command=lambda: [display_logo(3, acc_logo2), login()])
button1.grid(row=3, column=1, padx=0, pady=0)
Label(button_frame, image=about_logo, highlightthickness=0, bd=0).grid(row=4, column=0, padx=0, pady=0)
button2 = Button(button_frame, image=about, cursor="hand2", highlightthickness=0, bd=0,
                 command=lambda: [display_logo(4, about_logo2)])
button2.grid(row=4, column=1, padx=0, pady=0)
Label(button_frame, image=contact_logo, highlightthickness=0, bd=0).grid(row=5, column=0, padx=0, pady=0)
button3 = Button(button_frame, image=contact_us, cursor="hand2", highlightthickness=0, bd=0,
                 command=lambda: [display_logo(5, contact_logo2)])
button3.grid(row=5, column=1, padx=0, pady=0)


def admin():
    window.destroy()
    window2 = Tk()
    window2.geometry("{0}x{1}+0+0".format(window2.winfo_screenwidth() - 50, window2.winfo_screenheight() - 50))
    window2.configure(bg='white')
    window2.title('hospital bed management system')

    button_frame2 = Frame(window2, bg='#545454', width=250, height=715)
    button_frame2.pack(side='left')
    window2.mainloop()
    Label(button_frame2, image=logo, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=2, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=6, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=7, column=0, columnspan=2)
    Label(button_frame2, image=blank, padx=0, pady=0, bd=0).grid(row=8, column=0, columnspan=2)
    Label(button_frame2, image=acc_logo, highlightthickness=0, bd=0).grid(row=3, column=0, padx=0, pady=0)
    btn1 = Button(button_frame2, image=account, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [display_logo(3, acc_logo2, button_frame2), login()])
    btn1.grid(row=3, column=1, padx=0, pady=0)
    Label(button_frame2, image=about_logo, highlightthickness=0, bd=0).grid(row=4, column=0, padx=0, pady=0)
    btn2 = Button(button_frame2, image=about, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [display_logo(4, about_logo2, button_frame2)])
    btn2.grid(row=4, column=1, padx=0, pady=0)
    Label(button_frame2, image=contact_logo, highlightthickness=0, bd=0).grid(row=5, column=0, padx=0, pady=0)
    btn3 = Button(button_frame2, image=contact_us, cursor="hand2", highlightthickness=0, bd=0,
                  command=lambda: [display_logo(5, contact_logo2, button_frame2)])
    btn3.grid(row=5, column=1, padx=0, pady=0)


def display_logo(n, m, p=button_frame):
    Label(p, image=m, padx=0, pady=0, bd=0).grid(row=n, column=0)


def close():
    pass


def login():
    def login_final():
        u = user.get()
        p = password.get()
        if u in users:
            index = users.index(u)

            if passwords[index] == p:
                print("values matched")
                #admin()
            else:
                print("wrong password")
        else:
            print("wrong user name")

    users = wks2.col_values(1)
    passwords = wks2.col_values(2)
    password = StringVar()
    user = StringVar()
    main = Toplevel(window)
    main.geometry('700x500')
    main.protocol("WM_DELETE_WINDOW", close)
    main.resizable(0, 0)
    entry_frame = Frame(main)
    entry_frame.pack(side='top')
    Label(entry_frame, text="User Name : ").grid(row=0, column=0)
    entry1 = Entry(entry_frame, text=user)
    entry1.grid(row=0, column=1)
    Label(entry_frame, text="Password : ").grid(row=1, column=0)
    entry2 = Entry(entry_frame, text=password, show="*")
    entry2.grid(row=1, column=1)
    Button(main, text="Login", command=lambda: [login_final()]).pack()
    Button(main, text="Close", command=lambda: [main.destroy(), display_logo(3, acc_logo)]).pack()


window.mainloop()
