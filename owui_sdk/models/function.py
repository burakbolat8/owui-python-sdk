from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class Function(BaseModel):
    """Function model."""
    id: str = Field(..., description="Unique identifier for the function")
    name: str = Field(..., description="Name of the function")
    description: str = Field(..., description="Description of the function")
    parameters: Dict[str, Any] = Field(..., description="Function parameters schema")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional function metadata")

class FunctionCreate(BaseModel):
    """Function creation request model."""
    name: str = Field(..., description="Name of the function")
    description: str = Field(..., description="Description of the function")
    parameters: Dict[str, Any] = Field(..., description="Function parameters schema")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional function metadata")

class FunctionUpdate(BaseModel):
    """Function update request model."""
    name: Optional[str] = Field(None, description="New function name")
    description: Optional[str] = Field(None, description="New function description")
    parameters: Optional[Dict[str, Any]] = Field(None, description="New function parameters schema")
    metadata: Optional[Dict[str, Any]] = Field(None, description="New function metadata") 