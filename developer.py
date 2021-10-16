from tkinter import*
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title("Student Management System Developer Window")

        # First header image

        img1 = Image.open("images/mh1.jpg")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=510, height=130)

        # Middle header image

        img2 = Image.open("images/mh2.jpg")
        img2 = img2.resize((520, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Third header image

        img3 = Image.open("images/mh3.jpg")
        img3 = img3.resize((520, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1020, y=0, width=520, height=130)

# <----------- image frame for background of remaining window except header window -------------->
        img4 = Image.open("images/bgmain4.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Developer Of Project Student Management System By Facial Recognition ", font=(
            "'Fredoka One', sans-serif", 30, "bold"), bg="#b0c4de", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Creating s sub frame inside the image frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=52, width=1530, height=650)

        # inside the sub frame we create another frame

        # Left frame
        Left_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Developer Window", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Left_frame.place(x=0, y=0, width=750, height=597)

        # profile Image

        profile_img = Image.open("images/akhil1.jpg")
        profile_img = profile_img.resize((150, 150), Image.ANTIALIAS)
        self.photoprofile_img = ImageTk.PhotoImage(profile_img)

        f_lbl = Label(Left_frame, image=self.photoprofile_img)
        f_lbl.place(x=300, y=0, width=150, height=150)

        developer_info = LabelFrame(
            Left_frame, bd=0, relief=RIDGE, text="", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        developer_info.place(x=200, y=190, width=545, height=350)

        # for name

        dev_name = Label(developer_info, text="Name", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_name.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dev_name1 = Label(developer_info, text=": Akhilesh Yadav", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_name1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # for graduation

        dev_graduatin = Label(developer_info, text="Graduation", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_graduatin.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        dev_graduatin1 = Label(developer_info, text=": Bachelor Of Technology", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_graduatin1.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Stream
        dev_stream = Label(developer_info, text="Stream", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_stream.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        dev_stream1 = Label(developer_info, text=": Computer Science and Engineering", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_stream1.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Office
        dev_office = Label(developer_info, text="Office", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_office.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        dev_office = Label(developer_info, text=": Kanpur,Utter Pradesh", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_office.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Phone

        dev_phone = Label(developer_info, text="Phone", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_phone.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        dev_phone1 = Label(developer_info, text=": +919616588637", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_phone1.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # email

        dev_email = Label(developer_info, text="Email", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_email.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        dev_email1 = Label(developer_info, text=": yadavakhilesh201616@gmail.com", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_email1.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # Right frame
        Right_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Python Library and other Funcion Used in this Project", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Right_frame.place(x=760, y=0, width=760, height=595)

        developer_skills = LabelFrame(
            Right_frame, bd=2, relief=RIDGE, text="", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        developer_skills.place(x=0, y=0, width=750, height=570)


# Files used in thhis project

        dev_files = Label(developer_skills, text="Files", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_files.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dev_files1 = Label(developer_skills, text=": main.py", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_files1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        dev_files2 = Label(developer_skills, text=", student.py", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_files2.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        dev_files3 = Label(developer_skills, text=", train.py", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_files3.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        dev_files4 = Label(developer_skills, text=", developer.py", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_files4.grid(row=0, column=4, padx=10, pady=10, sticky=W)
        dev_files5 = Label(developer_skills, text=", attendence.py", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_files5.grid(row=0, column=5, padx=10, pady=10, sticky=W)

# Technical skills

        dev_tech = Label(developer_skills, text="Technical Skills", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_tech.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        # skills
        dev_tech1 = Label(developer_skills, text=": Python", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_tech1.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        dev_tech2 = Label(developer_skills, text=", MySQL", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_tech2.grid(row=1, column=2, padx=10, pady=10, sticky=W)

# Library used in this project are

        dev_lib = Label(developer_skills, text="Library Used", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_lib.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        dev_lib1 = Label(developer_skills, text=": NumPy, cv2 ,", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_lib1.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        dev_lib2 = Label(developer_skills, text=",Tkinter,  os ,", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_lib2.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        dev_lib4 = Label(developer_skills, text="PIL , ", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_lib4.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        dev_lib5 = Label(developer_skills, text="mysql.connector , ", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_lib5.grid(row=2, column=4, padx=10, pady=10, sticky=W)

        dev_lib6 = Label(developer_skills, text="csv", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_lib6.grid(row=2, column=5, padx=10, pady=10, sticky=W)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
