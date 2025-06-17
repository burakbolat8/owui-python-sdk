from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Retrieval(BaseModel):
    id: str = Field(..., description="Unique identifier for the retrieval entry")
    type: Optional[str] = Field(None, description="Type of retrieval")
    config: Optional[Dict[str, Any]] = Field(None, description="Retrieval configuration")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 