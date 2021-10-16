from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
# from login import Login_window


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#8df084")
        self.root.title("Registration From of Facial Recognition System")

        # now variables to take the vslue from entry fields
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security = StringVar()
        self.var_security_ans = StringVar()
        self.var_pass = StringVar()
        self.var_pass_conf = StringVar()
        self.var_terms = IntVar()

        bg_frame = Frame(self.root, bd=2, bg="#4c57ed")
        bg_frame.place(x=250, y=150, width=1000, height=500)

        reg_img = Image.open("images/register.jpg")
        reg_img = reg_img.resize((600, 600), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(reg_img)

        reg_lbl = Label(bg_frame, image=self.bg_photo)
        reg_lbl.place(x=0, y=0, width=450, height=495)

        text_frame = Frame(bg_frame, bd=2, bg="#737bf0")
        text_frame.place(x=450, y=0, width=550, height=500)

        head_name = Label(text_frame, text="REGISTER HERE", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#737bf0")
        head_name.place(x=140, y=0, width=250, height=45)

        # first name

        first_name = Label(text_frame, text="First Name", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        first_name.place(x=15, y=70, width=100, height=30)

        first_name_entry = ttk.Entry(text_frame, textvariable=self.var_first_name, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        first_name_entry.place(x=25, y=100, width=200, height=25)

        # last name no
        last_name = Label(text_frame, text="Last Name", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        last_name.place(x=257, y=70, width=100, height=30)

        last_name_entry = ttk.Entry(text_frame, textvariable=self.var_last_name, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        last_name_entry.place(x=270, y=100, width=200, height=25)

        # contact no
        contact = Label(text_frame, text="Contact No", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        contact.place(x=15, y=140, width=100, height=30)

        contact_entry = ttk.Entry(text_frame, textvariable=self.var_contact, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        contact_entry.place(x=25, y=170, width=200, height=25)

        # Email id
        email_name = Label(text_frame, text="Email", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        email_name.place(x=240, y=140, width=100, height=30)

        email_name_entry = ttk.Entry(text_frame, textvariable=self.var_email, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        email_name_entry.place(x=270, y=170, width=200, height=25)

        # security Question
        security_question = Label(text_frame, text="Select Security Questions", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        security_question.place(x=15, y=210, width=200, height=30)

        # security_question_entry = ttk.Entry(text_frame, width=20, font=(
        #     "'Fredoka One', sans-serif", 11, "bold"))
        # security_question_entry.place(x=25, y=240, width=200, height=25)

        security_combo = ttk.Combobox(text_frame, textvariable=self.var_security, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=18)
        security_combo["values"] = ("Security Questions",
                                    "What is your faverate game", "What is your birth place", "What is your faverate book", "What is tour nick name")
        security_combo.current(0)
        security_combo.place(x=25, y=240, width=200, height=25)

        # security Answer id
        s_answer = Label(text_frame, text="Security Answer", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        s_answer.place(x=250, y=210, width=150, height=30)

        s_answer_entry = ttk.Entry(text_frame, textvariable=self.var_security_ans, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        s_answer_entry.place(x=270, y=240, width=200, height=25)

        password = Label(text_frame, text="Password", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        password.place(x=10, y=270, width=100, height=30)

        password_entry = ttk.Entry(text_frame, textvariable=self.var_pass, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        password_entry.place(x=25, y=300, width=200, height=25)

        # Email id
        cnfpassword = Label(text_frame, text="Confirm Password", font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#737bf0")
        cnfpassword.place(x=245, y=270, width=175, height=30)

        cnfpassword_entry = ttk.Entry(text_frame, textvariable=self.var_pass_conf, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        cnfpassword_entry.place(x=270, y=300, width=200, height=25)

        # check box button
        radio_button1 = ttk.Checkbutton(
            text_frame, variable=self.var_terms, text="Agree,Terms and conditions", offvalue=0, onvalue=1)
        radio_button1.place(x=30, y=350, width=200, height=25)

        btn_frame = Frame(text_frame, bd=2, bg="#732bf1")
        btn_frame.place(x=50, y=400, width=376, height=35)

        register_btn = Button(btn_frame, command=self.register_data,  text="Register", width=9, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        register_btn.grid(row=0, column=0)

        # Login

        login_btn = Button(btn_frame,  text="Already have Account,Login", width=24, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        login_btn.grid(row=0, column=1)
        # exit
        exit_btn = Button(btn_frame, command=self.iExit, text="Exit", width=5, font=(
            "'Fredoka One', sans-serif", 11, "bold"), bg="#269ce0", fg="white")
        exit_btn.grid(row=0, column=2)

    def register_data(self):
        if self.var_first_name.get() == "" or self.var_email.get() == "" or self.var_security.get() == "Security Questions" or self.var_security_ans.get() == "" or self.var_pass.get() == "" or self.var_pass_conf.get() == "" or self.var_terms.get() == 0:
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_pass_conf.get():
            messagebox.showerror(
                "Error", "Password and confirms password are same")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Akhil@9369229439", database="face_recognition")
            my_cursor = conn.cursor()
            querry = ("select * from register where Email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(querry, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User Already exist try by using another eamil")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security.get(),
                    self.var_security_ans.get(),
                    self.var_pass.get(),

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered successfully")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure to exit from Register window", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    # def login_window(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Login_window(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = Register(root)
    root.mainloop()
