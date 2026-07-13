# 🚀 FastAPI Advanced Boilerplate

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-00a393?logo=fastapi&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-Database-orange)
![Redis](https://img.shields.io/badge/Redis-Caching-red?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package_Manager-purple)
![Pytest](https://img.shields.io/badge/Pytest-Testing-yellow?logo=pytest&logoColor=white)

A production-ready, highly scalable, and fully asynchronous REST API boilerplate built with **FastAPI**. This template incorporates modern Python backend best practices, including robust authentication, Role-Based Access Control (RBAC), Redis caching, async database operations, and a comprehensive test suite.

## ✨ Features

* **Fully Asynchronous:** Async database operations (SQLAlchemy/SQLModel) and async route handlers.
* **Modern ORM:** Built with [SQLModel](https://sqlmodel.tiangolo.com/) (combining Pydantic and SQLAlchemy).
* **Robust Security:**
  * **UUIDs** as primary keys to prevent ID enumeration (IDOR attacks).
  * Password hashing using `pwdlib`.
  * CORS middleware and global exception handling (e.g., database integrity errors).
* **Database Migrations:** Pre-configured with **Alembic** for seamless schema updates.
* **Authentication & Authorization:** 
  * JWT-based authentication (Access & Refresh tokens).
  * OAuth2 Password bearer flow.
  * Role-Based Access Control (RBAC) via dynamic dependency injection.
* **Caching:** Built-in Redis caching via `fastapi-cache2` with custom key builders for paginated data.
* **Testing:** Comprehensive async testing setup using `pytest`, `httpx`, and in-memory SQLite (bypassing Redis during tests).
* **Email Integration:** SMTP configuration ready for background email processing.
* **Modern Environment:** Fully dockerized and managed with **`uv`**, the ultra-fast Python package manager.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL (Production) / SQLite (Testing)
* **Migrations:** Alembic
* **Caching:** Redis
* **Authentication:** PyJWT, pwdlib
* **Testing:** Pytest, HTTPX
* **Infrastructure:** Docker, Docker Compose, `uv`

## 📂 Project Structure

```text
├── app/
│   ├── api/            # API Routers and Dependencies (v1)
│   ├── core/           # Config, Security, Logging, Exceptions, Emails
│   ├── crud/           # Generic & Specific CRUD operations
│   ├── db/             # Database session creation and initialization
│   ├── models/         # SQLModel database models & Enums
│   ├── schemas/        # Pydantic models for request/response validation
│   └── main.py         # FastAPI application instance & lifespan
├── migrations/         # Alembic database migrations
├── tests/              # Pytest async test suite
├── create_superuser.py # CLI script to bootstrap an admin user
├── docker-compose.yml  # Multi-container orchestration
└── pyproject.toml      # 'uv' dependencies and metadata
```

## 🚀 Getting Started (Docker Flow)

The easiest and recommended way to run this project is using Docker.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### 2. Environment Variables
Create a `.env` file in the root directory by copying the example:
```bash
cp .env.example .env
```
*(The default values in `.env.example` are already configured to work seamlessly with the included Docker Compose setup).*

### 3. Spin up the Infrastructure
Start the API, PostgreSQL, and Redis containers in the background:
```bash
docker compose up -d
```

### 4. Run Database Migrations
Apply the initial database schema using Alembic (runs inside the container via `uv`):
```bash
docker compose exec api uv run alembic revision --autogenerate -m "init"
docker compose exec api uv run alembic upgrade head
```

### 5. Create the Initial Superuser
Inject the first admin user into the database:
```bash
docker compose exec api uv run python create_superuser.py
```

## 📚 API Documentation

Once the server is running, FastAPI automatically generates interactive API documentation:
* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **OpenAPI JSON:** [http://localhost:8000/api/v1/openapi.json](http://localhost:8000/api/v1/openapi.json)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧪 Running Tests

The test suite is built with `pytest` and uses an isolated, in-memory SQLite database. It automatically mocks the Redis connection to prevent conflicts during CI/CD.

Run the tests inside the container:
```bash
docker compose exec api uv run pytest
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
