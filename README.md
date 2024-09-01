# Python Django Expense Tracker

## Introduction

The Python Django Expense Tracker is a web application designed to help users manage their finances by tracking their expenses. Users can create profiles, categorize their expenses, and monitor their spending according to the categories they specify during profile creation. This application is built using the Django framework and incorporates HTML, CSS, JavaScript, and Bootstrap for the frontend.

## Features

- **User Profiles:** Users can create profiles and track expenses based on custom categories.
- **Expense Categorization:** Expenses can be categorized, making it easier to manage and review spending habits.
- **Budget Monitoring:** Users can set a budget for each project and monitor the remaining budget after expenses.
- **Detailed Dashboard:** The dashboard provides an overview of total expenses, budget left, and the number of transactions.
- **Responsive Design:** The application is fully responsive and works well on desktops, tablets, and mobile devices.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Django installed (version 3.x or higher recommended).
- Basic knowledge of Django, HTML, CSS, JavaScript, and Bootstrap.
- A code editor like Visual Studio Code, PyCharm, or Sublime Text.

## Installation

Follow these steps to set up the Django Expense Tracker project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/django-expense-tracker.git
   cd django-expense-tracker
   ```

2. **Create a Virtual Environment**

   It's recommended to create a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Django Project**

   Run the following commands to set up the project:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser  # Create an admin user
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/` in your web browser.


## Usage

1. **Creating a New Project**

   - Navigate to the "Create New Finance" page.
   - Enter the project name, budget, and categories.
   - Save the project to start tracking expenses.

2. **Adding Expenses**

   - Go to the project details page.
   - Click on "Add Expense" and fill in the details (title, amount, category).
   - Submit the form to record the expense.

3. **Viewing and Managing Expenses**

   - View the total budget, budget left, and the number of transactions on the project dashboard.
   - Review and manage expenses by category.

4. **Admin Panel**

   - Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser account created earlier.
   - Manage users, projects, categories, and expenses.

