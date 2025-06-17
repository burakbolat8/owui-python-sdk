from typing import Optional, Dict, Any
from .base import BaseAPI

class AuthsAPI(BaseAPI):
    """API endpoints for authentication operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/auths"

    def signin(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sign in a user."""
        return self._post("/signin", json=data)

    def signup(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sign up a user."""
        return self._post("/signup", json=data)

    def signout(self) -> Dict[str, Any]:
        """Sign out the current user."""
        return self._post("/signout")

    def ldap(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """LDAP authentication."""
        return self._post("/ldap", json=data)

    def update_profile(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user profile."""
        return self._post("/update/profile", json=data)

    def update_password(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user password."""
        return self._post("/update/password", json=data)

    def add(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new user (admin)."""
        return self._post("/add", json=data)

    def admin_details(self) -> Dict[str, Any]:
        """Get admin details."""
        return self._get("/admin/details")

    def admin_config(self) -> Dict[str, Any]:
        """Get admin config."""
        return self._get("/admin/config")

    def admin_config_ldap_server(self) -> Dict[str, Any]:
        """Get admin LDAP server config."""
        return self._get("/admin/config/ldap/server")

    def admin_config_ldap(self) -> Dict[str, Any]:
        """Get admin LDAP config."""
        return self._get("/admin/config/ldap")

    def api_key(self) -> Dict[str, Any]:
        """Get API key."""
        return self._get("/api_key") 