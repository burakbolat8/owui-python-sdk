from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Memory(BaseModel):
    """Memory model."""
    id: str = Field(..., description="Unique identifier for the memory")
    content: str = Field(..., description="Content of the memory")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional memory metadata")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

class MemoryCreate(BaseModel):
    """Memory creation request model."""
    content: str = Field(..., description="Content of the memory")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional memory metadata")

class MemoryUpdate(BaseModel):
    """Memory update request model."""
    content: Optional[str] = Field(None, description="New content of the memory")
    metadata: Optional[Dict[str, Any]] = Field(None, description="New memory metadata") 