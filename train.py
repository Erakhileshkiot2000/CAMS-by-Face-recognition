from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title(
            "Student Management System For Training The Images Taken By Web Camera In Student Details")

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

        #  title label frame

        title_lbl = Label(self.root, text="Training Data Set By Using Python", font=(
            "'Fredoka One', sans-serif", 35, "bold"), fg="Green")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        # Train data frame

        current_course_frame = LabelFrame(
            self.root, bd=2, relief=RIDGE, text="Train Data", font=(
                "'Fredoka One', sans-serif", 14, "bold"), fg="blue")
        current_course_frame.place(x=0, y=185, width=1530, height=602)

        # Now for train button image

        # For Train Button

        img4 = Image.open("images/card1.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(current_course_frame, command=self.train_classifier,
                    image=self.photoimg4, cursor="hand2")
        b1.place(x=660, y=50, width=220, height=220)

        train_btn = Button(current_course_frame, command=self.train_classifier, text="Train Data", width=11, font=(
            "'Fredoka One', sans-serif", 18, "bold"), fg="Green", bg="#b0c4de")
        train_btn.place(x=660, y=270, height=50, width=220)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            # to convert the image in gray scale
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train data", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # <------------train the classifier------------------>

        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data set completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
