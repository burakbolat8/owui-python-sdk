from typing import Optional, Dict, Any, List
from .base import BaseAPI

class ChannelsAPI(BaseAPI):
    """API endpoints for channel operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/channels"

    def list(self) -> List[Dict[str, Any]]:
        """Get all channels."""
        return self._get("")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new channel."""
        return self._post("/create", json=data)

    def get(self, channel_id: str) -> Dict[str, Any]:
        """Get a channel by ID."""
        return self._get(f"/{channel_id}")

    def update(self, channel_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a channel by ID."""
        return self._post(f"/{channel_id}/update", json=data)

    def delete(self, channel_id: str) -> Dict[str, Any]:
        """Delete a channel by ID."""
        return self._post(f"/{channel_id}/delete")

    def get_messages(self, channel_id: str) -> List[Dict[str, Any]]:
        """Get messages for a channel."""
        return self._get(f"/{channel_id}/messages")

    def post_message(self, channel_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Post a message to a channel."""
        return self._post(f"/{channel_id}/messages/post", json=data)

    def get_message(self, channel_id: str, message_id: str) -> Dict[str, Any]:
        """Get a message by ID in a channel."""
        return self._get(f"/{channel_id}/messages/{message_id}")

    def get_message_thread(self, channel_id: str, message_id: str) -> List[Dict[str, Any]]:
        """Get message thread by message ID in a channel."""
        return self._get(f"/{channel_id}/messages/{message_id}/thread")

    def update_message(self, channel_id: str, message_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a message by ID in a channel."""
        return self._post(f"/{channel_id}/messages/{message_id}/update", json=data)

    def add_reaction(self, channel_id: str, message_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a reaction to a message in a channel."""
        return self._post(f"/{channel_id}/messages/{message_id}/reactions/add", json=data)

    def remove_reaction(self, channel_id: str, message_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Remove a reaction from a message in a channel."""
        return self._post(f"/{channel_id}/messages/{message_id}/reactions/remove", json=data)

    def delete_message(self, channel_id: str, message_id: str) -> Dict[str, Any]:
        """Delete a message by ID in a channel."""
        return self._post(f"/{channel_id}/messages/{message_id}/delete") 