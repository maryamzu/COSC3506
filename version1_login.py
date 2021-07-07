import os
from tkinter import *

def register_new_user():
    user_info = username.get()
    pass_info = password.get()
   # passc_info = password_c.get()
    file = open(user_info, "w")
    file.write(user_info+"\n")
    file.write(pass_info)
    file.close()

    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    passc_entry.delete(0, END)

    if password == password_c:
        return
    Label(screen1, text="Registration Success", fg="green").pack()

def login_verify():
    username1 = user_verification.get()
    password1 = pass_verification.get()
    user_entry1.delete(0, END)
    pass_entry1.delete(0, END)

    list = os.listdir()
    if username1 in list:
        file1 = open(username1, "r")
        verification = file1.read().splitlines()
        if password1 in verification:
            print("Login Success!")
        else:
            print("User not found!")

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x250")
    global username
    global password
    global user_entry
    global pass_entry
    global passc_entry
    global password_c
    username = StringVar()
    password = StringVar()
    password_c = StringVar()

    Label(screen1, text="Username * ").pack()
    user_entry = Entry(screen1, textvariable=username)
    user_entry.pack()

    Label(screen1, text="Password * ").pack()
    pass_entry = Entry(screen1, textvariable=password,  show='*')
    pass_entry.pack()

    Label(screen1, text="Password Confirmation * ").pack()
    passc_entry = Entry(screen1, textvariable=password_c, show='*')
    passc_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_new_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry('400x250')

    global user_verification
    global pass_verification

    user_verification = StringVar()
    pass_verification = StringVar()

    global user_entry1
    global pass_entry1

    Label(screen2, text="Username * ").pack()
    user_entry1 = Entry(screen2, textvariable=user_verification)
    user_entry1.pack()

    Label(screen2, text="Password * ").pack()
    pass_entry1 = Entry(screen2, textvariable=pass_verification, show='*')
    pass_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def mainScreen():
    global screen
    screen = Tk()
    screen.geometry('400x250')
    screen.title("StaffChat")
    Label(text="Staff Chat", bg="Grey", width="300", height="2", font=("Times Roman", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()
mainScreen()