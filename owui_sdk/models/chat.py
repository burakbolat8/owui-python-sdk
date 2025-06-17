from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Message(BaseModel):
    """Chat message model."""
    role: str = Field(..., description="Role of the message sender (user/assistant)")
    content: str = Field(..., description="Content of the message")
    name: Optional[str] = Field(None, description="Name of the message sender")
    function_call: Optional[Dict[str, Any]] = Field(None, description="Function call details")
    tool_calls: Optional[List[Dict[str, Any]]] = Field(None, description="Tool call details")

class ChatCompletionRequest(BaseModel):
    """Chat completion request model."""
    model: str = Field(..., description="Model to use for completion")
    messages: List[Message] = Field(..., description="List of messages in the conversation")
    stream: Optional[bool] = Field(False, description="Whether to stream the response")
    temperature: Optional[float] = Field(1.0, description="Sampling temperature")
    top_p: Optional[float] = Field(1.0, description="Top p sampling parameter")
    max_tokens: Optional[int] = Field(None, description="Maximum number of tokens to generate")
    functions: Optional[List[Dict[str, Any]]] = Field(None, description="Available functions")
    function_call: Optional[Dict[str, Any]] = Field(None, description="Function call configuration")
    tools: Optional[List[Dict[str, Any]]] = Field(None, description="Available tools")
    tool_choice: Optional[Dict[str, Any]] = Field(None, description="Tool choice configuration")

class ChatCompletionResponse(BaseModel):
    """Chat completion response model."""
    id: str = Field(..., description="Unique identifier for the completion")
    object: str = Field(..., description="Object type")
    created: int = Field(..., description="Unix timestamp of creation")
    model: str = Field(..., description="Model used for completion")
    choices: List[Dict[str, Any]] = Field(..., description="Completion choices")
    usage: Optional[Dict[str, int]] = Field(None, description="Token usage statistics")

class Chat(BaseModel):
    id: str = Field(..., description="Unique identifier for the chat")
    title: Optional[str] = Field(None, description="Title of the chat")
    user_id: Optional[str] = Field(None, description="User ID associated with the chat")
    created_at: Optional[int] = Field(None, description="Creation timestamp (epoch)")
    updated_at: Optional[int] = Field(None, description="Last update timestamp (epoch)") 