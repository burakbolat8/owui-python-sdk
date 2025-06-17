# Open WebUI Python SDK Documentation

Welcome to the documentation for the Open WebUI Python SDK. This documentation provides detailed guides for each major API group, usage examples, authentication, error handling, and advanced features.

---

# Quick Start

## Installation

```bash
pip install owui-sdk
```

## Client Initialization

```python
from owui_sdk import OpenWebUI

client = OpenWebUI(
    base_url="http://localhost:3000",
    api_key="your-api-key"  # or use oauth_token
)
```

## Example: Get All Models

```python
models = client.models.get_all()
print(models)
```

---

# Authentication

The SDK supports both API key and OAuth authentication.

## API Key Authentication

```python
client = OpenWebUI(api_key="your-api-key")
```

## OAuth Authentication

```python
client = OpenWebUI(
    oauth_provider="google",
    oauth_token="your-oauth-token"
)
```

- Store credentials securely (e.g., environment variables).
- Never commit secrets to version control.

---

# Error Handling

The SDK provides robust error handling with custom exceptions.

## Example

```python
from owui_sdk.exceptions import APIError

try:
    response = client.chat.create_completion(...)
except APIError as e:
    print(f"Error: {e.message}")
    print(f"Status code: {e.status_code}")
```

## Exception Types
- APIError
- AuthenticationError
- ValidationError
- RateLimitError
- ResourceNotFoundError

---

# Models API

Manage and query available models.

## Endpoints
- `get_all()` — List all models
- `get_base_models()` — List base models
- `create(model, stream=None, path=None, **kwargs)` — Create a new model
- `push(name, insecure=None, stream=None)` — Push a model
- `copy(source, destination)` — Copy a model

## Example
```python
models = client.models.get_all()
print(models)
```

---

# Chat API

Interact with chat completions and conversations.

## Endpoints
- `create_completion(model, messages, ...)` — Create a chat completion
- `get_conversations()` — List conversations
- `get_conversation(conversation_id)` — Get a conversation
- `delete_conversation(conversation_id)` — Delete a conversation
- `get_messages(conversation_id)` — List messages in a conversation
- `create_message(conversation_id, content, role, **kwargs)` — Add a message

## Example
```python
response = client.chat.create_completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response)
```

---

# Memories API

Manage and query user memories.

## Endpoints
- `add_memory(content, metadata=None, **kwargs)` — Add a memory
- `get_memories(limit=None, offset=None, **kwargs)` — List memories
- `get_memory(memory_id)` — Get a memory
- `update_memory(memory_id, content=None, metadata=None, **kwargs)` — Update a memory
- `delete_memory(memory_id)` — Delete a memory
- `search_memories(query, limit=None, **kwargs)` — Search memories

## Example
```python
memories = client.memories.get_memories(limit=10)
print(memories)
```

---

# Functions API

Manage and execute custom functions.

## Endpoints
- `get_functions()` — List all functions
- `get_function(function_id)` — Get a function
- `create_function(name, description, parameters, **kwargs)` — Create a function
- `update_function(function_id, ...)` — Update a function
- `delete_function(function_id)` — Delete a function
- `execute_function(function_id, arguments, **kwargs)` — Execute a function

## Example
```python
functions = client.functions.get_functions()
print(functions)
```

---

# Tools API

Manage and execute tools.

## Endpoints
- `get_tools()` — List all tools
- `get_tool(tool_id)` — Get a tool
- `create_tool(name, description, parameters, **kwargs)` — Create a tool
- `update_tool(tool_id, ...)` — Update a tool
- `delete_tool(tool_id)` — Delete a tool
- `execute_tool(tool_id, arguments, **kwargs)` — Execute a tool
- `update_user_valves(tool_id, valves, **kwargs)` — Update user valves for a tool

## Example
```python
tools = client.tools.get_tools()
print(tools)
```

---

# Users API

Manage users, permissions, and groups.

## Endpoints
- `get_users()` — List all users
- `get_user(user_id)` — Get a user
- `create_user(username, email, password, **kwargs)` — Create a user
- `update_user(user_id, ...)` — Update a user
- `delete_user(user_id)` — Delete a user
- `get_user_permissions(user_id)` — Get user permissions
- `update_user_permissions(user_id, permissions, **kwargs)` — Update user permissions
- `get_user_groups(user_id)` — Get user groups
- `add_user_to_group(user_id, group_id, **kwargs)` — Add user to group
- `remove_user_from_group(user_id, group_id)` — Remove user from group

## Example
```python
users = client.users.get_users()
print(users)
```

---

# Knowledge API

Manage knowledge bases and files.

## Endpoints
- `get_all()` — List all knowledge bases
- `get()` — Get knowledge for current user
- `create(name, description, ...)` — Create a knowledge base
- `reindex()` — Reindex all knowledge files
- `get_by_id(knowledge_id)` — Get knowledge by ID
- `update(knowledge_id, ...)` — Update knowledge by ID
- `add_file(knowledge_id, file_id)` — Add file to knowledge
- `update_file(knowledge_id, file_id)` — Update file in knowledge
- `remove_file(knowledge_id, file_id)` — Remove file from knowledge
- `delete(knowledge_id)` — Delete knowledge by ID
- `reset(knowledge_id)` — Reset knowledge by ID
- `add_files_batch(knowledge_id, file_ids)` — Add multiple files to knowledge

## Example
```python
knowledge = client.knowledge.get_all()
print(knowledge)
```

---

# Files API

Manage file uploads, downloads, and metadata.

## Endpoints
- `upload(file, filename=None, content_type=None, **kwargs)` — Upload a file
- `get_files()` — List all files
- `get_file(file_id)` — Get file metadata
- `delete_file(file_id)` — Delete a file
- `download_file(file_id)` — Download file content
- `get_file_content(file_id)` — Get file content as text

## Example
```python
files = client.files.get_files()
print(files)
``` 