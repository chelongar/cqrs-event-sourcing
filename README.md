# CQRS & Event Sourcing
This repository contains a simple implementation of CQRS (Command Query Responsibility Segregation) and Event Sourcing in Python (FastAPI + SQLite).

## Features
✅ CQRS Architecture → Separates commands (writes) and queries (reads).

✅ Event Sourcing → Stores all state changes as immutable events.

✅ FastAPI (Python) → High-performance API framework.

✅ SQLite for Persistence → Lightweight, serverless database.

✅ Docker Support → Easily deployable via containers.

## 📁 Project Structure

- cqrs-event-sourcing/ (Root directory)
  - python/
    - database.py – Database setup (SQLite + SQLAlchemy)
    - models.py – User & Event models
    - events.py – Event schema (UserCreated, UserUpdated, etc.)
    - event_store.py – Stores and retrieves events from the database
    - command_handler.py – Handles commands (Create user, Update user)
    - query_handler.py – Handles queries (Get user, List users)
    - main.py – FastAPI routes and endpoints
    - requirements.txt – Project dependencies
    - Dockerfile – Docker container setup
    - docker-compose.yml – Docker Compose setup
## API Endpoints
| **Method** | **Endpoint**          | **Description**                          |
|-----------|----------------------|------------------------------------------|
| `POST`   | `/users/`             | Create a new user                       |
| `PUT`    | `/users/{user_id}`    | Update user email                       |
| `GET`    | `/users/{user_id}`    | Get user details                        |
| `GET`    | `/users/`             | List all users                          |
| `GET`    | `/events/`            | Retrieve all stored events              |

## 🐳 Running Python Application in Docker

```sh
cd cqrs-event-sourcing/python
docker-compose up --build
```

## 📂 Example of Stored Events

```json
[
  {
    "id": 1,
    "type": "UserCreated",
    "data": {
      "user_id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
    }
  },
  {
    "id": 2,
    "type": "UserEmailUpdated",
    "data": {
      "user_id": 1,
      "new_email": "john.new@example.com"
    }
  }
]
```

## 📌 Contributing
✅ Pull requests are welcome!

✅ Open an issue if you find bugs or have suggestions.

