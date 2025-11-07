from owui_sdk import OpenWebUI
from typing import Dict, List, Tuple
from owui_sdk.exceptions import APIError

def get_knowledge_files(client: OpenWebUI, kb_name: str, api_key_in_url: bool = False) -> List[Dict[str, str]]:
    """
    Get file IDs and URLs for a given knowledge base.
    
    Args:
        client: OpenWebUI client instance
        kb_name: Name of the knowledge base
        api_key_in_url: If True, adds the API key as a URL parameter instead of header
        
    Returns:
        List of dictionaries containing file information with keys:
        - file_id: The ID of the file
        - filename: Original filename
        - url: Full URL to access the file
        - content_type: MIME type of the file
    """
    try:
        # Get all knowledge bases and find the one with matching name
        all_kbs = client.knowledge.get_all()
        kb = None
        for k in all_kbs:
            if k.name == kb_name:
                kb = k
                break
                
        if not kb:
            raise ValueError(f"Knowledge base '{kb_name}' not found")
            
        # Get file IDs from the knowledge base
        file_ids = kb.data.get('file_ids', [])
        if not file_ids:
            return []
            
        # Get detailed information for each file
        files_info = []
        for file_id in file_ids:
            # Get file metadata
            file_meta = client.files.get_file(file_id)
            
            # Construct file URL
            base_url = f"{client.base_url}/api/v1/files/{file_id}/content"
            
            # Add API key to URL if requested
            if api_key_in_url and client.api_key:
                file_url = f"{base_url}?api_key={client.api_key}"
            else:
                file_url = base_url
            
            files_info.append({
                'file_id': file_id,
                'filename': file_meta.get('filename', file_meta.get('name', 'unknown')),
                'url': file_url,
                'content_type': file_meta.get('content_type', 'application/octet-stream')
            })
            
        return files_info
            
    except APIError as e:
        print(f"API Error: {e.message} (status code: {e.status_code})")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    # Initialize the client (replace with your actual API key or token)
    client = OpenWebUI(
        base_url="http://localhost:3000",
        api_key="sk-f8c4b6bb7813486cb130bd3d4d5051e3"  # Replace with your API key
    )
    
    # Example knowledge base name
    kb_name = "Articles"
    
    # Get file information with API key in URL
    files = get_knowledge_files(client, kb_name, api_key_in_url=True)
    
    # Print results
    if files:
        print(f"\nFiles in knowledge base '{kb_name}':")
        for file in files:
            print(f"\nFile ID: {file['file_id']}")
            print(f"Filename: {file['filename']}")
            print(f"URL: {file['url']}")
            print(f"Content Type: {file['content_type']}")
    else:
        print(f"\nNo files found in knowledge base '{kb_name}' or an error occurred")
