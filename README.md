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
