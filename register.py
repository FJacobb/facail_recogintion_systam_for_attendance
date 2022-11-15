from tkinter import *
import pandas
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter
import cv2
import os


class Register():
    def __init__(self):
        super().__init__()
        self.register = Toplevel()
        self.register.title("Register")
        self.register.geometry("925x500+300+200")
        self.img3 =  PhotoImage(file="./image_for_project/man.png")
        self.register.iconphoto(False, self.img3)
        self.background = PhotoImage(file="./image_for_project/background.png")
        Label(self.register, image=self.background).place(x=0, y=0)
        Label(self.register, text="Student Data Collection", fg="#2B65EC", bg="#fff",
              font=("Franklin Gothic Heavy", 28, "bold")).place(x=220, y=2)
        self.but()
        self.register.mainloop()

    def but(self):
        def on_enter(e):
            self.button_rg['background'] = "#434cc7"
            self.button_rg["foreground"] = "#fff"

        def on_leave(e):
            self.button_rg['background'] = "#fff"
            self.button_rg["foreground"] = "#434cc7"

        self.frame1 = Frame(self.register, width=350, height=350, bg="#446bb9")
        self.frame1.place(x=480, y=70)
        self.paneeli_image = tkinter.Label(self.frame1)  # ,image=img)
        self.paneeli_image.place(x=0, y=0)
        self.button_rg = Button(self.frame1, text="ADD USER", width=25, pady=7, bg="#fff", fg="#446bb9", border=0,
                                command=self.facecollect)
        self.button_rg.place(x=80, y=290)
        self.button_rg.bind("<Enter>", on_enter)
        self.button_rg.bind("<Leave>", on_leave)
        ##############_________________________________________

        self.frame2 = Frame(self.register, width=350, height=350, bg="#446bb9")
        self.frame2.place(x=100, y=70)

        #############___________________________________________
    global video

    def facecollect(self):
        global video
        self.button_rg.destroy()
        def cam():
            global frame
            count = 0
            partment = dep.get().upper()
            id = nameID.get().upper()
            while True:
                ret, frame = video.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = facedetect.detectMultiScale(frame, 2.0, 5)
                img_update = ImageTk.PhotoImage(Image.fromarray(frame))
                self.paneeli_image.configure(image=img_update, width=350, height=350)
                self.paneeli_image.image = img_update
                self.paneeli_image.update()
                for x, y, w, h in faces:
                    count = count + 1
                    name = './images/AFIT/' +str(partment)+"/"+ str(id) + '/' + str(count) + '.jpg'
                    Label(self.frame2, text="Creating Images......" + name, fg="#fff", bg="#446bb9",
                          font=("Franklin Gothic Heavy", 6, "bold")).place(x=20, y=160)
                    cv2.imwrite(name, frame[y:(y - 32) + (h + 20), x:(x - 32) + (w + 20)])
                cv2.waitKey(1)
                if count > 500:
                    Label(self.frame2, text="Successful Data Collection", fg="#fff", bg="#446bb9",
                          font=("Franklin Gothic Heavy", 10, "bold")).place(x=20,
                                                                            y=180)
                    break

            video.release()
            cv2.destroyAllWindows()
            mg = "You have successfully register (" + str(id) + ") ."
            messagebox.showinfo("Message", mg)
            self.register.destroy()


        def check():

            self.path = 'images/AFIT/' +str(dep.get().upper())+"/"+ str(nameID.get().upper())

            self.isExist = os.path.exists(self.path)

            if self.isExist:
                mg = "This student ID ("+str(nameID.get().upper())+") is registered"
                messagebox.showerror("error", mg)
            else:
                with open("id of student.txt", mode='a') as file:
                    fm = str(nameID.get().upper())
                    file.write(f"{fm}\n")
                os.makedirs(self.path)
                cam()
        video = cv2.VideoCapture(2)

        facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


        Label(self.frame2, text="Enter Your Student ID: ", fg="#fff", bg="#446bb9",
              font=("Franklin Gothic Heavy", 10, "bold")).place(x=40,
                                                           y=120)
        Label(self.frame2, text="Enter your Department: ", fg="#fff", bg="#446bb9",
            font=("Franklin Gothic Heavy", 10, "bold")).place(x=40, y=60)

        def on_enter1(e):
            dep.delete(0, "end")

        def on_leave1(e):
            name = dep.get()
            if name == "":
                dep.insert(0, "cyber security")
        def on_enter2(e):
            nameID.delete(0, "end")

        def on_leave2(e):
            name = nameID.get()
            if name == "":
                nameID.insert(0, "AFIT-CYS-18-0027")
        dep = Entry(self.frame2, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        dep.place(x=40, y=80)
        dep.insert(0, "cyber security")
        dep.bind("<FocusIn>", on_enter1)
        dep.bind("<FocusOut>", on_leave1)
        nameID = Entry(self.frame2, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
        nameID.place(x=40, y=140)
        nameID.insert(0, "AFIT-CYS-18-0027")
        nameID.bind("<FocusIn>", on_enter2)
        nameID.bind("<FocusOut>", on_leave2)


        def on_enter(e):
            self.button_rg['background'] = "#434cc7"
            self.button_rg["foreground"] = "#fff"

        def on_leave(e):
            self.button_rg['background'] = "#fff"
            self.button_rg["foreground"] = "#434cc7"

        self.button_rg = Button(self.frame2, text="Verify Student ID", width=25, pady=7, bg="#fff", fg="#446bb9", border=0,
                           command=check)
        self.button_rg.place(x=80, y=290)
        self.button_rg.bind("<Enter>", on_enter)
        self.button_rg.bind("<Leave>", on_leave)
