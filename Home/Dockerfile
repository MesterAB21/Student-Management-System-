# Use official Python image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Django with Gunicorn
CMD gunicorn Home.wsgi:application --bind 0.0.0.0:8000
