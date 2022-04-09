from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1650x850+0+0")
        title = Label(self.root, text="Student Management System", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        #========== All Variables ===========
        self.Roll_No_var = StringVar()
        self.fullname_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.birth_date_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        #============ Manage Frame Section ============
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Manage_Frame.place(x=15, y=100, width=563, height=742)

        m_title = Label(Manage_Frame, text="Manage Student", bg="yellow", fg="black", font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=18, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Full Name:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.fullname_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=18, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=18, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 15, "bold"), state="readonly")
        combo_gender["values"] = ("Male", "Female")
        combo_gender.grid(row=4, column=1, padx=15, pady=35)

        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=18, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="Birth Date:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame, textvariable=self.birth_date_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=18, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="blue", fg="white", font=("times new roman", 28, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=21, height=2, font=("times new roman", 15, "bold"), relief=GROOVE)
        self.txt_Address.grid(row=7, column=1, pady=18, padx=20, sticky="w")

        #======= Btn Frame ==========
        btn_frame = Frame(Manage_Frame, bd=5, relief=RIDGE, bg="black")
        btn_frame.place(x=15, y=660, width=525)

        Addbtn = Button(btn_frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        #========= Details Frame Section ========
        Details_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="blue")
        Details_Frame.place(x=600, y=100, width=1034, height=742)

        lbl_search = Label(Details_Frame, text="Search by", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by, font=("times new roman", 13, "bold"), width=10, state="readonly")
        combo_search["values"] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=22, pady=12)
        txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=12, padx=22, sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10, pady=4, bd=5, command=self.search_data).grid(row=0, column=3, padx=20, pady=23)
        showallbtn = Button(Details_Frame, text="Show All", width=10, pady=4, bd=5, command=self.fetch_data).grid(row=0, column=4, padx=20, pady=23)

        #========== Table Frame ==========
        Table_Frame = Frame(Details_Frame, bd=7, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=0, y=95, width=1030, height=641)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, column=("roll", "fullname", "email", "gender", "contact", "birth_date", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("fullname", text="Full Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("birth_date", text="Birth Date")
        self.Student_table.heading("Address", text="Address")

        self.Student_table["show"] = "headings"
        self.Student_table.column("roll", width=15)
        self.Student_table.column("fullname", width=100)
        self.Student_table.column("email", width=180)
        self.Student_table.column("gender", width=15)
        self.Student_table.column("contact", width=80)
        self.Student_table.column("birth_date", width=50)
        self.Student_table.column("Address", width=230)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.fullname_var.get() == "":
            messagebox.showerror("Error", "All fields are required to fill !")
        else:
            con = pymysql.connect(host="localhost", user="root", password="welcome123", database="StudentMS")
            cur = con.cursor()
            cur.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                           self.fullname_var.get(),
                                                                           self.email_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.birth_date_var.get(),
                                                                           self.txt_Address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Recorded has been inserted !")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="welcome123", database="StudentMS")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        rows = contents['values']
        self.Roll_No_var.set(rows[0])
        self.fullname_var.set(rows[1])
        self.email_var.set(rows[2])
        self.gender_var.set(rows[3])
        self.contact_var.set(rows[4])
        self.birth_date_var.set(rows[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, rows[6])

    def clear(self):
        self.Roll_No_var.set("")
        self.fullname_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.birth_date_var.set("")
        self.txt_Address.delete("1.0", END)

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="welcome123", database="StudentMS")
        cur = con.cursor()
        cur.execute("update student set fullname=%s,email=%s,gender=%s,contact=%s,birth_date=%s,address=%s where roll_no=%s",(
                                                                          self.fullname_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.birth_date_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.Roll_No_var.get()
                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Recorded has been inserted !")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="welcome123", database="StudentMS")
        cur = con.cursor()
        cur.execute("delete from student where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="welcome123", database="StudentMS")
        cur = con.cursor()
        cur.execute("select * from student where " + str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()

