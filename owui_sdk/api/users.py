from typing import Optional, Dict, Any, List
from .base import BaseAPI

class UsersAPI(BaseAPI):
    """API endpoints for user operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/users"
    
    def get_users(self) -> List[Dict[str, Any]]:
        """Get all users."""
        return self._get()
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Get a specific user.
        
        Args:
            user_id: ID of the user
        """
        return self._get(f"/{user_id}")
    
    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new user.
        
        Args:
            username: Username
            email: Email address
            password: Password
            **kwargs: Additional user parameters
        """
        data = {
            "username": username,
            "email": email,
            "password": password,
            **kwargs
        }
        return self._post(json=data)
    
    def update_user(
        self,
        user_id: str,
        username: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a user.
        
        Args:
            user_id: ID of the user
            username: New username
            email: New email address
            password: New password
            **kwargs: Additional parameters
        """
        data = {
            "username": username,
            "email": email,
            "password": password,
            **kwargs
        }
        return self._put(f"/{user_id}", json=data)
    
    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """
        Delete a user.
        
        Args:
            user_id: ID of the user
        """
        return self._delete(f"/{user_id}")
    
    def get_user_permissions(self, user_id: str) -> Dict[str, Any]:
        """
        Get user permissions.
        
        Args:
            user_id: ID of the user
        """
        return self._get(f"/{user_id}/permissions")
    
    def update_user_permissions(
        self,
        user_id: str,
        permissions: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update user permissions.
        
        Args:
            user_id: ID of the user
            permissions: New permissions
            **kwargs: Additional parameters
        """
        data = {
            "permissions": permissions,
            **kwargs
        }
        return self._put(f"/{user_id}/permissions", json=data)
    
    def get_user_groups(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Get user groups.
        
        Args:
            user_id: ID of the user
        """
        return self._get(f"/{user_id}/groups")
    
    def add_user_to_group(
        self,
        user_id: str,
        group_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add user to a group.
        
        Args:
            user_id: ID of the user
            group_id: ID of the group
            **kwargs: Additional parameters
        """
        data = {
            "group_id": group_id,
            **kwargs
        }
        return self._post(f"/{user_id}/groups", json=data)
    
    def remove_user_from_group(
        self,
        user_id: str,
        group_id: str
    ) -> Dict[str, Any]:
        """
        Remove user from a group.
        
        Args:
            user_id: ID of the user
            group_id: ID of the group
        """
        return self._delete(f"/{user_id}/groups/{group_id}") 