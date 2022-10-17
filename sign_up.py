from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import hashlib
from mysql.connector import connect, Error, cursor
import tkinter
import cv2
import os

class Signup():
    def __init__(self):
        super().__init__()
        self.signup = Toplevel()
        self.signup.title("Sign up")
        self.signup.geometry("925x500+300+200")
        self.img3 = PhotoImage(file="./image_for_project/man.png")
        self.signup.iconphoto(False, self.img3)
        self.background = PhotoImage(file="./image_for_project/background.png")
        self.img = PhotoImage(file="./image_for_project/Asset 111.png")
        Label(self.signup, image=self.background).place(x=0, y=0)
        Label(self.signup, image=self.img, bg="#fff").place(x=50, y=50)
        Label(self.signup, text="Student Data Collection", fg="#2B65EC", bg="#fff",
              font=("Franklin Gothic Heavy", 28, "bold")).place(x=220, y=2)
        self.but()
        self.signup.mainloop()

    def signin(self):
        self.signup.destroy()

    def sign_up(self):
        self.nr = self.user.get()
        self.pw = self.password.get()
        self.em = self.email.get()
        self.id = 1
        try:
            self.signin()
            with connect(
                    host="localhost",
                    user="root",
                    password="Fe$tu$245618",
                    database="project"

            ) as connection:
                my_database = connection.cursor()
                my_database.execute(f"INSERT INTO `user`(`id`, `username`, `password`, `email`) VALUES ('{self.id+1}','{self.nr}',MD5('{self.pw}'),'{self.em}')")
        except Error as e:
            print(e)

    def but(self):
        self.frame = Frame(self.signup, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)
        self.heading = Label(self.frame, text="Sign up", fg="#57a1f8", bg="#fff", font=("Microsoft YaHei UI Light", 23, "bold"))
        self.heading.place(x=110, y=5)

        #######################-----------------------username---------------------------------------

        def on_enter(e):
            self.user.delete(0, "end")

        def on_leave(e):
            name = self.user.get()
            if name == "":
                self.user.insert(0, "Username")

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Username")
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)
        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=105)

        ######################--------------------password--------------------------------------------------
        def on_enter(e):
            self.password.delete(0, "end")

        def on_leave(e):
            name = self.password.get()
            if name == "":
                self.password.insert(0, "Password")

        self.password = Entry(self.frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        self.password.place(x=30, y=125)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", on_enter)
        self.password.bind("<FocusOut>", on_leave)
        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=152)

        ######################--------------------password--------------------------------------------------
        def on_enter(e):
            self.email.delete(0, "end")

        def on_leave(e):
            name = self.email.get()
            if name == "":
                self.email.insert(0, "Password")

        self.email = Entry(self.frame, width=25, fg="black", border=0, bg="#fff",
                              font=("Microsoft YaHei UI Light", 11))
        self.email.place(x=30, y=170)
        self.email.insert(0, "Email")
        self.email.bind("<FocusIn>", on_enter)
        self.email.bind("<FocusOut>", on_leave)
        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=197)
        #############################################################################################################
        Button(self.frame, width=36, pady=7, text="Sign up", bg="#57a1f8", fg="#fff", border=0, command=self.signup).place(x=50,
                                                                                                                 y=230)
        label = Label(self.frame, text="Do you have an account?", fg="black", bg="white",
                      font=("Microsoft YaHei UI Light", 9))
        label.place(x=100, y=280)
        sign_up = Button(self.frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8",
                         command=self.signin)
        sign_up.place(x=250, y=280)
