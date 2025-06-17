from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Knowledge(BaseModel):
    id: str = Field(..., description="Unique identifier for the knowledge base")
    name: str = Field(..., description="Name of the knowledge base")
    description: Optional[str] = Field(None, description="Description of the knowledge base")
    data: Optional[Dict[str, Any]] = Field(None, description="Additional data, such as file_ids")
    meta: Optional[Dict[str, Any]] = Field(None, description="Metadata for the knowledge base")
    access_control: Optional[Dict[str, Any]] = Field(None, description="Access control information")
    created_at: Optional[int] = Field(None, description="Creation timestamp (epoch)")
    updated_at: Optional[int] = Field(None, description="Last update timestamp (epoch)")
    user: Optional[Dict[str, Any]] = Field(None, description="User who owns the knowledge base")
    files: Optional[List[Dict[str, Any]]] = Field(None, description="List of files associated with the knowledge base") 