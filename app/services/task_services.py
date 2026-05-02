from sqlalchemy.orm import Session
from app.repositories import task_repository
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate):
    return task_repository.create_task(db, task)


def get_tasks(db: Session):
    return task_repository.get_all_tasks(db)


def get_task(db: Session, task_id: int):
    return task_repository.get_task_by_id(db, task_id)


def update_task(
    db: Session,
    task_id: int,
    task: TaskUpdate
):
    return task_repository.update_task(
        db,
        task_id,
        task
    )


def delete_task(db: Session, task_id: int):
    return task_repository.delete_task(db, task_id)