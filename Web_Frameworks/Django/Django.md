# Django Learning Journey 🧩

Welcome to my **Django Learning Repository** — a collection of experiments, notes, and small projects as I explore the Django web framework.  
This repo documents my progress and provides quick references for setup, concepts, and useful resources.

---

## 📖 Overview

**Django** is a high-level Python web framework that encourages rapid development and clean, pragmatic design.  
It handles much of the hassle of web development so you can focus on writing your app without reinventing the wheel.

This repository includes:
- Tutorials and personal notes
- Example Django apps
- Key learnings from each module
- References to external resources and documentation

---

## 🧠 Learning Goals

- Understand the **Model-View-Template (MVT)** architecture  
- Learn to create **Django projects and apps**
- Work with **ORM (Object Relational Mapper)** for database operations  
- Implement **URL routing and views**  
- Manage **forms, authentication, and admin interface**  
- Deploy Django applications  

---

## ⚙️ Setup Instructions

To set up a Django project locally:

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Install Django
pip install django

# 4. Create a new Django project
django-admin startproject myproject

# 5. Run the server
cd myproject
python manage.py runserver
