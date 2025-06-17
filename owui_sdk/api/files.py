from typing import Optional, Dict, Any, List, BinaryIO
from .base import BaseAPI

class FilesAPI(BaseAPI):
    """API endpoints for file operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/files"
    
    def upload(
        self,
        file: BinaryIO,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Upload a file.
        
        Args:
            file: File object to upload
            filename: Name of the file
            content_type: Content type of the file
            **kwargs: Additional parameters
        """
        files = {
            "file": (filename or file.name, file, content_type)
        }
        return self._post("/upload", files=files, data=kwargs)
    
    def get_files(self) -> List[Dict[str, Any]]:
        """Get all files."""
        return self._get()
    
    def get_file(self, file_id: str) -> Dict[str, Any]:
        """
        Get a specific file.
        
        Args:
            file_id: ID of the file
        """
        return self._get(f"/{file_id}")
    
    def delete_file(self, file_id: str) -> Dict[str, Any]:
        """
        Delete a file.
        
        Args:
            file_id: ID of the file
        """
        return self._delete(f"/{file_id}")
    
    def download_file(self, file_id: str) -> bytes:
        """
        Download a file.
        
        Args:
            file_id: ID of the file
        """
        response = self._get(f"/{file_id}/download", stream=True)
        return response.content
    
    def get_file_content(self, file_id: str) -> str:
        """
        Get file content as text.
        
        Args:
            file_id: ID of the file
        """
        response = self._get(f"/{file_id}/content")
        return response.text 