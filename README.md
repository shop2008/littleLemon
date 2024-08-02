# Little Lemon

Welcome to the Little Lemon project! This is a Django-based web application.

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

2. **Install Dependencies:**

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Apply Migrations:**

   ```bash
   python3 manage.py migrate
   ```

4. **Create a Superuser (Optional):**

   ```bash
   python3 manage.py createsuperuser
   ```

## Running the Application

To start the development server, run:

```bash
python3 manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.
