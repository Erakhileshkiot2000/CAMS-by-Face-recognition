from tkinter import*
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from register import Register


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#efefef")
        self.root.title(
            "Login To Student Attendence System by Using Facial Recognition")

        # Mian frame
        self.var_user = StringVar()
        self.var_pass = StringVar()

        bg_lbl = Frame(self.root, bd=2, bg="#269ce0")
        bg_lbl.place(x=0, y=0, width=1530, height=790)

        # main frame
        main_frame = Frame(bg_lbl, bd=2, bg="#269ce0")
        main_frame.place(x=250, y=200, width=1000, height=500)

        # login Image

        login_img = Image.open("images/login1.jpg")
        login_img = login_img.resize((500, 500), Image.ANTIALIAS)
        self.photo_login = ImageTk.PhotoImage(login_img)
        login_lbl = Label(main_frame, image=self.photo_login)
        login_lbl.place(x=0, y=0, width=450, height=500)

        # login grid
        key_frame = LabelFrame(main_frame, text="", bd=0, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="black")
        key_frame.place(x=450, y=46, width=547, height=450)

        # Login Title

        dev_name = Label(key_frame, text="Login", font=(
            "'Fredoka One', sans-serif", 30, "bold"), bg="#269ce0", fg="Black")
        dev_name.place(x=200, y=50, width=100, height=45)

        # auth_img = Image.open("images/auth2.jpg")
        # auth_img = auth_img.resize((200, 200), Image.ANTIALIAS)
        # self.photo_auth = ImageTk.PhotoImage(auth_img)
        # auth_lbl = Label(key_frame, image=self.photo_auth)
        # auth_lbl.place(x=200, y=0, width=140, height=140)

        # now for text and box fields
        # text fields
        login_name = Label(key_frame, text="Username", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#269ce0")
        login_name.place(x=140, y=120, width=150, height=45)

        name_entry = ttk.Entry(key_frame, textvariable=self.var_user, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        name_entry.place(x=167, y=160, width=200, height=30)

        login_pass = Label(key_frame, text="Password", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#269ce0")
        login_pass.place(x=140, y=200, width=150, height=45)

        pass_entry = ttk.Entry(key_frame, textvariable=self.var_pass, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        pass_entry.place(x=167, y=240, width=200, height=30)

        # for button
        btn_frme = LabelFrame(key_frame, bd=2, text="",
                              bg="#269ce0", fg="black", relief=RIDGE)
        btn_frme.place(x=0, y=410, width=547, height=37)

        # save button
        login_btn = Button(btn_frme, command=self.login,  text="Login", width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        login_btn.grid(row=0, column=0)

        # Update button
        Sign_btn = Button(btn_frme, command=self.register_window,  text="New user,Register", width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        Sign_btn.grid(row=0, column=1)

        # delete buttn
        forgot_btn = Button(btn_frme,  text="Forgot Password", width=16, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        forgot_btn.grid(row=0, column=2)

        # Reset  button

        exit_btn = Button(btn_frme, text="Exit", command=self.iExit, width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        exit_btn.grid(row=0, column=3)

        # exit button

    # def home_window(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Face_Recognition_System(self.new_window)

    def login(self):
        if self.var_user.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        # elif self.var_user.get() == "Akhil" and self.var_pass.get() == "123":
        #     messagebox.showinfo(
        #         "Success", "Welcome to Facial recognition system")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Akhil@9369229439", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select *from register where Email = %s and Password = %s", (
                self.var_user.get(),
                self.var_pass.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid User name and password")
            else:
                open_main = messagebox.askyesno(
                    "Yesno", "Access only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)

                else:
                    if not open_main:
                        return

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure to exit from Login window", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Login_window(root)
#     root.mainloop()
