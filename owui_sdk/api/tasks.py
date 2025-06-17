from typing import Optional, Dict, Any
from .base import BaseAPI

class TasksAPI(BaseAPI):
    """API endpoints for task operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/tasks"

    def get_config(self) -> Dict[str, Any]:
        """Get tasks config."""
        return self._get("/config")

    def update_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Update tasks config."""
        return self._post("/config/update", json=config)

    def title_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get title completions for tasks."""
        return self._post("/title/completions", json=data)

    def tags_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get tags completions for tasks."""
        return self._post("/tags/completions", json=data)

    def image_prompt_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get image prompt completions for tasks."""
        return self._post("/image_prompt/completions", json=data)

    def queries_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get queries completions for tasks."""
        return self._post("/queries/completions", json=data)

    def auto_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get auto completions for tasks."""
        return self._post("/auto/completions", json=data)

    def emoji_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get emoji completions for tasks."""
        return self._post("/emoji/completions", json=data)

    def moa_completions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get moa completions for tasks."""
        return self._post("/moa/completions", json=data) 