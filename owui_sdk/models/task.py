from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Task(BaseModel):
    id: str = Field(..., description="Unique identifier for the task")
    name: str = Field(..., description="Name of the task")
    config: Optional[Dict[str, Any]] = Field(None, description="Task configuration")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 