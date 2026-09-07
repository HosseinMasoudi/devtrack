from fastapi import FastAPI, status
from schema import Project

app = FastAPI(description="DevTrack is a production-oriented project management backend built with FastAPI.")


@app.post("/api/v1/projects", status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
    return {"message": "Project created successfully", "project": project.name}

@app.get("/api/v1/projects", status_code=status.HTTP_200_OK)
def read_projects():
    return {"message": "List of all projects would be fetched here."}

@app.get("/api/v1/projects/{project_id}", status_code=status.HTTP_200_OK)
def read_project(project_id: int):
    return {"project_id": project_id, "message": "Project details would be fetched here."}

@app.put("/api/v1/projects/{project_id}", status_code=status.HTTP_200_OK)
def update_project(project_id: int, project: Project):
    return {"project_id": project_id, "message": "Project updated successfully", "updated_project": project.name}

@app.delete("/api/v1/projects/{project_id}/true", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int):
    return {"project_id": project_id, "message": "Project deleted successfully"}