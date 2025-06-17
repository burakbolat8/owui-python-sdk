from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Model(BaseModel):
    id: str = Field(..., description="Unique identifier for the model")
    name: str = Field(..., description="Name of the model")
    description: Optional[str] = Field(None, description="Description of the model")
    type: Optional[str] = Field(None, description="Type of the model")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 