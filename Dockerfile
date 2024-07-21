# Use the official Python image from the Docker Hub.
FROM python:3.11-slim-bullseye

# Set the working directory.
WORKDIR /code

# Copy the requirements file into the image.
COPY requirements.txt /tmp/requirements.txt

# Install the dependencies.
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/pip

# Copy the entire project into the image.
COPY . /code

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django development server.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "simuladoapp.wsgi:application"]
