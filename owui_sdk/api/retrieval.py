from typing import Optional, Dict, Any, List
from .base import BaseAPI

class RetrievalAPI(BaseAPI):
    """API endpoints for retrieval operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/retrieval"

    def get(self) -> Dict[str, Any]:
        """Get retrieval info."""
        return self._get("")

    def embedding(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get embedding for data."""
        return self._post("/embedding", json=data)

    def reranking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Get reranking for data."""
        return self._post("/reranking", json=data)

    def update_embedding(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update embedding config."""
        return self._post("/embedding/update", json=data)

    def update_reranking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update reranking config."""
        return self._post("/reranking/update", json=data)

    def get_config(self) -> Dict[str, Any]:
        """Get retrieval config."""
        return self._get("/config")

    def update_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Update retrieval config."""
        return self._post("/config/update", json=config)

    def process_file(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a file for retrieval."""
        return self._post("/process/file", json=data)

    def process_text(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process text for retrieval."""
        return self._post("/process/text", json=data)

    def process_youtube(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process YouTube for retrieval."""
        return self._post("/process/youtube", json=data)

    def process_web(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process web for retrieval."""
        return self._post("/process/web", json=data)

    def process_web_search(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process web search for retrieval."""
        return self._post("/process/web/search", json=data)

    def query_doc(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Query a document."""
        return self._post("/query/doc", json=data)

    def query_collection(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Query a collection."""
        return self._post("/query/collection", json=data)

    def delete(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Delete from retrieval."""
        return self._post("/delete", json=data)

    def reset_db(self) -> Dict[str, Any]:
        """Reset retrieval database."""
        return self._post("/reset/db")

    def reset_uploads(self) -> Dict[str, Any]:
        """Reset retrieval uploads."""
        return self._post("/reset/uploads")

    def ef(self, text: str) -> Dict[str, Any]:
        """EF endpoint for retrieval."""
        return self._get(f"/ef/{text}")

    def process_files_batch(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process files batch for retrieval."""
        return self._post("/process/files/batch", json=data) 