from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Pipeline(BaseModel):
    id: str = Field(..., description="Unique identifier for the pipeline")
    name: str = Field(..., description="Name of the pipeline")
    url: Optional[str] = Field(None, description="URL of the pipeline")
    url_idx: Optional[int] = Field(None, description="URL index")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    meta: Optional[Dict[str, Any]] = Field(None, description="Additional metadata") 