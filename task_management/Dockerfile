FROM python:3.10
WORKDIR /usr/src/app

# Allows docker to cache installed dependencies between builds
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . .

EXPOSE 8000

# runs the production server
# ENTRYPOINT ["python", "task_management/manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]
