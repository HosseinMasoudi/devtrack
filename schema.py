from pydantic import BaseModel, Field, field_validator

class Project(BaseModel):
    id: int = Field(..., description="The unique identifier of the project")
    name: str = Field(..., description="The name of the project")
    description: str = Field(..., description="A brief description of the project")
    start_date: str = Field(..., description="The start date of the project in YYYY-MM-DD format")
    end_date: str = Field(..., description="The end date of the project in YYYY-MM-DD format")
    
class Task(BaseModel):
    id: int = Field(..., description="The unique identifier of the task")
    project_id: int = Field(..., description="The unique identifier of the project this task belongs to")
    name: str = Field(..., description="The name of the task")
    description: str = Field(..., description="A brief description of the task")
    status: str = Field(..., description="The current status of the task (e.g., 'pending', 'in progress', 'completed')")
    priority: str = Field(..., description="The priority level of the task (e.g., 'low', 'medium', 'high', 'critical')")
    due_date: str = Field(..., description="The due date of the task in YYYY-MM-DD format")
    
    @field_validator("status")
    def validate_status(self, value):
        allowed_statuses = ["active", "completed", "in_progress"]
        if value not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return value
    
    @field_validator("priority")
    def validate_priority(self, value):
        allowed_priorities = ["low", "medium", "high", "critical"]
        if value not in allowed_priorities:
            raise ValueError(f"Priority must be one of {allowed_priorities}")
        return value
