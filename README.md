# project
A project running Django and Postgres.
## Setup

This application is containerized using Docker, so running it is quite simple.

- Ensure Docker is installed on your local system.

- Clone the repo

**Inside the app directory:**
- Build the container through Docker: ```docker-compose build```

- Launch the container through Docker: ```docker-compose up```

- View the project in a browser: ```http://0.0.0.0:8000/draw```
