from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate):
    task = Task(
        title=task_data.title,
        completed=task_data.completed
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_tasks(db: Session):
    return db.query(Task).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(
        Task.id == task_id
    ).first()


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):
    task = get_task_by_id(db, task_id)

    if not task:
        return None

    task.title = task_data.title
    task.completed = task_data.completed

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)

    if not task:
        return None

    db.delete(task)
    db.commit()

    return task