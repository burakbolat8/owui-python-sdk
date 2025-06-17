import os
from typing import Optional, Dict, Any
import requests
from .exceptions import APIError, AuthenticationError
from .api import (
    ModelsAPI,
    ChatAPI,
    FilesAPI,
    MemoriesAPI,
    FunctionsAPI,
    ToolsAPI,
    UsersAPI,
    KnowledgeAPI,
    PipelinesAPI,
    TasksAPI,
    ImagesAPI,
    AudioAPI,
    RetrievalAPI,
    ConfigsAPI,
    AuthsAPI,
    ChannelsAPI,
    ChatsAPI,
)

class OpenWebUI:
    """Main client class for interacting with the Open WebUI API."""
    
    def __init__(
        self,
        base_url: str = "http://localhost:3000",
        api_key: Optional[str] = None,
        oauth_provider: Optional[str] = None,
        oauth_token: Optional[str] = None,
        timeout: int = 30,
    ):
        """
        Initialize the OpenWebUI client.
        
        Args:
            base_url: The base URL of the Open WebUI API
            api_key: API key for authentication
            oauth_provider: OAuth provider name (e.g., "google")
            oauth_token: OAuth token for authentication
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        
        # Set up authentication
        self.api_key = api_key or os.getenv("OWUI_API_KEY")
        self.oauth_provider = oauth_provider
        self.oauth_token = oauth_token
        
        # Initialize session
        self.session = requests.Session()
        self._setup_session()
        
        # Initialize API endpoints
        self.models = ModelsAPI(self)
        self.chat = ChatAPI(self)
        self.files = FilesAPI(self)
        self.memories = MemoriesAPI(self)
        self.functions = FunctionsAPI(self)
        self.tools = ToolsAPI(self)
        self.users = UsersAPI(self)
        self.knowledge = KnowledgeAPI(self)
        self.pipelines = PipelinesAPI(self)
        self.tasks = TasksAPI(self)
        self.images = ImagesAPI(self)
        self.audio = AudioAPI(self)
        self.retrieval = RetrievalAPI(self)
        self.configs = ConfigsAPI(self)
        self.auths = AuthsAPI(self)
        self.channels = ChannelsAPI(self)
        self.chats = ChatsAPI(self)
    
    def _setup_session(self):
        """Set up the requests session with authentication headers."""
        headers = {}
        
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        elif self.oauth_token:
            headers["Authorization"] = f"Bearer {self.oauth_token}"
        
        self.session.headers.update(headers)
    
    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Any:
        """
        Make a request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters
            json: JSON body
            data: Form data
            files: Files to upload
            raw: If True, return raw response content (bytes)
            
        Returns:
            API response as dictionary or raw bytes
            
        Raises:
            APIError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                data=data,
                files=files,
                timeout=self.timeout,
            )
            response.raise_for_status()
            if raw:
                return response.content
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Authentication failed", e.response.status_code)
            raise APIError(str(e), e.response.status_code, e.response.json())
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, raw: bool = False) -> Any:
        """Make a GET request."""
        return self.request("GET", endpoint, params=params, raw=raw)
    
    def post(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request."""
        return self.request("POST", endpoint, json=json, data=data, files=files)
    
    def put(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a PUT request."""
        return self.request("PUT", endpoint, json=json, data=data)
    
    def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self.request("DELETE", endpoint, params=params) 