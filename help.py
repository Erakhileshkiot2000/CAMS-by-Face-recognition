from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
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

        title_lbl = Label(bg_img, text="For Help Of Project Student Management System By Facial Recognition ", font=(
            "'Fredoka One', sans-serif", 30, "bold"), bg="#b0c4de", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Creating s sub frame inside the image frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=52, width=1530, height=650)

        # inside the sub frame we create another frame

        # Left frame
        Left_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Help Window", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Left_frame.place(x=380, y=0, width=750, height=597)

        # profile Image

        profile_img = Image.open("images/akhil1.jpg")
        profile_img = profile_img.resize((150, 150), Image.ANTIALIAS)
        self.photoprofile_img = ImageTk.PhotoImage(profile_img)

        f_lbl = Label(Left_frame, image=self.photoprofile_img)
        f_lbl.place(x=300, y=0, width=150, height=150)

        developer_info = LabelFrame(
            Left_frame, bd=0, relief=RIDGE, text="", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        developer_info.place(x=230, y=190, width=400, height=422)

        # Phone

        dev_phone = Label(developer_info, text="Phone", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_phone.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dev_phone1 = Label(developer_info, text=": +919616588637", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_phone1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # email

        dev_email = Label(developer_info, text="Email", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="red")
        dev_email.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        dev_email1 = Label(developer_info, text=": yadavakhilesh201616@gmail.com", font=(
            "'Fredoka One', sans-serif", 12, "bold"), fg="Green")
        dev_email1.grid(row=1, column=1, padx=10, pady=10, sticky=W)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
