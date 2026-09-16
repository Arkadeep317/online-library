# 📚 Library Management System

<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white" />
  <img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" />
  <img src="https://img.shields.io/badge/pythonanywhere-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515" />
</p>

---

## 📖 Project Description

The **Library Management System** is a web-based application built using Django that efficiently manages users, books, and borrowing records.

It simulates real-world library operations with features like **dynamic fine calculation**, **book availability tracking**, and a **structured CRUD system** with a clean UI and scalable backend architecture.

---

## 📑 Table of Contents

* [Features](#-features)
* [Advanced Settings](#-advanced-settings)
* [User Experience](#-user-experience)
* [Security & Stability](#-security--stability)
* [SEO & Optimization](#-seo--optimization)
* [Tech Stack](#-tech-stack)
* [System Architecture](#-system-architecture)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Application Flow](#-application-flow)
* [Future Enhancements](#-future-enhancements)
* [Sponsor](#-sponsor)

---

## 🚀 Features

### 📌 Core Features

* User Management (Add, Edit, Delete, View Details)
* Book Management (CRUD operations)
* Borrow & Return System
* Open Records (Active borrowings)
* Closed Records (Returned books)

---

### 💰 Fine System (Dynamic)

* ₹2 per day after 7 days
* Calculated **dynamically (not stored in DB)**
* Logic:

  * Uses **current date** for open records
  * Uses **return_date** for closed records
* Always up-to-date and accurate

---

### 📚 Book Management Enhancements

* Book Availability Tracking
  `Available = Stock - Borrowed (Open Records)`
* Prevent borrowing when stock is unavailable

---

### 🧠 Smart Validations

* Prevent borrowing when book is out of stock
* Backend-controlled fields (status, issue_date, return_date)
* Form validation using Django ModelForms

---

### 🎨 UI Features

* Clean table-based layout
* Separate pages for Add / Edit / Detail views
* Reusable layout using `base.html`
* Simple and intuitive navigation

---

## ⚙️ Advanced Settings

* Status handled internally (not exposed in forms)
* Automatic `issue_date` generation
* `return_date` updated only during return action
* Fine calculated using model method (`calculate_fine()`)
* Optimized queries using Django ORM

---

## 🎨 User Experience

* Minimal and clean UI
* Consistent layout using `base.html`
* Easy navigation across modules
* Structured data display in tables
* Beginner-friendly and intuitive design

---

## 🔐 Security & Stability

* CSRF protection enabled in all forms
* Django ORM prevents SQL injection
* Backend-controlled business logic
* Safe date/time handling using Django utilities
* Validated form inputs

---

## ⚡ SEO & Optimization

* Lightweight templates
* Reusable base layout
* Efficient database queries
* Scalable project structure

---

## 🧰 Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Django

### Database

* MySQL
* MariaDB 

---

## 🏗 System Architecture

```
User → Template (HTML)
        ↓
      Views
        ↓
      Forms
        ↓
      Models
        ↓
     Database
```

---

## 📂 Project Structure

```
librarymanagement/

├── manage.py

├── myproject/
│   ├── settings.py
│   ├── urls.py

├── myapps/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py

│   ├── templates/myapps/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── users.html
│   │   ├── add_user.html
│   │   ├── edit_user.html
│   │   ├── user_detail.html
│   │   ├── books.html
│   │   ├── add_book.html
│   │   ├── edit_book.html
│   │   ├── book_detail.html
│   │   ├── borrow_book.html
│   │   ├── open_records.html
│   │   ├── closed_records.html
│   │   ├── record_detail.html

│   ├── static/myapps/
│       ├── css/
│       ├── images/

```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* Django installed

---

### Installation

```bash
git clone <your-repo-link>
cd librarymanagement
pip install django
```

---

### Run Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---


## 🔄 Application Flow

```
User visits website
↓
Navigates through dashboard
↓
Performs actions (Add User / Add Book / Borrow Book)
↓
Forms validate input
↓
Views process logic
↓
Data stored in database
↓
Results displayed in templates
```

---

## 🚀 Future Enhancements

* 📊 Admin Dashboard (analytics & reports)
* 🔔 Due date + overdue notifications
* 💳 Payment integration for fines
* 🔍 Search & filter system
* 📱 Responsive UI (mobile-friendly)
* 👤 Authentication & role-based access

---

## 🤝 Sponsor

This project is developed for learning, academic, and portfolio purposes.
Open for contributions and improvements.

---


Made  using Python & Django
By **Arkadeep Si**
