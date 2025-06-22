# Contact Agenda Microservices API
This project is a simple microservices API for managing contacts using FastAPI, PostgreSQL, and GraphQL (via Strawberry). It includes REST and GraphQL endpoints.

## Requirements
- `Docker`
- `Docker Compose`

## Setup and Run
Clone the repository

```
git clone <your-repo-url>
cd <your-repo-folder>
```

## Create .env file

Create a .env file in the project root with the following content:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=agenda
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://user:password@db:5432/agenda
```
## Start services with Docker Compose
```
docker compose up --build
```
This will start three containers:

- `db`: PostgreSQL database

- `api`: FastAPI application

- `tester`: Runs the test script against the API

## Access the API

- REST endpoints available at: http://localhost:8000/contacts/

- GraphQL playground at: http://localhost:8000/graphql

## Run tests

Tests run automatically in the tester container when starting with Docker Compose. You can check the logs with:
```
docker logs agenda_test_runner
```
Or enter the tester container to run tests manually:
```
docker exec -it agenda_test_runner sh
python test_script.py
```

## Project Structure
`/app:` FastAPI backend source code

`/tests:` Test scripts using HTTP requests

`docker-compose.yml:` Docker Compose config

`.env:` Environment variables for database connection
