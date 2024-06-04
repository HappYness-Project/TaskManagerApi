FROM python:3.10
WORKDIR /usr/src/app

# Allows docker to cache installed dependencies between builds
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . /usr/src/app/

EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# runs the production server
# ENTRYPOINT ["python", "task_management/manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]
