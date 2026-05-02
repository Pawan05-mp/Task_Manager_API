from fastapi import FastAPI
from app.database import engine, Base
from app.api.v1.tasks import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "Task Manager API Running"}