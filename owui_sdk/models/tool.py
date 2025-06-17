from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class Tool(BaseModel):
    """Tool model."""
    id: str = Field(..., description="Unique identifier for the tool")
    name: str = Field(..., description="Name of the tool")
    description: str = Field(..., description="Description of the tool")
    parameters: Dict[str, Any] = Field(..., description="Tool parameters schema")
    valves: Dict[str, Any] = Field(default_factory=dict, description="Tool valve configurations")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional tool metadata")

class ToolCreate(BaseModel):
    """Tool creation request model."""
    name: str = Field(..., description="Name of the tool")
    description: str = Field(..., description="Description of the tool")
    parameters: Dict[str, Any] = Field(..., description="Tool parameters schema")
    valves: Optional[Dict[str, Any]] = Field(None, description="Tool valve configurations")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional tool metadata")

class ToolUpdate(BaseModel):
    """Tool update request model."""
    name: Optional[str] = Field(None, description="New tool name")
    description: Optional[str] = Field(None, description="New tool description")
    parameters: Optional[Dict[str, Any]] = Field(None, description="New tool parameters schema")
    valves: Optional[Dict[str, Any]] = Field(None, description="New tool valve configurations")
    metadata: Optional[Dict[str, Any]] = Field(None, description="New tool metadata") 