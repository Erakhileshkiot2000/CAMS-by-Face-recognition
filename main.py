from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Student_attendence
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title(
            "Student Attendence Management System By Using Facial Recognition")

        # First Header image

        img1 = Image.open("images/mh1.jpg")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=510, height=130)

        # Third header image

        img2 = Image.open("images/mh2.jpg")
        img2 = img2.resize((520, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Second header image

        img3 = Image.open("images/mh3.jpg")
        img3 = img3.resize((520, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1020, y=0, width=520, height=130)

        # Background Image for our home frame or main frmae

        img4 = Image.open("images/bgmain4.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Face Reacognition System In Python", font=(
            "'Fredoka One', sans-serif", 35, "bold"), bg="#b0c4de", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # For card view or to create the different button of home GUI

        # Student Button for card view

        img5 = Image.open("images/student.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face detector

        img6 = Image.open("images/faced1.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, command=self.face_recognition,
                    image=self.photoimg6, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.face_recognition, text="Face Detector", cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendence of student

        img7 = Image.open("images/attendence.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command=self.student_attendence,
                    image=self.photoimg7, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.student_attendence, text="Attendence", cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Window for Users

        img8 = Image.open("images/help.jpeg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command=self.help_window,
                    image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.help_window, text="Help", cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Data

        img9 = Image.open("images/train.jpeg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, command=self.train_data,
                    image=self.photoimg9, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=200, y=600, width=220, height=40)

        # Photos

        img10 = Image.open("images/imagesface.jpeg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, command=self.open_img,
                    image=self.photoimg10, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Images", command=self.open_img, cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=500, y=600, width=220, height=40)

        # Developer

        img11 = Image.open("images/developer.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, command=self.developer_window,
                    image=self.photoimg11, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer",  command=self.developer_window, cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=800, y=600, width=220, height=40)

        # Exit Window for Users

        img12 = Image.open("images/exit.jpeg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, command=self.iExit,
                    image=self.photoimg12, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_1 = Button(bg_img, command=self.iExit, text="Exit", cursor="hand2", font=(
            "'Fredoka One', sans-serif", 15, "bold"), bg="#b0c4de", fg="blue")
        b1_1.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")

# ===============function Button=========================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # for train file import function

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    # for face recognition function

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

        # for attendence window

    def student_attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_attendence(self.new_window)

        # for developer window
    def developer_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

        # for Help window
    def help_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure to exit from this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
