import datetime
from tkinter import *
from tkinter import messagebox
from send_log import Mail

def login_pages():
    root = Tk()
    root.title("PROFILE")
    root.geometry("925x500+300+200")
    img4 = PhotoImage(file="./image_for_project/Ellipse 1.png")
    root.iconphoto(False, img4)
    root.configure(bg="#fff")
    root.resizable(False, False)

    background = PhotoImage(file="./image_for_project/background.png")
    Label(root, image=background).place(x=0, y=0)
    Label(root, text="PROFILE", fg="#2B65EC", bg="#fff",
        font=("Franklin Gothic Heavy", 28, "bold")).place(x=390, y=2)
    # Label(root, text="Facial Recognition System", bg="#fff").place(x=50, y=60)
    Label(root, image=img4, bg="#fff").place(x=145, y=10)
    frame = Frame(root, width=350, height=350, bg="#446bb9")
    frame.place(x=50, y=70)
    heading = Label(frame, text="Sign in", fg="#57a1f8", bg="#fff", font=("Microsoft YaHei UI Light", 23, "bold"))
    frame2 = Frame(root, width=350, height=160, bg="#446bb9")
    frame2.place(x=480, y=70)

    frame3 = Frame(root, width=350, height=160, bg="#446bb9")
    frame3.place(x=480, y=260)

    #########################################################################################################
    def click_in():
        if faculty.get() != '' and department.get() != "" and user.get() != "":
            selected_faculty = faculty.get()
            selected_department = department.get()
            Mail(selected_faculty, selected_department, user.get())
            messagebox.showinfo("Status","Mail sent")
        else:
            messagebox.showerror("Invalid", "you most select an option for each box and put in your email")
    Label(frame2, text="Email", fg="#fff", bg="#446bb9",font=("Franklin Gothic Heavy", 18, "bold")).place(x=135, y=5)
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Email")

    def on_enter1(e):
        button_email['background'] = "#fffccc"
        button_email["foreground"] = "#434cc7"

    def on_leave1(e):
        button_email['background'] = "#434cc7"
        button_email["foreground"] = "#fff"

    user = Entry(frame2, width=25, fg="#fff", border=0, bg="#446bb9", font=("Microsoft YaHei UI Light", 11))
    user.place(x=20, y=80)
    user.insert(0, "Email")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame2, width=295, height=2, bg="#fff").place(x=20, y=105)
    button_email = Button(frame2, text="send",  width=36, pady=7, bg="#446bb9", fg="#fff", border=0, command=click_in)
    button_email.place(x=40,y=120)
    button_email.bind("<Enter>", on_enter1)
    button_email.bind("<Leave>", on_leave1)

    #########################################################################################################
    options_faculty = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    faculty = StringVar()
    faculty.set("Select the Faculty")
    drop = OptionMenu(frame3, faculty, *options_faculty, user.get())
    drop.place(x=10, y=10)

    #--------------------------------------------------------------------------------------------------------
    options_department = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    department = StringVar()
    department.set("Select the Department")
    drop = OptionMenu(frame3, department, *options_department)
    drop.place(x=10, y=60)
    #########################################################################################################
    label1 = Label(frame, text="Admin", fg="#fff", bg="#446bb9", font=("Arial Rounded MT", 18, "bold"))
    label1.place(x=10,y=150)
    label2 = Label(frame, text="projectfestus@gmail.com", fg="#fff", bg="#446bb9", font=("Arial Rounded MT", 18))
    label2.place(x=10, y=180)
    label3 = Label(frame, text="password", fg="#fff", bg="#446bb9", font=("Arial Rounded MT", 15))
    label3.place(x=10, y=210)
    label4 = Label(frame, text=f"{datetime.datetime.now().strftime('%y%B%d')}", fg="#fff", bg="#446bb9", font=("Arial Rounded MT", 18))
    label4.place(x=10, y=240)
    #########################################################################################################

    root.mainloop()
login_pages()
