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


# PostgreSQL Queries

This README contains the PostgreSQL commands needed to create and test the database for the **Project Management API**.

## 1. Create Database

Run this command from `psql`:

```sql
CREATE DATABASE project_manager;
```

Connect to the database:

```bash
psql -U postgres -d project_manager
```

---

## 2. Create `projects` Table

```sql
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    start_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP NOT NULL
);
```

---

## 3. Create `tasks` Table

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,

    status VARCHAR(20) NOT NULL
        CHECK (status IN ('active', 'completed', 'in_progress')),

    priority VARCHAR(20) NOT NULL
        CHECK (priority IN ('low', 'medium', 'high', 'critical')),

    due_date TIMESTAMP NOT NULL,

    CONSTRAINT fk_tasks_project
        FOREIGN KEY (project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE
);
```

---

## 4. Create Index

Index `project_id` for faster queries:

```sql
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
```

---

## 5. Insert Sample Projects

```sql
INSERT INTO projects (
    name,
    description,
    start_date,
    end_date
)
VALUES (
    'FastAPI Project',
    'Learning FastAPI with PostgreSQL',
    '2026-09-12',
    '2026-10-12'
);
```

```sql
INSERT INTO projects (
    name,
    description,
    start_date,
    end_date
)
VALUES (
    'Task Management API',
    'Build a REST API for managing projects and tasks',
    '2026-09-15',
    '2026-11-15'
);
```

---

## 6. Insert Sample Tasks

```sql
INSERT INTO tasks (
    project_id,
    name,
    description,
    status,
    priority,
    due_date
)
VALUES (
    1,
    'Connect PostgreSQL',
    'Connect FastAPI to PostgreSQL using psycopg2',
    'in_progress',
    'high',
    '2026-09-15'
);
```

```sql
INSERT INTO tasks (
    project_id,
    name,
    description,
    status,
    priority,
    due_date
)
VALUES (
    1,
    'Create CRUD endpoints',
    'Implement CRUD operations for projects',
    'active',
    'high',
    '2026-09-20'
);
```

```sql
INSERT INTO tasks (
    project_id,
    name,
    description,
    status,
    priority,
    due_date
)
VALUES (
    1,
    'Write tests',
    'Write tests for API endpoints',
    'active',
    'medium',
    '2026-09-25'
);
```

---

# 7. Read Queries

### Get all projects

```sql
SELECT * FROM projects;
```

### Get a specific project

```sql
SELECT * FROM projects WHERE id = 1;
```

### Get all tasks

```sql
SELECT * FROM tasks;
```

### Get tasks for a project

```sql
SELECT * FROM tasks WHERE project_id = 1;
```

### Get a specific task

```sql
SELECT * FROM tasks WHERE id = 1;
```

---

# 8. Join Projects and Tasks

Get projects together with their tasks:

```sql
SELECT
    p.id AS project_id,
    p.name AS project_name,
    t.id AS task_id,
    t.name AS task_name,
    t.status,
    t.priority,
    t.due_date
FROM projects p
JOIN tasks t
    ON p.id = t.project_id;
```

---

# 9. Update Queries

### Update task status

```sql
UPDATE tasks
SET status = 'completed'
WHERE id = 1;
```

### Update task priority

```sql
UPDATE tasks
SET priority = 'critical'
WHERE id = 2;
```

### Update project

```sql
UPDATE projects
SET name = 'Advanced FastAPI Project'
WHERE id = 1;
```

---

# 10. Delete Queries

### Delete a task

```sql
DELETE FROM tasks
WHERE id = 3;
```

### Delete a project

```sql
DELETE FROM projects
WHERE id = 1;
```

Because the foreign key uses:

```sql
ON DELETE CASCADE
```

deleting a project also deletes its related tasks.

---

# 11. Useful Verification Queries

Check the tables:

```sql
\dt
```

Describe a table:

```sql
\d projects
```

```sql
\d tasks
```

Check database:

```sql
SELECT current_database();
```

Check PostgreSQL version:

```sql
SELECT version();
```

Check all projects:

```sql
SELECT * FROM projects;
```

Check all tasks:

```sql
SELECT * FROM tasks;
```

---

## Database Structure

```text
project_manager
│
├── projects
│   ├── id
│   ├── name
│   ├── description
│   ├── start_date
│   └── end_date
│
└── tasks
    ├── id
    ├── project_id ──────> projects.id
    ├── name
    ├── description
    ├── status
    ├── priority
    └── due_date
```

Relationship:

```text
projects 1 ─────────── N tasks
```

This database is now ready to be connected to the FastAPI application using `psycopg2`.
