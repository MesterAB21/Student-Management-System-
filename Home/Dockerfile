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

# Run migrations
RUN python manage.py migrate --noinput

# Expose port 8080 for Vercel
EXPOSE 8080

# Start Django with Gunicorn on port 8080
CMD gunicorn Home.wsgi:application --bind 0.0.0.0:8080
