from typing import Optional, Dict, Any, List, BinaryIO, Union
from .base import BaseAPI

class FilesAPI(BaseAPI):
    """API endpoints for file operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/v1/files"
    
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
    
    def download_file(self, file_id: str, save_path: Optional[str] = None, return_base64: bool = False) -> Union[bytes, str]:
        """
        Download a file and optionally save it to disk.
        
        Args:
            file_id: ID of the file
            save_path: Optional path where to save the file. If not provided, the file will be saved
                      with its original filename in the current directory. If provided and is a directory,
                      the file will be saved in that directory with its original filename. If provided and
                      is a file path, the file will be saved with that name.
            return_base64: If True, returns the file content as a base64-encoded string instead of bytes.
        
        Returns:
            If return_base64 is True, returns the file content as a base64-encoded string.
            Otherwise, returns the file content as bytes.
        """
        # Get file metadata to get the original filename
        file_meta = self.get_file(file_id)
        original_filename = file_meta.get("filename", file_meta.get("name"))
        
        # Download the file content
        content = self._get(f"/{file_id}/content", params={"attachment": True}, raw=True)
        
        # Save the file if requested
        if save_path is not None or original_filename:
            import os
            
            # Determine the final save path
            if save_path is None:
                final_path = original_filename or f"{file_id}.bin"
            elif os.path.isdir(save_path):
                final_path = os.path.join(save_path, original_filename or f"{file_id}.bin")
            else:
                final_path = save_path
                
            # Save the file
            with open(final_path, "wb") as f:
                f.write(content)
                
            print(f"Saved file as {final_path}")
        
        # Return as base64 if requested
        if return_base64:
            import base64
            return base64.b64encode(content).decode("utf-8")
            
        return content
    
    def get_file_content(self, file_id: str) -> str:
        """
        Get file content as text.
        
        Args:
            file_id: ID of the file
        """
        response = self._get(f"/{file_id}/content")
        return response.text 