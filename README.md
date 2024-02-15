# Lab 28 - Class 401d24

## Project
Snacks Crud

## Author

Kaitlin Davis | February 2024

## About
The Snacks CRUD Project is a Django-based web application that allows users to manage (create, read, update, and delete) snack items. Each snack item includes a title, description, and the user who posted it. The project demonstrates the implementation of CRUD operations in Django and provides user authentication to secure access to certain features.

## Features
- User authentication for secure access to the admin panel.
- Ability to create, read, update, and delete snack items via the Django admin interface.
- Dedicated snack list and snack detail views.
- Responsive navigation bar with links to home and about pages.
- Styled with Tailwind CSS for a modern and responsive design.

## Installation

Follow these steps to set up and run the project:

1. **Clone the repository**

    ```sh
    git clone https://github.com/KaitlinDa/snacks-crud.git
    cd snacks-crud
    ```

2. **Set up the Python virtual environment**

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the requirements**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser account in Django**

    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server**

    ```sh
    python manage.py runserver
    ```

7. **Open your web browser and navigate to** `http://127.0.0.1:8000/` to explore the application.


## User Acceptance Tests
The application includes tests for verifying the correct status codes for the home and about pages and ensuring the appropriate templates are used, including the ancestor template.

## Resources
I used the help of the class demo as well as ChatGPT for this assignment. 
