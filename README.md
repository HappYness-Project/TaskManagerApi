## Testing Instructions

1. **Start the Docker Compose Environment**
   - From the root directory of the project, run the following command:
     ```sh
     docker-compose up
     ```

2. **Run Database Migrations**
   - Access the Docker container's shell:
     ```sh
     docker exec -it task_management-web-1 bash
     ```
   - Inside the Docker shell, run the migrations:
     ```sh
     python manage.py migrate
     ```
   - Ensure PostgreSQL is installed and running within the container.
