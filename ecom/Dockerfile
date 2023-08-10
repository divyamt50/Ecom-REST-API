# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8080

# Run Gunicorn to serve the application
CMD ["gunicorn", "rocket.wsgi:application", "--bind", "0.0.0.0:8000"]
