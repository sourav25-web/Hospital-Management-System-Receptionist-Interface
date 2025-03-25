# Hospital Management System

A modern, user-friendly Hospital Management System built with Django, designed to streamline hospital operations and improve patient care management.

## Description

This Hospital Management System is a comprehensive solution for managing hospital operations, patient records, and administrative tasks. It features a clean, intuitive interface with a modern teal/turquoise color scheme and responsive design.

## Purpose

The system was built to:
- Simplify patient registration and management
- Streamline hospital administrative tasks
- Improve patient care coordination
- Enhance the overall hospital management workflow
- Provide a user-friendly interface for both staff and patients

## Features

### Patient Management
- Patient registration with comprehensive details
- Patient history tracking
- Medical records management
- Appointment scheduling
- Patient search and filtering

### Administrative Features
- User authentication and authorization
- Role-based access control
- Admin dashboard for system management
- Data visualization and reporting

### User Interface
- Modern, responsive design
- Intuitive navigation
- Mobile-friendly layout
- Clean and professional appearance
- Teal/turquoise color scheme for visual appeal

## Technology Stack

- **Backend Framework:** Django 5.0.2
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite3
- **Additional Libraries:** python-dateutil 2.8.2

## Installation Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/sourav25-web/Hospital-Management-System-Receptionist-Interface.git
   cd HospitalManagementSystem
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # On Windows (Command Prompt)
   .\venv\Scripts\activate.bat
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage Instructions

1. **Admin Access**
   - Log in to the admin panel using your superuser credentials
   - Manage users, permissions, and system settings

2. **Patient Registration**
   - Navigate to the patient registration page
   - Fill in the required patient information
   - Submit the form to create a new patient record

3. **Patient Management**
   - View patient list
   - Search for specific patients
   - View and edit patient details
   - Manage patient appointments

4. **System Administration**
   - Monitor system usage
   - Manage user accounts
   - Configure system settings

## Project Structure

```
HospitalManagementSystem/
├── hospital_management_system/  # Main project directory
├── receptionist/               # Main application
│   ├── migrations/            # Database migrations
│   ├── static/               # Static files (CSS, JS)
│   ├── templates/           # HTML templates
│   ├── admin.py            # Admin configuration
│   ├── models.py          # Database models
│   ├── views.py          # View functions
│   └── urls.py          # URL routing
├── static/              # Global static files
├── venv/               # Virtual environment
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```