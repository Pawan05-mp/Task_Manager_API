# Task Manager API (FastAPI + PostgreSQL + JWT)
- Task CRUD Operations
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Pydantic Request Validation
- Dependency Injection using Depends()
- Clean Service + Repository Architecture
- Swagger API Documentation
- Production-ready folder structure

---

## Architecture Diagram

```text
                ┌──────────────────────┐
                │      Client          │
                │ Browser / Postman    │
                │ Frontend / Mobile    │
                └──────────┬───────────┘
                           │ HTTP Request
                           ▼
                ┌──────────────────────┐
                │   FastAPI Routes     │
                │   app/api/v1         │
                │ GET POST PUT DELETE  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Dependency Layer     │
                │ get_db()             │
                │ get_current_user()   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Pydantic Schemas     │
                │ Request Validation   │
                │ Response Models      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Service Layer        │
                │ Business Logic       │
                │ Rules + Validation   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Repository Layer     │
                │ DB Operations        │
                │ CRUD + Queries       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ SQLAlchemy ORM       │
                │ Python ↔ SQL Bridge  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ PostgreSQL Database  │
                │ users / tasks tables │
                └──────────────────────┘

Response Flow:
PostgreSQL → SQLAlchemy → Repository → Service → Route → Client
