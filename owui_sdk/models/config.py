from typing import Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Config(BaseModel):
    id: str = Field(..., description="Unique identifier for the config")
    name: str = Field(..., description="Name of the config")
    value: Optional[Any] = Field(None, description="Value of the config")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp") 