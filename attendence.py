from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np


mydata = []


class Student_attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title("Student Management System Student Attendence Details")

        # variable for filf the predefiened values

        self.var_attendence_id = StringVar()
        self.var_attendence_name = StringVar()
        self.var_attendence_roll = StringVar()
        self.var_attendence_dep = StringVar()
        self.var_attendence_time = StringVar()
        self.var_attendence_date = StringVar()
        self.var_attendence_status = StringVar()

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

        title_lbl = Label(bg_img, text="Save The Attendence In DataBases And Show In A Table On Attendence Window", font=(
            "'Fredoka One', sans-serif", 30, "bold"), bg="#b0c4de", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Creating s sub frame inside the image frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=52, width=1530, height=650)

        # inside the sub frame we create another frame

        # Left frame
        Left_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Student Attendence Details", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Left_frame.place(x=0, y=0, width=750, height=600)

        # left frame top image
        img_left_top = Image.open("images/mh1.jpg")
        img_left_top = img_left_top.resize((740, 130), Image.ANTIALIAS)
        self.photoimg_left_top = ImageTk.PhotoImage(img_left_top)

        f_lbl = Label(Left_frame, image=self.photoimg_left_top)
        f_lbl.place(x=0, y=0, width=747, height=130)

        # Current Course frame

        # For the grid inside the Current course frame
        class_student_frame = LabelFrame(
            Left_frame, bd=2, relief=RIDGE, text="", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        class_student_frame.place(x=0, y=130, width=745, height=443)
        # for department

        # <=------------Attendence Id -------------->

        attendence_label = Label(class_student_frame, text="Attendence Id", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        attendence_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        attendence_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_id, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        attendence_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name Field and Entry fields

        name_label = Label(class_student_frame, text="Name", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_name, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        # time Field and Entry fields

        time_label = Label(class_student_frame, text="Time", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_time, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # <----------for Roll number fields -------------->

        roll_label = Label(class_student_frame, text="Roll", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        roll_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_roll, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Name Field and Entry fields

        dep_label = Label(class_student_frame, text="Department", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        dep_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        dep_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_dep, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        # time Field and Entry fields

        date_label = Label(class_student_frame, text="Date", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        date_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(class_student_frame, textvariable=self.var_attendence_date, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # for status of attendence

        status_label = Label(class_student_frame, text="Status", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        status_label.grid(row=3, column=0, padx=6, pady=10, sticky=W)

        # <----------- combobox field value  ----------------->
        status_combo = ttk.Combobox(class_student_frame, textvariable=self.var_attendence_status, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=18)
        status_combo["values"] = ("Status",
                                  "Present", "Abscent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=6, pady=10, sticky=W)

        btn_frme = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frme.place(x=0, y=396, width=740, height=40)

        # save button
        import_btn = Button(btn_frme, command=self.import_csv, text="Import", width=19, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        import_btn.grid(row=0, column=0)

        # Update button
        export_btn = Button(btn_frme, command=self.export_csv, text="Export", width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        export_btn.grid(row=0, column=1)

        # delete buttn
        update_btn = Button(btn_frme,  text="Update", width=19, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        update_btn.grid(row=0, column=2)

        # Reset  button

        reset_btn = Button(btn_frme, command=self.reset_data, text="Reset", width=19, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        reset_btn.grid(row=0, column=3)

        # <-------------right frame---------------->
        Right_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Right_frame.place(x=760, y=0, width=760, height=600)

        # left frame top image
        right_top = Image.open("images/mh1.jpg")
        right_top = right_top.resize((750, 130), Image.ANTIALIAS)
        self.photoimg_right_top = ImageTk.PhotoImage(right_top)

        f_lbl = Label(Right_frame, image=self.photoimg_right_top)
        f_lbl.place(x=0, y=0, width=756, height=130)

        # table frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=130, width=752, height=444)

        # to set scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendence_table = ttk.Treeview(table_frame, column=(
            "id", "name", "roll", "department", "time", "date", "attendence"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendence_table.xview)
        scroll_y.config(command=self.attendence_table.yview)

        self.attendence_table.heading("id", text="Attendence_Id")
        self.attendence_table.heading("name", text="Name")
        self.attendence_table.heading("roll", text="Roll")
        self.attendence_table.heading("department", text="Department")
        self.attendence_table.heading("time", text="Time")
        self.attendence_table.heading("date", text="Date")
        self.attendence_table.heading("attendence", text="Attendence_Status")

        self.attendence_table["show"] = "headings"

        self.attendence_table.column("id", width=120)
        self.attendence_table.column("name", width=120)
        self.attendence_table.column("roll", width=120)
        self.attendence_table.column("department", width=120)
        self.attendence_table.column("time", width=120)
        self.attendence_table.column("date", width=120)
        self.attendence_table.column("attendence", width=120)

        self.attendence_table.pack(fill=BOTH, expand=1)
        self.attendence_table.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self, rows):
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert("", END, values=i)

        # <------------------- for import csv ----------------->

    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

            # <------------- for export csv data --------------->
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="")as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Data Exportedto "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendence_table.focus()
        content = self.attendence_table.item(cursor_row)
        rows = content['values']
        self.var_attendence_id.set(rows[0])
        self.var_attendence_name.set(rows[1])
        self.var_attendence_roll.set(rows[2])
        self.var_attendence_dep.set(rows[3])
        self.var_attendence_time.set(rows[4])
        self.var_attendence_date.set(rows[5])
        self.var_attendence_status.set(rows[6])

    def reset_data(self):
        self.var_attendence_id.set("")
        self.var_attendence_name.set("")
        self.var_attendence_roll.set("")
        self.var_attendence_dep.set("")
        self.var_attendence_time.set("")
        self.var_attendence_date.set("")
        self.var_attendence_status.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Student_attendence(root)
    root.mainloop()
