# To-Do Flask App

A simple Flask-based to-do application that lets users manage tasks with create, read, update, and delete operations. The app uses Flask, Flask-SQLAlchemy, Flask-WTF, and SQLite for data persistence.

## Features

- View all tasks on the home page
- Add new tasks
- Edit existing tasks
- Delete tasks
- Form validation and CSRF protection
- Persistent storage using SQLite

## Project Structure

- app.py — creates the Flask app, configures the database, and starts the server
- routes.py — defines the application routes for listing, adding, editing, and deleting tasks
- forms.py — contains the WTForms classes used for task input and delete confirmation
- models.py — defines the Task database model
- templates/ — HTML templates used by the app
- instance/ — application instance folder
- requirements.txt — Python dependencies
- Dockerfile — container setup for running the app in Docker

## Prerequisites

Make sure the following are installed:

- Python 3.10+
- pip
- Docker (optional, for containerized usage)

## Run the App with Flask

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:

   ```bash
   python app.py
   ```

4. Open the app in your browser:

   - Flask server: <http://127.0.0.1:5000>
   - Or: <http://localhost:5000>

The app will automatically create the SQLite database when it starts.

## Run the App with Docker

### Build the Docker image

```bash
docker build -t todo-flask-app .
```

### Run the Docker container

```bash
docker run -p 5000:5000 --name todo-flask-app todo-flask-app
```

### Access the app

Open your browser and go to:

- Flask server: <http://127.0.0.1:5000>
- Or: <http://localhost:5000>

### Stop or remove the container

```bash
docker stop todo-flask-app
docker rm todo-flask-app
```

## Notes

- The app runs on port 5000 by default.
- If you want to access it from another machine on the same network, use the server IP address followed by port 5000.
- The SQLite database file is created as data.db in the project directory.
