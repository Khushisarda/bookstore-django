bookstore

added video below.please watch
https://github.com/user-attachments/assets/5bf7911b-288b-4687-8b69-e38f529372a6

# 📚 Bookstore Management System (Assignment 1)

## 📌 Project Overview

This project is a simple **Bookstore Management System** built using the Django framework (Python). It allows users to browse books, add them to a shopping cart (using sessions), and includes a custom administration panel for managing the book inventory. The project is fully containerized using Docker and includes a basic Jenkins pipeline definition for CI/CD.

---

## ✅ Features Implemented

### 👤 User Authentication:
- User Registration
- User Login / Logout
- Restricted access based on login status

### 🛍️ User Interface:
- View a list of all available books
- View detailed information for a single book
- Add books to a persistent shopping cart (using Django Sessions)
- View the shopping cart contents and total price

### 🛠️ Custom Admin Panel (`/custom-admin/`):
- Accessible only to staff users (`is_staff=True`)
- List all books in the inventory
- Add new books (with optional cover image upload)
- Edit existing book details (including image)
- Delete books from the inventory

> Note: Uses **Class-Based Views** and **manual HTML forms**  
> ❌ No Django Admin  
> ❌ No Django Forms

### ⚙️ DevOps:
- Dockerized environment using `Dockerfile` and `docker-compose.yml`
- Basic CI/CD pipeline defined in `Jenkinsfile`

---

## 🧰 Tech Stack

| Layer       | Technology Used                 |
|-------------|---------------------------------|
| **Backend** | Python 3.11+, Django 4.x        |
| **Frontend**| HTML5, CSS3 (Bootstrap 5)       |
| **Database**| MySQL                           |
| **WSGI**    | Gunicorn                        |
| **Images**  | Pillow                          |
| **Containers**| Docker, Docker Compose        |
| **CI/CD**   | Jenkins                         |

---

## ⚙️ Setup & Run Instructions (Using Docker Compose)

These instructions assume you have Docker and Docker Compose installed and running on your system.

### Step 1: Clone the Repository
```bash
git clone https://github.com/Khushisarda/bookstore_project.git
cd bookstore_project
Step 2: Build the Docker Images
bash
Copy
Edit
docker-compose build
Step 3: Apply Database Migrations
bash
Copy
Edit
docker-compose run --rm web python manage.py migrate
Step 4: Create a Superuser for Admin Access
bash
Copy
Edit
docker-compose run --rm web python manage.py createsuperuser
Step 5: Start the Application
bash
Copy
Edit
docker-compose up
