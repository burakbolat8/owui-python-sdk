from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Channel(BaseModel):
    id: str = Field(..., description="Unique identifier for the channel")
    name: str = Field(..., description="Name of the channel")
    description: Optional[str] = Field(None, description="Description of the channel")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 