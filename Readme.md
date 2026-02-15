# 🏥 Pearl Hospital Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Status](https://img.shields.io/badge/Project-Desktop%20App-success)

---

## 📖 Overview

**Pearl Hospital Management System** is a desktop-based healthcare management application built using **Python Tkinter** and **MySQL**.
The system helps streamline hospital operations by providing an interactive GUI for patient registration, appointment booking, doctor management, and service tracking.

It demonstrates real-world database connectivity with a user-friendly desktop interface.

---

## ✨ Key Features

* 👤 Patient Registration System
* 📅 Appointment Booking with Token Generation
* 🔍 Patient Search Functionality
* ✏️ Modify Patient Records
* 👨‍⚕️ Doctors List Viewer
* 🧪 Hospital Services Viewer
* 🔐 Secure MySQL Password Prompt
* 🖥️ Clean Tkinter GUI Dashboard

---

## 🛠️ Tech Stack

| Layer     | Technology             |
| --------- | ---------------------- |
| Language  | Python                 |
| GUI       | Tkinter                |
| Database  | MySQL                  |
| Connector | mysql-connector-python |

---

## 🗄️ Database Schema

### Database: `Hospital`

#### Table: `appointment`

| Column | Type             |
| ------ | ---------------- |
| idno   | VARCHAR(12) (PK) |
| name   | VARCHAR(50)      |
| age    | VARCHAR(3)       |
| gender | VARCHAR(1)       |
| phone  | VARCHAR(10)      |
| bg     | VARCHAR(3)       |

#### Table: `appointment_details`

| Column         | Type             |
| -------------- | ---------------- |
| idno           | VARCHAR(12) (PK) |
| doctor         | VARCHAR(50)      |
| date           | VARCHAR(20)      |
| time           | VARCHAR(20)      |
| appointment_no | VARCHAR(10)      |

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the repository

```bash
git clone https://github.com/SayanMallick55/Hospital-Management-System-.git
cd Hospital-Management-System
```

---

### 🔹 2. Install required package

```bash
pip install mysql-connector-python
```

---

### 🔹 3. Requirements

Make sure you have:

* ✅ Python 3.x installed
* ✅ MySQL Server running
* ✅ MySQL root access

---

### 🔹 4. Run the application

```bash
python Pearl_Hospital.py
```

👉 The program will prompt for your **MySQL root password**.

---

## 🚀 How It Works

1. User launches the application
2. System asks for MySQL root password
3. Database and tables are auto-created
4. User can:

   * Register patients
   * Book appointments
   * View doctors
   * Modify records
   * Check services

---

## 🖥️ Application Modules

* 🏠 Dashboard
* 📝 Registration
* 📅 Appointment
* 🔎 Search Patient
* ✏️ Modify Data
* 👨‍⚕️ Doctors List
* 🧪 Services



## 🔐 Security Note

* MySQL password is securely requested using `getpass`
* Duplicate Aadhar entries are prevented
* Basic input validation implemented

---

## 🚧 Future Improvements

* Add proper login system
* Better input validation
* Export reports
* Multi-user support
* Web-based version
* Advanced UI styling

---

## 👨‍💻 Author

**Sayan Mallick**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
