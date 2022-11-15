from tkinter import *
from tkinter import messagebox
from register import Register
from sign_up import Signup
import hashlib
from mysql.connector import connect, Error
from train import Train

try:
    with connect(host="localhost", user="root", password="Fe$tu$245618", database="project"

    ) as connection:
        my_database = connection.cursor()
        my_database.execute("SELECT * FROM `user`")
        output = my_database.fetchall()
        hash = hashlib.md5()

        UR = output[0][1]
        PW = output[0][2]
except Error as e:
    print(e)


def reg_page():
    Register()


def home_page():
    home = Tk()
    home.title("Home")
    home.geometry("925x500+300+200")
    img4 = PhotoImage(file="./image_for_project/man.png")
    home.iconphoto(False, img4)
    home.configure(bg="#fff")
    home.resizable(False, False)
    img2 = PhotoImage(file="./image_for_project/woman.png")
    background = PhotoImage(file="./image_for_project/background.png")
    Label(home, image=background).place(x=0, y=0)
    Label(home, text="Facial Recognition System", fg="#2B65EC", bg="#fff",
        font=("Franklin Gothic Heavy", 28, "bold")).place(x=180, y=2)

    ###################__________________________________
    def on_enter(e):
        button_rg['background'] = "#434cc7"
        button_rg["foreground"] = "#fff"

    def on_leave(e):
        button_rg['background'] = "#fff"
        button_rg["foreground"] = "#434cc7"

    frame1 = Frame(home, width=350, height=350, bg="#446bb9")
    frame1.place(x=480, y=70)
    Label(frame1, text="Verify User", fg="#fff", bg="#446bb9", font=("Franklin Gothic Heavy", 23, "bold")).place(x=80,
        y=110)
    button_rg = Button(frame1, text="Verify User", width=25, pady=7, bg="#fff", fg="#446bb9", border=0, command=Train)
    button_rg.place(x=80, y=290)
    button_rg.bind("<Enter>", on_enter)
    button_rg.bind("<Leave>", on_leave)
    Label(frame1, image=img4, bg="#fff").place(x=130, y=10)

    ##############_________________________________________
    def on_enter(e):
        button_lg['background'] = "#434cc7"
        button_lg["foreground"] = "#fff"

    def on_leave(e):
        button_lg['background'] = "#fff"
        button_lg["foreground"] = "#434cc7"

    frame2 = Frame(home, width=350, height=350, bg="#446bb9")
    frame2.place(x=100, y=70)
    Label(frame2, text="Registration", fg="#fff", bg="#446bb9", font=("Franklin Gothic Heavy", 23, "bold")).place(x=80,
        y=110)
    button_lg = Button(frame2, text="Register User", width=25, pady=7, bg="#fff", fg="#446bb9", border=0, command=reg_page)
    button_lg.place(x=80, y=290)
    button_lg.bind("<Enter>", on_enter)
    button_lg.bind("<Leave>", on_leave)
    Label(frame2, image=img2, bg="#fff").place(x=130, y=10)

    #############___________________________________________

    home.mainloop()
def Signups():
    Signup(output)

def login_pages():
    root = Tk()
    root.title("LOGIN")
    root.geometry("925x500+300+200")
    img4 = PhotoImage(file="./image_for_project/man.png")
    root.iconphoto(False, img4)
    root.configure(bg="#fff")
    root.resizable(False, False)
    img = PhotoImage(file="./image_for_project/Asset 111.png")
    background = PhotoImage(file="./image_for_project/background.png")
    Label(root, image=background).place(x=0, y=0)

    def signin():
        username = user.get().lower()
        pword = password.get()
        if username == UR and hashlib.md5(pword.encode()).hexdigest() == PW:
            root.destroy()
            home_page()

            # screen = Toplevel(root)  # screen.title("App")  # screen.geometry("925x500+300+200")  # screen.config(bg="white")  #  # Label(screen, text="Hello Everyone", bg="#fff", font=("calibri(Body)", 50, "bold")).pack(expand=True)  # screen.mainloop()
        elif (username != UR and hashlib.md5(pword.encode()).hexdigest() != PW) or (username != UR):
            messagebox.showerror("Invalid", "invalid username or password")
        elif hashlib.md5(pword.encode()).hexdigest() != PW:
            messagebox.showerror("Invalid", "invalid username or password")

    Label(root, image=img, bg="#fff").place(x=50, y=50)
    Label(root, text="Student Data Collection", fg="#2B65EC", bg="#fff",
        font=("Franklin Gothic Heavy", 28, "bold")).place(x=220, y=2)
    # Label(root, text="Facial Recognition System", bg="#fff").place(x=50, y=60)
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)
    heading = Label(frame, text="Sign in", fg="#57a1f8", bg="#fff", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=110, y=5)

    #######################-----------------------username---------------------------------------

    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")

    user = Entry(frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=105)

    ######################--------------------password--------------------------------------------------
    def on_enter(e):
        password.delete(0, "end")

    def on_leave(e):
        name = password.get()
        if name == "":
            password.insert(0, "Password")

    password = Entry(frame, show="*", width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
    password.place(x=30, y=150)
    password.insert(0, "Password")
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    #############################################################################################################
    def on_enter(e):
        button['background'] = "#fffccc"
        button["foreground"] = "#434cc7"

    def on_leave(e):
        button['background'] = "#434cc7"
        button["foreground"] = "#fff"

    button = Button(frame, width=36, pady=7, text="Sign in", bg="#434cc7", fg="#fff", border=0, command=signin)
    button.place(x=50, y=210)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=110, y=270)
    sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=Signups)
    sign_up.place(x=250, y=270)
    root.mainloop()


login_pages()
