from __future__ import annotations

from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


class TaskUpdate(BaseModel):
    completed: bool


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


@dataclass
class TaskStore:
    tasks: dict[int, Task]
    next_id: int = 1

    def create(self, payload: TaskCreate) -> Task:
        task = Task(id=self.next_id, title=payload.title)
        self.tasks[task.id] = task
        self.next_id += 1
        return task


def create_app() -> FastAPI:
    app = FastAPI(title="AEW E2E Task API", version="0.1.0")
    store = TaskStore(tasks={})

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
    def create_task(payload: TaskCreate) -> Task:
        return store.create(payload)

    @app.get("/tasks", response_model=list[Task])
    def list_tasks(completed: bool | None = Query(default=None)) -> list[Task]:
        tasks = list(store.tasks.values())
        if completed is None:
            return tasks
        return [task for task in tasks if task.completed is completed]

    @app.patch("/tasks/{task_id}", response_model=Task)
    def update_task(task_id: int, payload: TaskUpdate) -> Task:
        task = store.tasks.get(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        updated = task.model_copy(update={"completed": payload.completed})
        store.tasks[task_id] = updated
        return updated

    return app


app = create_app()
