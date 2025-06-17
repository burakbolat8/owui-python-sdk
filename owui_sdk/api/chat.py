from typing import Optional, Dict, Any, List, Union
from .base import BaseAPI

class ChatAPI(BaseAPI):
    """API endpoints for chat operations."""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "/api/chat"
    
    def create_completion(
        self,
        model: str,
        messages: List[Dict[str, Any]],
        stream: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> Union[Dict[str, Any], Any]:
        """
        Create a chat completion.
        
        Args:
            model: Model to use
            messages: List of messages
            stream: Whether to stream the response
            temperature: Sampling temperature
            top_p: Top p sampling parameter
            max_tokens: Maximum number of tokens to generate
            **kwargs: Additional parameters
        """
        data = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            **kwargs
        }
        return self._post("/completions", json=data)
    
    def get_conversations(self) -> List[Dict[str, Any]]:
        """Get all conversations."""
        return self._get("/conversations")
    
    def get_conversation(self, conversation_id: str) -> Dict[str, Any]:
        """
        Get a specific conversation.
        
        Args:
            conversation_id: ID of the conversation
        """
        return self._get(f"/conversations/{conversation_id}")
    
    def delete_conversation(self, conversation_id: str) -> Dict[str, Any]:
        """
        Delete a conversation.
        
        Args:
            conversation_id: ID of the conversation
        """
        return self._delete(f"/conversations/{conversation_id}")
    
    def get_messages(self, conversation_id: str) -> List[Dict[str, Any]]:
        """
        Get messages from a conversation.
        
        Args:
            conversation_id: ID of the conversation
        """
        return self._get(f"/conversations/{conversation_id}/messages")
    
    def create_message(
        self,
        conversation_id: str,
        content: str,
        role: str = "user",
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new message in a conversation.
        
        Args:
            conversation_id: ID of the conversation
            content: Message content
            role: Message role (user/assistant)
            **kwargs: Additional message parameters
        """
        data = {
            "content": content,
            "role": role,
            **kwargs
        }
        return self._post(f"/conversations/{conversation_id}/messages", json=data) 