# Personal-Expense-Tracker

## Overview

The Personal Expense Tracker is a web application built with Flask for managing and tracking personal expenses. This application allows users to register, log in, and efficiently monitor their expenses. It features secure authentication and robust expense management using SQLAlchemy for database interactions and Flask-Login for user sessions.

## Features

- **User Registration and Login:** Users can create accounts and securely log in to their personal dashboard.
- **Expense Management:** Track, categorize, and manage personal expenses.
- **Secure Authentication:** Uses Flask-Login for handling user sessions and password protection.
- **Database Management:** Employs SQLAlchemy for robust database interactions and data management.

## Technologies Used

- **Flask:** Web framework for creating the application.
- **SQLAlchemy:** ORM for managing database operations.
- **Flask-Login:** Manages user sessions and authentication.
- **Werkzeug:** Provides password hashing and secure user authentication.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/personal-expense-tracker.git
   cd personal-expense-tracker
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database:**
   ```bash
   flask db upgrade
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```

## Configuration

- **Database URI:** Configure the database URI in the `.env` file.
- **Secret Key:** Set a secret key for session management in the `.env` file.

## Usage

1. **Navigate to the Web Application:**
   Open your web browser and go to `http://localhost:5000`.

2. **Register an Account:**
   Click on "Register" to create a new user account.

3. **Log In:**
   Use your credentials to log in.

4. **Track Expenses:**
   Access the expense tracker from your dashboard to add, view, and manage expenses.

