from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class File(BaseModel):
    """File model."""
    id: str = Field(..., description="Unique identifier for the file")
    name: str = Field(..., description="Name of the file")
    size: int = Field(..., description="Size of the file in bytes")
    content_type: str = Field(..., description="MIME type of the file")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional file metadata")

class FileUpload(BaseModel):
    """File upload request model."""
    file: bytes = Field(..., description="File content")
    filename: str = Field(..., description="Name of the file")
    content_type: Optional[str] = Field(None, description="MIME type of the file")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional file metadata") 