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


