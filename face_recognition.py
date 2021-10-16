from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title(
            "Student Management System Face Recoginition By Using Web Camera")

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

        title_lbl = Label(self.root, text="Face Recognition To Take Attendence By Using Python", font=(
            "'Fredoka One', sans-serif", 35, "bold"), fg="Green")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        current_course_frame = LabelFrame(
            self.root, bd=2, relief=RIDGE, text="Train Data", font=(
                "'Fredoka One', sans-serif", 14, "bold"), fg="blue")
        current_course_frame.place(x=0, y=185, width=1530, height=602)

        img4 = Image.open("images/card1.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS, )
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(current_course_frame, command=self.face_recognizer,
                    image=self.photoimg4, cursor="hand2")
        b1.place(x=660, y=50, width=220, height=220)

        train_btn = Button(current_course_frame, command=self.face_recognizer,
                           text="Face Recognition", width=11, fg="Green", bg="#b0c4de")
        train_btn.place(x=660, y=270, height=50, width=220)

# <------------------ Attendence Markseet Save to our excel sheet ------------->
    def save_attendence(self, i, n, r, d):
        with open("Akhil.csv", "r+", newline="\n")as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)and(n not in name_list)and(r not in name_list)and(d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")

                # function for face recognition

    def face_recognizer(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                # to show name
                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                # to show id
                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                # to show department
                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 50:
                    # to show id of student
                    cv2.putText(
                        img, f"ID:{i}", (x-299, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (253, 0, 0), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x-299, y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (253, 0, 0), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x-299, y+150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (253, 0, 0), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x-299, y+200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (253, 0, 0), 3)
                    self.save_attendence(i, n, r, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown face:", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Fcae Recognization", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
