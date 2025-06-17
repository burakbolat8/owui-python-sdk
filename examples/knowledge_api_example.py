from owui_sdk import OpenWebUI
from owui_sdk.exceptions import APIError
import base64

# Set to True if you want to print base64 of each file
PRINT_BASE64 = True

# Initialize the client (replace with your actual API key or token)
client = OpenWebUI(
    base_url="http://localhost:3000",
    api_key="sk-f8c4b6bb7813486cb130bd3d4d5051e3"
)

def get_knowledge_by_name(client, name):
    all_kbs = client.knowledge.get_all()
    for kb in all_kbs:
        if kb.name == name:
            return kb
    return None

# Usage
kb_name = "Articles"

try:
    kb = get_knowledge_by_name(client, kb_name)
    file_ids = kb.data['file_ids']
    content_base64 = client.files.download_file(file_ids[0], return_base64=True)
    for file_id in file_ids:
        # Download file as bytes
        print(f"Downloading file {file_id} ...")
        raw_bytes = client.files.download_file(file_id)
        content_base64 = client.files.download_file("file_id", return_base64=True)
        print(f"Downloaded {len(raw_bytes)} bytes for {file_id}")

        # Get original filename from file metadata
        print(f"Fetching metadata for {file_id} ...")
        file_meta = client.files.get_file(file_id)
        # print(f"Metadata: {file_meta}")
        
        # Try to get the original filename first
        original_filename = file_meta.get("filename", file_meta.get("name"))
        
        # If no filename found, create one using content type
        if not original_filename:
            content_type = file_meta.get("content_type", "application/octet-stream")
            extension = {
                "application/pdf": ".pdf",
                "image/jpeg": ".jpg",
                "image/png": ".png",
                "text/plain": ".txt",
                "application/json": ".json",
                "text/csv": ".csv",
                "application/msword": ".doc",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
                "application/vnd.ms-excel": ".xls",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx"
            }.get(content_type, ".bin")
            original_filename = f"{file_id}{extension}"
            
        with open(original_filename, "wb") as f:
            f.write(raw_bytes)
        print(f"Saved file as {original_filename}")

        if PRINT_BASE64:
            b64_content = base64.b64encode(raw_bytes).decode("utf-8")
            print(f"Base64 for {original_filename}: {b64_content[:80]}... (truncated)")

except APIError as e:
    print(f"API Error: {e.message} (status code: {e.status_code})") 