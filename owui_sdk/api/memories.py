from typing import Optional, Dict, Any, List
from .base import BaseAPI

class MemoriesAPI(BaseAPI):
    """API endpoints for memory operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/memories"
    
    def add_memory(
        self,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add a new memory.
        
        Args:
            content: Memory content
            metadata: Additional metadata
            **kwargs: Additional parameters
        """
        data = {
            "content": content,
            "metadata": metadata or {},
            **kwargs
        }
        return self._post("/add", json=data)
    
    def get_memories(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Get memories with optional pagination.
        
        Args:
            limit: Maximum number of memories to return
            offset: Number of memories to skip
            **kwargs: Additional query parameters
        """
        params = {
            "limit": limit,
            "offset": offset,
            **kwargs
        }
        return self._get(params=params)
    
    def get_memory(self, memory_id: str) -> Dict[str, Any]:
        """
        Get a specific memory.
        
        Args:
            memory_id: ID of the memory
        """
        return self._get(f"/{memory_id}")
    
    def update_memory(
        self,
        memory_id: str,
        content: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a memory.
        
        Args:
            memory_id: ID of the memory
            content: New memory content
            metadata: New metadata
            **kwargs: Additional parameters
        """
        data = {
            "content": content,
            "metadata": metadata,
            **kwargs
        }
        return self._put(f"/{memory_id}", json=data)
    
    def delete_memory(self, memory_id: str) -> Dict[str, Any]:
        """
        Delete a memory.
        
        Args:
            memory_id: ID of the memory
        """
        return self._delete(f"/{memory_id}")
    
    def search_memories(
        self,
        query: str,
        limit: Optional[int] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Search memories.
        
        Args:
            query: Search query
            limit: Maximum number of results
            **kwargs: Additional search parameters
        """
        params = {
            "query": query,
            "limit": limit,
            **kwargs
        }
        return self._get("/search", params=params) 