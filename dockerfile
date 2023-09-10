# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY todo_app.py /app/todo_app.py


# Specify the command to run your application
CMD ["python", "todo_app.py"]
