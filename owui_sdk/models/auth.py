from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Auth(BaseModel):
    id: str = Field(..., description="Unique identifier for the auth entry")
    user_id: Optional[str] = Field(None, description="User ID associated with the auth entry")
    token: Optional[str] = Field(None, description="Authentication token")
    provider: Optional[str] = Field(None, description="Authentication provider")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp") 