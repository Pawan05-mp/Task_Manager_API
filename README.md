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
# Task Manager API (FastAPI + PostgreSQL + JWT)

## Request Flow Example

### Create Task

```http
POST /tasks
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

```json
{
  "title": "Prepare Backend Interview",
  "completed": false
}
```

Flow:

```text
Client → Route → Depends() → Schema Validation → Service → Repository → PostgreSQL
```

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Pydantic
* Uvicorn
* Git + GitHub

---

## Run Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Why This Architecture?

Because production systems require:

* separation of concerns
* easier debugging
* testability
* scalability
* security
* maintainability

This avoids the beginner mistake of putting everything inside `main.py`.

---

## Author

M P Pawan Chander
Backend Developer | FastAPI | PostgreSQL | REST APIs

````

---

## Run Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
````

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

