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
docker-compose build

Step 3: Apply Database Migrations
docker-compose run --rm web python manage.py migrate

Step 4: Create a Superuser for Admin Access
docker-compose run --rm web python manage.py createsuperuser

Step 5: Start the Application
docker-compose up

Step 2: Build the Docker Images
docker-compose build

Step 3: Apply Database Migrations
docker-compose run --rm web python manage.py migrate

Step 4: Create a Superuser for Admin Access
docker-compose run --rm web python manage.py createsuperuser

Step 5: Start the Application
docker-compose up

## 🐳 Docker Usage Notes

- All components run inside isolated Docker containers for consistent and reproducible environments.
- The `docker-compose.yml` file includes:
  - `web` service: Runs the Django application.
  - `db` service: Runs the MySQL database server.
- Code is synchronized into the container using the volume mount: `.:/app`
- Port mapping: Port `8000` on your local machine is mapped to port `8000` inside the container.
- Uploaded media files and MySQL database data are persistent across container restarts using volume mounts.
- The application uses **Gunicorn** as the WSGI server inside the production Docker image for better performance.

---

## 🤖 Jenkins Usage Notes

- A `Jenkinsfile` is provided at the root of the project to define a basic CI/CD pipeline.
- Pipeline Stages:
  - **Checkout**: Retrieves the project source code from the repository.
  - **Build**: Builds the Docker image for the Django application.
  - **Test**: Runs Django unit tests using `python manage.py test` inside the container.
  - **Deploy**: Placeholder step for future deployment integration.
- Requirements:
  - A Jenkins server must be set up with Docker installed and configured.
- This Jenkins pipeline is intended as a template and can be extended to include additional stages such as automated deployment or notifications.


