# DevTrack

DevTrack is a production-oriented project management backend built with FastAPI.

The project starts as a simple CRUD-based REST API and is designed to evolve gradually into a scalable backend system with authentication, authorization, background processing, real-time communication, observability, CI/CD, and AI-powered features.

## Project Goals

The main goal of DevTrack is to explore and implement modern backend engineering concepts using Python and FastAPI in a real-world project.

Rather than building a large system from the beginning, DevTrack is developed incrementally. Each stage introduces new backend concepts and technologies.

## Planned Features

- Project management
- Task management
- User management
- Authentication and authorization
- Role-based access control (RBAC)
- PostgreSQL database
- SQLAlchemy ORM
- Database migrations with Alembic
- Search, filtering, sorting, and pagination
- Automated testing with Pytest
- Redis caching
- Background jobs
- WebSocket-based real-time updates
- Audit logging
- Rate limiting
- Structured logging
- Metrics and monitoring
- OpenTelemetry tracing
- Docker and Docker Compose
- CI/CD with GitHub Actions
- AI-powered project assistant
- Retrieval-Augmented Generation (RAG)
- GitHub integration

## Technology Stack

The technology stack will evolve throughout the development of the project.

### Current

- Python
- FastAPI
- Pydantic

### Planned

- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- Celery
- Pytest
- Docker
- GitHub Actions
- Prometheus
- Grafana
- OpenTelemetry
- pgvector
- LLM / RAG

## Architecture

The architecture will evolve gradually as new requirements and technologies are introduced.

Initial architecture:

```text
Client
  |
  v
FastAPI
  |
  v
Service Layer
  |
  v
Database Layer
  |
  v
PostgreSQL


# PostgreSQL + Docker + Python

A simple development setup for running PostgreSQL with Docker and connecting to it from Python using `psycopg2`.

## 1. Project Structure

```text
project/
├── docker-compose.yml
├── app/
│   └── main.py
└── .env
```

## 2. Docker Compose

Create `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:17
    container_name: my-postgres
    restart: unless-stopped

    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myproject

    ports:
      - "5432:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Start PostgreSQL:

```bash
docker compose up -d
```

Check the container:

```bash
docker ps
```

## 3. Test PostgreSQL

Access PostgreSQL inside the container:

```bash
docker exec -it my-postgres psql -U postgres -d myproject
```

Test:

```sql
SELECT version();
```

Exit:

```sql
\q
```

## 4. Install Psycopg2

```bash
pip install psycopg2-binary
```

## 5. Connect Python to PostgreSQL

```python
import psycopg2

with psycopg2.connect(
    database="myproject",
    user="postgres",
    password="password",
    host="127.0.0.1",
    port="5432",
) as conn:

    with conn.cursor() as cursor:
        cursor.execute("SELECT version()")
        print("Connection established!")
        print(cursor.fetchone())
```

Run:

```bash
python app/main.py
```

## 6. Environment Variables

For real projects, don't hard-code database credentials.

`.env`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=my-secret-password
POSTGRES_DB=myproject
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

Add `.env` to `.gitignore`:

```gitignore
.env
```

## 7. Docker-to-Docker Connection

If both FastAPI and PostgreSQL run inside Docker, use the **service name** as the host:

```python
conn = psycopg2.connect(
    database="myproject",
    user="postgres",
    password="password",
    host="postgres",
    port="5432",
)
```

### Important

| Python location           | PostgreSQL host |
| ------------------------- | --------------- |
| Python running on your OS | `127.0.0.1`     |
| Python running in Docker  | `postgres`      |

## 8. Useful Commands

```bash
# Start
docker compose up -d

# Stop
docker compose down

# View logs
docker compose logs postgres

# PostgreSQL shell
docker exec -it my-postgres psql -U postgres -d myproject

# Remove containers + volume
docker compose down -v
```

> **Note:** `docker compose down -v` deletes the PostgreSQL data volume. Use it carefully.

### Next Step

For a FastAPI project, the recommended progression is:

```text
PostgreSQL
    ↓
psycopg2
    ↓
SQL
    ↓
SQLAlchemy 2.0
    ↓
Alembic
    ↓
FastAPI + Pydantic
    ↓
CRUD API
```
