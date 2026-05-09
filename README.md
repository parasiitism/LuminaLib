# LuminaLib

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python FastAPI" />
  <img src="https://img.shields.io/badge/Domain-Books%20%26%20Reviews-7C3AED?style=for-the-badge" alt="Books" />
  <img src="https://img.shields.io/badge/AI-Recommendations-F97316?style=for-the-badge" alt="Recommendations" />
  <img src="https://img.shields.io/badge/Storage-SQLAlchemy%20%2B%20S3-16A34A?style=for-the-badge" alt="Storage" />
</p>

LuminaLib is a FastAPI-based book and review platform with clean architecture boundaries for authentication, books, reviews, recommendation use cases, LLM integration, and storage abstractions.

## What It Demonstrates

- FastAPI API modules for auth, books, reviews, and recommendations.
- Application use cases such as ingesting books, analyzing reviews, and recommending books.
- Domain interfaces for LLMs, recommenders, and storage.
- Infrastructure adapters for local storage, S3-style storage, mock LLMs, and Ollama.
- SQLAlchemy, Alembic, and async Postgres-ready dependencies.
- Docker and Docker Compose deployment setup.

## Architecture

```mermaid
flowchart LR
    A[API Layer] --> B[Application Use Cases]
    B --> C[Domain Interfaces]
    C --> D[LLM Adapter]
    C --> E[Storage Adapter]
    C --> F[Recommendation Engine]
    B --> G[Database]
    classDef api fill:#dbeafe,stroke:#2563eb,color:#1e3a8a,stroke-width:2px
    classDef app fill:#ede9fe,stroke:#7c3aed,color:#4c1d95,stroke-width:2px
    classDef infra fill:#dcfce7,stroke:#16a34a,color:#14532d,stroke-width:2px
    class A api
    class B,C app
    class D,E,F,G infra
```

## Repository Map

```text
app/api/                  HTTP endpoints
app/application/use_cases/ Business workflows
app/domain/               Models and interfaces
app/infrastructure/       LLM and storage adapters
app/core/                 Config, database, security, dependencies
Dockerfile                Container entry point
docker-compose.yml        Local service composition
requirements.txt          Runtime dependencies
```

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

With Docker:

```powershell
docker compose up --build
```

## Revision Notes

- Clean architecture works well when domain logic should not depend on infrastructure.
- Interfaces make it easy to swap mock LLMs, Ollama, local storage, or S3 storage.
- Recommendation systems benefit from clear separation between ingestion, analysis, and serving.

## Interview Talking Points

```text
The strongest design choice here is the separation between API, application use cases,
domain interfaces, and infrastructure adapters. That keeps the book recommendation and
review analysis logic testable while allowing LLM and storage providers to change later.
```
