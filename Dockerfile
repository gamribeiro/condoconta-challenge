# Use the official Python base image
FROM python:3.8.6

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port the Flask app runs on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
