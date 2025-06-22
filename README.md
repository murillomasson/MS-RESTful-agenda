# Contact Agenda Microservices API
This project is a simple microservices API for managing contacts using FastAPI, PostgreSQL, and GraphQL (via Strawberry). It includes REST and GraphQL endpoints.

## Technologies Used

- `FastAPI` for REST API
- `Strawberry` for GraphQL API
- `PostgreSQL` as database
- `SQLAlchemy` ORM
- `Docker` & `Docker Compose` for containerization

## Requirements
- `Docker`
- `Docker Compose`

## Setup and Run
Clone the repository

``` bash
git clone <your-repo-url>
cd <your-repo-folder>
```

## Create .env file

Create a .env file in the project root with the following content:
``` bash
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=agenda
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://user:password@db:5432/agenda
```
## Start services with Docker Compose
``` bash
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
``` bash
docker logs agenda_test_runner
```
Or enter the tester container to run tests manually:
``` bash
docker exec -it agenda_test_runner sh
python test_script.py
```

## Project Structure
`/app:` FastAPI backend source code

`/tests:` Test scripts using HTTP requests

`docker-compose.yml:` Docker Compose config

`.env:` Environment variables for database connection

## API Usage Examples

### REST API

**Create Contact:**

``` bash
curl -X POST "http://localhost:8000/contacts/" -H "Content-Type: application/json" -d '{
  "name": "Jane Doe",
  "category": "personal",
  "phones": [
    {"number": "555-1234", "type": "mobile"},
    {"number": "555-5678", "type": "landline"}
  ]
}'
```

**Response:**
``` json
{
  "id": 2,
  "name": "Jane Doe",
  "category": "personal",
  "phones": [
    {"id": 3, "number": "555-1234", "type": "mobile"},
    {"id": 4, "number": "555-5678", "type": "landline"}
  ]
}
```

**Get Contact by ID:**
``` bash
curl http://localhost:8000/contacts/2
```

## GraphQL API
**List Contacts Query:**
``` graphql
query {
  listContacts {
    id
    name
    category
    phones {
      number
      type
    }
  }
}
```

**Response:**
``` json
{
  "data": {
    "listContacts": [
      {
        "id": 2,
        "name": "Jane Doe",
        "category": "personal",
        "phones": [
          {"number": "555-1234", "type": "mobile"},
          {"number": "555-5678", "type": "landline"}
        ]
      }
    ]
  }
}
```

**Create Contact Mutation:**
``` graphql
mutation {
  createContact(
    name: "GraphQL User",
    category: personal,
    phones: ["mobile:77777", "landline:88888"]
  ) {
    id
    name
    category
    phones {
      number
      type
    }
  }
}
```
