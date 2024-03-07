# Use the official Python image with Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install -r requirements.txt
RUN pip install Flask gunicorn

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
