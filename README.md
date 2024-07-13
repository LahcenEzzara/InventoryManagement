# Inventory Management System Django

## Project Overview
**Project Name**: Inventory Management System Django  
**Technologies Used**: Python with Django Web Framework  
**Database**: SQLite  
**Type**: Web Application  
**Developer**: Lahcen

## Instructions: How to Run?

### Step 1: Download and Unzip the Project
After you finish downloading the project, unzip the project file and navigate to the project root folder.

### Step 2: Create and Activate a Virtual Environment (Optional but Recommended)
Creating a virtual environment is a good practice to manage dependencies. You can create and activate a virtual environment using the following commands:

```sh
# Create a virtual environment
python -m venv env

# Activate the virtual environment (Windows)
env\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source env/bin/activate
```

### Step 3: Install the Requirements
Open your Terminal/Command Prompt in the project's root folder and install the required packages using:

```sh
Copy code
pip install -r requirements.txt
```

### Step 4: Make Database Migrations
Run the following commands to make and apply the database migrations:

```sh
Copy code
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Application
After a successful migration, start the Django development server with:

```sh
Copy code
python manage.py runserver
```

### Step 6: Open the Application in a Web Browser
Open your favorite web browser and go to the following URL:

```sh
http://127.0.0.1:[PORT_NUMBER]/
```

### Step 7: Create Admin Login Credentials
For the Admin Login credentials, you need to create a superuser. Run the following command and follow the prompts to create a superuser:

```sh
Copy code
python manage.py createsuperuser
```

### Additional Information
And there you have it, a full setup of the Inventory Management System project in Django. At first, all you need to have is Python and Django installed on your local machine, whereas the remaining modules are listed in the requirements.txt file. Still, the versions may vary according to different project requirements.

You can use Python virtual environments to manage dependencies. Also, you can download the free Inventory Management System Project in Python Django source code from this repo.

This Online Inventory System in Django is a fully functional project for all beginners. Indeed, it helps to broaden vast knowledge into such Django web applications. In conclusion, this whole Django project with free source code is an absolute project and a meaningful way for the users to learn and explore more about it.