"""
PEARL HOSPITAL MANAGEMENT SYSTEM 
"""

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as sqlcon
import random as rd
import getpass

#  PASSWORD ASKING 
print(" Database login required")
db_pass = getpass.getpass("Enter MySQL root password: ")

#  DATABASE 
con = sqlcon.connect(host="localhost", user="root", password=db_pass)
cur = con.cursor(buffered=True)

cur.execute("CREATE DATABASE IF NOT EXISTS Hospital")
cur.execute("USE Hospital")

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS appointment(
        idno VARCHAR(12) PRIMARY KEY,
        name VARCHAR(50),
        age VARCHAR(3),
        gender VARCHAR(1),
        phone VARCHAR(10),
        bg VARCHAR(3)
    )
    """
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS appointment_details(
        idno VARCHAR(12) PRIMARY KEY,
        doctor VARCHAR(50),
        date VARCHAR(20),
        time VARCHAR(20),
        appointment_no VARCHAR(10)
    )
    """
)



#  MAIN APP 
class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PEARL HOSPITAL — Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#EB4C4C")

        self.setup_style()
        self.build_layout()

    #  STYLE 
    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure("Sidebar.TButton", font=("Segoe UI", 10, "bold"), padding=10)
        style.configure("Header.TLabel", font=("Segoe UI", 22, "bold"))

    #  LAYOUT 
    def build_layout(self):
        header = ttk.Label(
            self.root,
            text=" PEARL HOSPITAL MANAGEMENT SYSTEM",
            style="Header.TLabel",
            background="#0b5ed7",
            foreground="white",
            anchor="center",
        )
        header.pack(fill="x")

        container = tk.Frame(self.root, bg="#EB4C4C")
        container.pack(fill="both", expand=True)

        # Sidebar
        sidebar = tk.Frame(container, bg="#1f2a44", width=220)
        sidebar.pack(side="left", fill="y")

        # Main area
        self.main_area = tk.Frame(container, bg="#EB4C4C")
        self.main_area.pack(side="right", fill="both", expand=True)

        buttons = [
            ("Registration", self.show_registration),
            ("Appointment", self.show_appointment),
            ("View Patient", self.show_search),
            ("Modify Data", self.show_modify),
            ("Doctors List", self.show_doctors),
            ("Services", self.show_services),
            ("Exit", self.root.destroy),
        ]

        for text, cmd in buttons:
            ttk.Button(sidebar, text=text, style="Sidebar.TButton", command=cmd).pack(
                fill="x", padx=10, pady=8
            )

        self.show_welcome()

    #  UTIL 
    def clear_main(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_main()

        # Hero Title
        ttk.Label(
            self.main_area,
            text="Welcome to Pearl Hospital",
            font=("Segoe UI", 26, "bold"),
        ).pack(pady=(30, 5))

        # Tagline placeholder
        ttk.Label(
            self.main_area,
            text="Healing with Heart, Right from the Start.",
            font=("Segoe UI", 12, "italic"),
            foreground="#444",
        ).pack(pady=(0, 25))

        # ---------- Dashboard Cards ----------
        card_frame = tk.Frame(self.main_area, bg="#EB4C4C")
        card_frame.pack(pady=10)

        cards = [
            ("👨‍⚕️ Doctors", "14 Available"),
            ("🧪 Services", "9 Active"),
            ("📅 Appointments", "Book Anytime"),
            ("🏥 Status", "System Online"),
        ]

        for i, (title, value) in enumerate(cards):
            card = tk.Frame(
                card_frame,
                bg="white",
                bd=1,
                relief="solid",
                width=180,
                height=110,
            )
            card.grid(row=0, column=i, padx=15, pady=10)
            card.pack_propagate(False)

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 11, "bold"),
                bg="white",
            ).pack(pady=(15, 5))

            tk.Label(
                card,
                text=value,
                font=("Segoe UI", 12),
                bg="white",
                fg="#0b5ed7",
            ).pack()
        ttk.Label(
            self.main_area,
            text="Welcome to Pearl Hospital System",
            font=("Segoe UI", 20, "bold"),
        ).pack(pady=40)

    
    #  REGISTRATION 
     
    def show_registration(self):
        self.clear_main()

        labels = [
            "Aadhar No",
            "Name",
            "Age",
            "Gender (M/F)",
            "Phone",
            "Blood Group",
        ]

        self.reg_entries = []

        for i, text in enumerate(labels):
            ttk.Label(self.main_area, text=text).grid(row=i, column=0, padx=20, pady=10)
            e = ttk.Entry(self.main_area, width=30)
            e.grid(row=i, column=1)
            self.reg_entries.append(e)

        ttk.Button(self.main_area, text="Register", command=self.register_user).grid(
            row=6, columnspan=2, pady=20
        )

    def register_user(self):
        data = [e.get().strip() for e in self.reg_entries]

        if "" in data:
            messagebox.showwarning("Error", "All fields required")
            return

        if len(data[4]) != 10 or not data[4].isdigit():
            messagebox.showwarning("Error", "Phone must be 10 digits")
            return

        try:
            cur.execute(
                "INSERT INTO appointment VALUES (%s,%s,%s,%s,%s,%s)",
                tuple(data),
            )
            con.commit()
            messagebox.showinfo("Success", "Registration Complete")
        except sqlcon.Error:
            messagebox.showerror("Error", "Aadhar already registered")

    
    #  APPOINTMENT 
  
    def show_appointment(self):
        self.clear_main()

        ttk.Label(self.main_area, text="Aadhar No").grid(row=0, column=0, pady=10)
        self.app_id = ttk.Entry(self.main_area)
        self.app_id.grid(row=0, column=1)

        ttk.Label(self.main_area, text="Department (1-6)").grid(row=1, column=0)
        self.dep = ttk.Entry(self.main_area)
        self.dep.grid(row=1, column=1)

        ttk.Label(self.main_area, text="Date (DD-MM-YYYY)").grid(row=2, column=0)
        self.date = ttk.Entry(self.main_area)
        self.date.grid(row=2, column=1)

        ttk.Label(self.main_area, text="Time (24hr)").grid(row=3, column=0)
        self.time = ttk.Entry(self.main_area)
        self.time.grid(row=3, column=1)

        ttk.Button(self.main_area, text="Book Appointment", command=self.book).grid(
            row=4, columnspan=2, pady=20
        )

    def book(self):
        idno = self.app_id.get().strip()
        dep = self.dep.get().strip()
        date = self.date.get().strip()
        time = self.time.get().strip()

        cur.execute("SELECT * FROM appointment WHERE idno=%s", (idno,))
        if not cur.fetchone():
            messagebox.showerror("Error", "Patient not registered")
            return

        doctors = {
            "1": ["Dr. Sharma", "Dr. Verma"],
            "2": ["Dr. Sidharth", "Dr. Tendulkar"],
            "3": ["Dr. Kumar", "Dr. Khan"],
            "4": ["Dr. Virat", "Dr. Leo"],
            "5": ["Dr. Kohli", "Dr. Singh"],
            "6": ["Dr. Irfan", "Dr. John", "Dr. Sanjay", "Dr. Shahid"],
        }

        if dep not in doctors:
            messagebox.showerror("Error", "Invalid department")
            return

        doctor = rd.choice(doctors[dep])
        app_no = str(rd.randint(1000, 9999))

        try:
            cur.execute(
                "INSERT INTO appointment_details VALUES (%s,%s,%s,%s,%s)",
                (idno, doctor, date, time, app_no),
            )
            con.commit()
        except sqlcon.Error:
            messagebox.showerror("Error", "Appointment already exists")
            return

        messagebox.showinfo("Success", f"Doctor: {doctor}\nToken: {app_no}")

   
    #  SEARCH

    def show_search(self):
        self.clear_main()

        ttk.Label(self.main_area, text="Enter Aadhar").pack(pady=10)
        self.search_id = ttk.Entry(self.main_area)
        self.search_id.pack()

        ttk.Button(self.main_area, text="Search", command=self.search).pack(pady=10)

    def search(self):
        pid = self.search_id.get().strip()
        cur.execute("SELECT * FROM appointment WHERE idno=%s", (pid,))
        data = cur.fetchone()

        if not data:
            messagebox.showerror("Error", "No data found")
            return

        messagebox.showinfo("Patient Data", str(data))


    #  MODIFY

    def show_modify(self):
        self.clear_main()

        ttk.Label(self.main_area, text="Aadhar No").grid(row=0, column=0, pady=10)
        self.mod_id = ttk.Entry(self.main_area)
        self.mod_id.grid(row=0, column=1)

        ttk.Label(self.main_area, text="Field").grid(row=1, column=0)
        self.field = ttk.Combobox(
            self.main_area, values=["name", "age", "gender", "phone", "bg"]
        )
        self.field.grid(row=1, column=1)

        ttk.Label(self.main_area, text="New Value").grid(row=2, column=0)
        self.new_val = ttk.Entry(self.main_area)
        self.new_val.grid(row=2, column=1)

        ttk.Button(self.main_area, text="Update", command=self.modify).grid(
            row=3, columnspan=2, pady=20
        )

    def modify(self):
        pid = self.mod_id.get().strip()
        field = self.field.get()
        value = self.new_val.get().strip()

        cur.execute(f"UPDATE appointment SET {field}=%s WHERE idno=%s", (value, pid))
        con.commit()
        messagebox.showinfo("Success", "Data Updated")


    #  DOCTORS

    def show_doctors(self):
        self.clear_main()

        doctors = [
            ("Dr. Sharma", "Orthopaedic", 10),
            ("Dr. Verma", "Orthopaedic", 11),
            ("Dr. Kumar", "Nephrologist", 12),
            ("Dr. Khan", "Nephrologist", 13),
            ("Dr. Kohli", "Gynaecologist", 14),
            ("Dr. Singh", "Gynaecologist", 15),
        ]

        tree = ttk.Treeview(self.main_area, columns=("Name", "Dept", "Room"), show="headings")
        tree.pack(fill="both", expand=True)

        for col in ("Name", "Dept", "Room"):
            tree.heading(col, text=col)

        for d in doctors:
            tree.insert("", "end", values=d)


    #  SERVICES

    def show_services(self):
        self.clear_main()

        services = [
            ("Ultrasound", 1),
            ("X-Ray", 2),
            ("CT Scan", 3),
            ("MRI", 4),
            ("Blood Collection", 5),
        ]

        tree = ttk.Treeview(self.main_area, columns=("Service", "Room"), show="headings")
        tree.pack(fill="both", expand=True)

        tree.heading("Service", text="Service")
        tree.heading("Room", text="Room")

        for s in services:
            tree.insert("", "end", values=s)


#  RUN 
root = tk.Tk()
app = HospitalApp(root)
root.mainloop()
