from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#e6fae1")
        self.root.title("Student Management System GUI For Attendence")

    # variable required

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

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

        title_lbl = Label(bg_img, text="Student Management System In Python", font=(
            "'Fredoka One', sans-serif", 35, "bold"), bg="#b0c4de", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Creating s sub frame inside the image frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=52, width=1530, height=650)

        # inside the sub frame we create another frame

        # Left frame
        Left_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
                "'Fredoka One', sans-serif", 12, "bold"), fg="blue")
        Left_frame.place(x=0, y=0, width=750, height=600)

        # left frame top image
        img_left_top = Image.open("images/mh1.jpg")
        img_left_top = img_left_top.resize((740, 130), Image.ANTIALIAS)
        self.photoimg_left_top = ImageTk.PhotoImage(img_left_top)

        f_lbl = Label(Left_frame, image=self.photoimg_left_top)
        f_lbl.place(x=0, y=0, width=747, height=130)

        # Current Course frame
        current_course_frame = LabelFrame(
            Left_frame, bd=2, relief=RIDGE, text="Current Course", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        current_course_frame.place(x=0, y=135, width=745, height=115)

        # For the grid inside the Current course frame

        # for department

        dept_label = Label(current_course_frame, text="Department", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        dept_label.grid(row=0, column=0, sticky=W)

        # for combobox

        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=17)
        dept_combo["values"] = ("Select Department",
                                "Computer Science", "Information Technology", "Civil Engineering", "Mechanical Engineering")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=6, pady=10, sticky=W)

        # for combo box 2  for Year combobox

        year_frame = Label(current_course_frame, text="Year", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        year_frame.grid(row=1, column=0, padx=0, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=17)
        year_combo["values"] = ("Select Year",
                                "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=6, pady=10, sticky=W)

        # for combo box 3 Course combobox

        course_frame = Label(current_course_frame, text="Course", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        course_frame.grid(row=0, column=2, padx=0, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=17)
        course_combo["values"] = ("Select Course",
                                  "C programming", "Robotics", "Strength of Material", "Python Programming")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=6, pady=10, sticky=W)

        # for combo box Semester combo box
        sem_frame = Label(current_course_frame, text="Semester", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        sem_frame.grid(row=1, column=2, padx=0, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=17)
        sem_combo["values"] = ("Select Semester",
                               "Semester_1", "Semester_2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=6, pady=10, sticky=W)

        # now for Class student section informaion

        # this is for label frame

        class_student_frame = LabelFrame(
            Left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        class_student_frame.place(x=0, y=250, width=745, height=325)

        # this is for student information fields

        # student name

        student_name_label = Label(class_student_frame, text="Student Name", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        student_name_label.grid(row=0, column=2, padx=6, pady=10, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # student roll number

        rollno_label = Label(class_student_frame, text="Roll No", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        rollno_label.grid(row=1, column=2, padx=6, pady=10, sticky=W)

        rollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # for dob fields

        dob_label = Label(class_student_frame, text="DOB", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        dob_label.grid(row=2, column=2, padx=6, pady=10, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        #  Phone number fields

        phone_label = Label(class_student_frame, text="Phone No", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        phone_label.grid(row=3, column=2, padx=6, pady=10, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Teacher name fields fields

        teacher_name_label = Label(class_student_frame, text="Teacher Name", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        teacher_name_label.grid(row=4, column=2, padx=6, pady=10, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_teacher, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        # student name
        studentid_label = Label(class_student_frame, text="Student Id", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        studentid_label.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Class devisions

        class_devisions_label = Label(class_student_frame, text="Class Devisions", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        class_devisions_label.grid(row=1, column=0, padx=6, pady=10, sticky=W)

        # class_devisions_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_div, font=(
        #     "'Fredoka One', sans-serif", 11, "bold"))
        # class_devisions_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A",
                               "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=6, pady=10, sticky=W)

        # for gender fields

        gender_label = Label(class_student_frame, text="Gender", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        gender_label.grid(row=2, column=0, padx=6, pady=10, sticky=W)

# <----------- combobox field value  ----------------->
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male",
                                  "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=6, pady=10, sticky=W)

        # Email Address fields

        email_label = Label(class_student_frame, text="Email", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        email_label.grid(row=3, column=0, padx=6, pady=10, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Address fields

        address_label = Label(class_student_frame, text="Address", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        address_label.grid(row=4, column=0, padx=6, pady=10, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # for radio buttons
        # variable for radio button

        # fro take photo button
        radio_button1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo sample", value="Yes")
        radio_button1.grid(row=5, column=0)

        # for do not take photo button

        # variable for button 2

        radio_button2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Do Not Take Photo sample", value="No")
        radio_button2.grid(row=5, column=1)

        btn_frme = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frme.place(x=0, y=260, width=740, height=40)

        # save button
        save_btn = Button(btn_frme, command=self.add_data, text="Save", width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        save_btn.grid(row=0, column=0)

        # Update button
        update_btn = Button(btn_frme, command=self.update_data, text="Update", width=11, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        update_btn.grid(row=0, column=1)

        # delete buttn
        delete_btn = Button(btn_frme, command=self.delete_data, text="Delete", width=11, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        delete_btn.grid(row=0, column=2)

        # Reset  button

        reset_btn = Button(btn_frme, text="Reset", command=self.reset_data, width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        reset_btn.grid(row=0, column=3)

        # Take photo sample
        take_photo_btn = Button(btn_frme, command=self.generate_dataset, text="Take Photo Sample", width=16, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        take_photo_btn.grid(row=0, column=4)

        # udate photo sample

        update_photo_btn = Button(btn_frme, text="Update Photo Sample", width=17, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        update_photo_btn.grid(row=0, column=5)

        # Right frame

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

        # ==============  Search system ==========================

        # search frame
        search_frame = LabelFrame(
            Right_frame, bd=2, relief=RIDGE, text="Search System", font=(
                "'Fredoka One', sans-serif", 11, "bold"), fg="blue")
        search_frame.place(x=0, y=135, width=745, height=70)

        # search label
        search_label = Label(search_frame, text="Search By", font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        search_label.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        # Search combo box

        # course_frame = Label(current_course_frame, text="Course", font=(
        #     "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        # course_frame.grid(row=0, column=2, padx=0, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "'Fredoka One', sans-serif", 11, "bold"), state="readonly", width=17)
        search_combo["values"] = ("Select",
                                  "Roll_No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=6, pady=10, sticky=W)

        # for search entry
        Search_entry = ttk.Entry(search_frame, width=20, font=(
            "'Fredoka One', sans-serif", 11, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        # for buton
        # search button
        search_btn = Button(search_frame, text="Search", width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        search_btn.grid(row=0, column=3, padx=5, pady=10)

        # Show all button
        showall_btn = Button(search_frame, text="Show All", width=10, font=(
            "'Fredoka One', sans-serif", 11, "bold"), fg="Green")
        showall_btn.grid(row=0, column=4, padx=5, pady=10)

        # ================== table frame ======================
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=210, width=745, height=300)

        # for horizontal and vertical scrolbar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Dep", "Course", "Year", "Semester", "Student_Id", "Name", "Divisions", "Roll",
                                                               "Gender", "Dob", "Email", "Phone", "Address", "Teacher", "PhotoSample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student_Id", text="StudentId")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Divisions", text="Division")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Dob", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("PhotoSample", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=120)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=80)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student_Id", width=80)
        self.student_table.column("Name", width=100)
        self.student_table.column("Divisions", width=80)
        self.student_table.column("Roll", width=80)
        self.student_table.column("Gender", width=80)
        self.student_table.column("Dob", width=100)
        self.student_table.column("Email", width=120)
        self.student_table.column("Phone", width=80)
        self.student_table.column("Address", width=130)
        self.student_table.column("Teacher", width=80)
        self.student_table.column("PhotoSample", width=80)

        self.student_table.pack(fill=BOTH, expand=1)

        self.fetch_data()
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        # =================== function decleration ==================

        # ======================== function for add data =======================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Duo To :{str(es)}", parent=self.root)

            # ================ fetch data to our right frame table ========================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select *from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(
                *self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===================== function cursor to fetch datafrom  table of right side

    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ================ Update function ===================

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details added seccessfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # ============= Delete function =====================

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student delete page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id=%s"
                    val = (self.var_std_id.get())
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To : {str(es)}", parent=self.root)

    # ================ Reset button function ======================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


# =============== Generate data set =============================


    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Akhil@9369229439", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1
                        my_cursor.execute(
                            "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s", (
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get() == id+1
                            ))

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

# <-------------------  to load preddefiend data on face frontals from opencv------------------->
                    face_classifier = cv2.CascadeClassifier(
                        "haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scalling factor for face frame = 1.3
                        # minimum neighbour = 5
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y+h, x:x+w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(
                                face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + \
                                str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50),
                                        cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo(
                        "Result", "Generating data sets completed")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
