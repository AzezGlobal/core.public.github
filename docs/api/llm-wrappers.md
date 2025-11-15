# LLM Wrappers API Documentation

## Core Classes

### LLMClient

Main client for interacting with LLM providers.

#### Constructor

```python
LLMClient(
    provider: str,
    api_key: Optional[str] = None,
    config: Optional[Dict] = None,
    retry_config: Optional[RetryConfig] = None
)
```

**Parameters:**
- `provider` (str): The LLM provider name ('openai', 'azure_openai', 'anthropic')
- `api_key` (str, optional): API key for authentication
- `config` (dict, optional): Provider-specific configuration
- `retry_config` (RetryConfig, optional): Retry configuration

**Example:**
```python
client = LLMClient(
    provider="openai",
    api_key="sk-...",
    config={"model": "gpt-4", "temperature": 0.7}
)
```

#### Methods

##### complete()

Generate a completion for a given prompt.

```python
complete(
    prompt: str,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
    **kwargs
) -> CompletionResponse
```

**Parameters:**
- `prompt` (str): The input prompt
- `max_tokens` (int, optional): Maximum tokens to generate
- `temperature` (float, optional): Sampling temperature (0.0 to 2.0)
- `**kwargs`: Additional provider-specific parameters

**Returns:**
- `CompletionResponse`: Object containing the generated text and metadata

**Example:**
```python
response = client.complete(
    "Write a haiku about coding",
    max_tokens=100,
    temperature=0.7
)
print(response.text)
```

##### stream()

Generate a streaming completion.

```python
stream(
    prompt: str,
    max_tokens: Optional[int] = None,
    **kwargs
) -> Iterator[str]
```

**Parameters:**
- `prompt` (str): The input prompt
- `max_tokens` (int, optional): Maximum tokens to generate
- `**kwargs`: Additional provider-specific parameters

**Yields:**
- `str`: Text chunks as they are generated

**Example:**
```python
for chunk in client.stream("Tell me a story"):
    print(chunk, end="", flush=True)
```

##### chat()

Perform a chat completion with message history.

```python
chat(
    messages: List[Dict[str, str]],
    max_tokens: Optional[int] = None,
    **kwargs
) -> ChatResponse
```

**Parameters:**
- `messages` (list): List of message dictionaries with 'role' and 'content'
- `max_tokens` (int, optional): Maximum tokens to generate
- `**kwargs`: Additional provider-specific parameters

**Returns:**
- `ChatResponse`: Object containing the response message and metadata

**Example:**
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is Python?"}
]
response = client.chat(messages)
print(response.message.content)
```

### Response Objects

#### CompletionResponse

```python
class CompletionResponse:
    text: str                    # Generated text
    model: str                   # Model used
    tokens_used: int            # Total tokens consumed
    finish_reason: str          # Reason for completion
    metadata: Dict              # Additional metadata
```

#### ChatResponse

```python
class ChatResponse:
    message: Message            # Response message
    model: str                  # Model used
    tokens_used: int           # Total tokens consumed
    finish_reason: str         # Reason for completion
    metadata: Dict             # Additional metadata

class Message:
    role: str                  # Message role (system/user/assistant)
    content: str               # Message content
```

### Configuration Classes

#### RetryConfig

```python
class RetryConfig:
    max_retries: int = 3
    backoff_factor: float = 2.0
    retry_on: List[Type[Exception]] = [TimeoutError, RateLimitError]
```

## Provider-Specific Notes

### OpenAI

**Supported Models:**
- gpt-4
- gpt-4-turbo
- gpt-3.5-turbo

**Configuration:**
```python
config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}
```

### Azure OpenAI

**Configuration:**
```python
config = {
    "endpoint": "https://your-resource.openai.azure.com/",
    "deployment_name": "gpt-4",
    "api_version": "2024-02-01"
}
```

### Anthropic

**Supported Models:**
- claude-3-opus
- claude-3-sonnet
- claude-3-haiku

**Configuration:**
```python
config = {
    "model": "claude-3-opus-20240229",
    "max_tokens": 4096
}
```

## Error Handling

### Exception Hierarchy

```
LLMException
├── AuthenticationError
├── RateLimitError
├── InvalidRequestError
├── TimeoutError
└── ProviderError
```

**Example:**
```python
from llm_wrappers.exceptions import LLMException, RateLimitError

try:
    response = client.complete("Hello")
except RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
    # Handle rate limiting
except LLMException as e:
    print(f"LLM error: {e}")
    # Handle other errors
```

## Advanced Features

### Token Counting

```python
from llm_wrappers import TokenCounter

counter = TokenCounter(model="gpt-4")
token_count = counter.count("Your text here")
print(f"Tokens: {token_count}")
```

### Prompt Templates

```python
from llm_wrappers import PromptTemplate

template = PromptTemplate(
    "Translate {text} from {source_lang} to {target_lang}"
)

prompt = template.format(
    text="Hello",
    source_lang="English",
    target_lang="French"
)
```

### Caching

```python
from llm_wrappers import CachedLLMClient

client = CachedLLMClient(
    provider="openai",
    cache_ttl=3600  # Cache for 1 hour
)
```

## Rate Limiting

```python
from llm_wrappers import RateLimiter

limiter = RateLimiter(requests_per_minute=60)
client = LLMClient(provider="openai", rate_limiter=limiter)
```
