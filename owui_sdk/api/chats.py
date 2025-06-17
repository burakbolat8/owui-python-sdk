from .base import BaseAPI

class ChatsAPI(BaseAPI):
    """API class for /api/v1/chats/ endpoints."""
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/chats/"

    def list(self):
        """List chats."""
        return self._get()

    def new(self, data):
        """Create a new chat."""
        return self._post(data=data) 