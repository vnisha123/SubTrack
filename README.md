# Subscription Tracker API

A robust RESTful API built with **Python** and **FastAPI** to help users track their subscriptions. 

This project features secure user authentication, JWT token-based authorization, and full CRUD operations, all backed by a **PostgreSQL** database.

---

## Features

* **User Authentication:** Secure signup and login using `pwdlib` (Argon2) for password hashing and JWT tokens for session management.
* **Subscription Management (CRUD):** Users can create, read, update, and delete their subscriptions.
* **Data Validation:** Request and response schemas enforced via `Pydantic v2`.
* **Relational Database:** Organized PostgreSQL database schema managed through `SQLAlchemy` ORM.


---

## Tech Stack

* **Framework:** FastAPI
* **ASGI Server:** Uvicorn
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens) & Argon2


---

## Setup and Installation

Follow these steps to configure the environment and run the application locally:

### 1. Environment Variables Configuration
Create a file named `.env` in the root folder of your project and add your database and authentication secrets:

```env
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/db_name
SECRET_KEY=secret_jwt_signing_key
```

## Dependency Installation

### Create and activate a virtual environment
*  **`python -m venv venv`**
*  **`venv\Scripts\activate`** (for windows)

### Install system dependencies
*  **`pip install -r requirements.txt`**

### 3. Starting the Application
* Launch the local development server using Uvicorn:
**`uvicorn main:app --reload`**


