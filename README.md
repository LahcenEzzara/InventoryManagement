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

Create a virtual environment :
```bash
python -m venv env
```

Activate the virtual environment (Windows) :
```bash
env\Scripts\activate
```

Activate the virtual environment (macOS/Linux) :
```bash
source env/bin/activate
```

### Step 3: Install the Requirements
Open your Terminal/Command Prompt in the project's root folder and install the required packages using:

```bash
pip install -r requirements.txt
```

### Step 4: Make Database Migrations
Run the following commands to make and apply the database migrations:

```bash
python manage.py makemigrations
```

then :
```bash
python manage.py migrate
```

### Step 5: Run the Application
After a successful migration, start the Django development server with:

```bash
python manage.py runserver
```

### Step 6: Open the Application in a Web Browser
Open your favorite web browser and go to the following URL:

```bash
http://127.0.0.1:[PORT_NUMBER]/
```

### Step 7: Create Admin Login Credentials
For the Admin Login credentials, you need to create a superuser. Run the following command and follow the prompts to create a superuser:

```bash
python manage.py createsuperuser
```