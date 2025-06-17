from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class Permission(BaseModel):
    """Permission model."""
    id: str = Field(..., description="Unique identifier for the permission")
    name: str = Field(..., description="Name of the permission")
    description: str = Field(..., description="Description of the permission")
    scope: str = Field(..., description="Permission scope")

class Group(BaseModel):
    """Group model."""
    id: str = Field(..., description="Unique identifier for the group")
    name: str = Field(..., description="Name of the group")
    description: str = Field(..., description="Description of the group")
    permissions: List[Permission] = Field(default_factory=list, description="Group permissions")

class User(BaseModel):
    """User model."""
    id: str = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="Email address")
    permissions: List[Permission] = Field(default_factory=list, description="User permissions")
    groups: List[Group] = Field(default_factory=list, description="User groups")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional user metadata")

class UserCreate(BaseModel):
    """User creation request model."""
    username: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., description="Password")
    permissions: Optional[List[str]] = Field(None, description="List of permission IDs")
    groups: Optional[List[str]] = Field(None, description="List of group IDs")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional user metadata")

class UserUpdate(BaseModel):
    """User update request model."""
    username: Optional[str] = Field(None, description="New username")
    email: Optional[EmailStr] = Field(None, description="New email address")
    password: Optional[str] = Field(None, description="New password")
    permissions: Optional[List[str]] = Field(None, description="New list of permission IDs")
    groups: Optional[List[str]] = Field(None, description="New list of group IDs")
    metadata: Optional[Dict[str, Any]] = Field(None, description="New user metadata") 