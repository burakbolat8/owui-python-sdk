from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Audio(BaseModel):
    id: str = Field(..., description="Unique identifier for the audio")
    url: Optional[str] = Field(None, description="URL of the audio")
    model: Optional[str] = Field(None, description="Model used for generation")
    config: Optional[Dict[str, Any]] = Field(None, description="Audio configuration")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 