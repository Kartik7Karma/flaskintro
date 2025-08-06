# Use official Python base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Flask config
ENV FLASK_APP=flaskintro
ENV FLASK_RUN_FACTORY=1
ENV FLASK_ENV=development
ENV FLASK_CONFIG=DevelopmentConfig

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --timeout=100 --retries=5 -i https://pypi.org/simple

# Copy project files
COPY . .

# Make wait-for-it executable
RUN chmod +x wait-for-it.sh

# Start the app after waiting for the database
CMD ["./wait-for-it.sh", "postgres_db:5432", "--", "flask", "run", "--host=0.0.0.0"]
