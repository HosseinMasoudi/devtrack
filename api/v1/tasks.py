from fastapi import FastAPI, status
from schema import Task

app = FastAPI(description="DevTrack is a production-oriented project management backend built with FastAPI.")

@app.post("/api/v1/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    return {"message": "Task created successfully", "task": task.name}

@app.get("/api/v1/tasks", status_code=status.HTTP_200_OK)
def read_tasks():
    return {"message": "List of all tasks would be fetched here."}

@app.get("/api/v1/tasks/{task_id}", status_code=status.HTTP_200_OK)
def read_task(task_id: int):
    return {"task_id": task_id, "message": "Task details would be fetched here."}

@app.put("/api/v1/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: Task):
    return {"task_id": task_id, "message": "Task updated successfully", "updated_task": task.name}

@app.delete("/api/v1/tasks/{task_id}/true", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    return {"task_id": task_id, "message": "Task deleted successfully"}
