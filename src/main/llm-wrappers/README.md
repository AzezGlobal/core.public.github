# LLM Wrappers Framework

A unified framework for integrating with various Large Language Model (LLM) providers.

## Overview

This framework provides a consistent interface for working with different LLM providers such as OpenAI, Azure OpenAI, Anthropic, and others. It abstracts away provider-specific details and offers common functionality for prompt management, response handling, and error recovery.

## Features

- **Multi-Provider Support**: Works with OpenAI, Azure OpenAI, Anthropic, and more
- **Unified Interface**: Consistent API across all providers
- **Error Handling**: Built-in retry logic and error management
- **Token Management**: Automatic token counting and optimization
- **Streaming Support**: Real-time response streaming
- **Configuration Management**: Easy provider configuration and switching

## Quick Start

### Installation

```bash
# Python
pip install -r requirements.txt

# Or for specific providers
pip install openai anthropic
```

### Basic Usage

```python
from llm_wrappers import LLMClient

# Initialize client
client = LLMClient(provider="openai", api_key="your-api-key")

# Simple completion
response = client.complete("Tell me a joke about programming")
print(response.text)

# With streaming
for chunk in client.stream("Write a short story"):
    print(chunk, end="")
```

## Architecture

The framework is built around several core components:

- **LLMClient**: Main entry point for all LLM operations
- **ProviderAdapter**: Abstract interface for provider implementations
- **PromptManager**: Template management and prompt engineering
- **ResponseHandler**: Standardized response parsing and processing
- **TokenCounter**: Token counting and optimization utilities

## Provider Support

| Provider | Status | Features |
|----------|--------|----------|
| OpenAI | ✅ Full | Chat, Completion, Embeddings |
| Azure OpenAI | ✅ Full | Chat, Completion, Embeddings |
| Anthropic | ✅ Full | Chat, Completion |
| Google PaLM | 🚧 Beta | Chat, Completion |
| Cohere | 🚧 Beta | Completion, Embeddings |

## Configuration

Create a configuration file `llm_config.json`:

```json
{
  "default_provider": "openai",
  "providers": {
    "openai": {
      "api_key": "${OPENAI_API_KEY}",
      "model": "gpt-4",
      "temperature": 0.7,
      "max_tokens": 2000
    },
    "azure_openai": {
      "api_key": "${AZURE_OPENAI_KEY}",
      "endpoint": "${AZURE_OPENAI_ENDPOINT}",
      "deployment_name": "gpt-4",
      "api_version": "2024-02-01"
    }
  }
}
```

## Advanced Features

### Prompt Templates

```python
from llm_wrappers import PromptTemplate

template = PromptTemplate(
    "Translate the following {source_lang} text to {target_lang}: {text}"
)

response = client.complete(
    template.format(
        source_lang="English",
        target_lang="French",
        text="Hello, world!"
    )
)
```

### Error Handling & Retries

```python
from llm_wrappers import LLMClient, RetryConfig

client = LLMClient(
    provider="openai",
    retry_config=RetryConfig(
        max_retries=3,
        backoff_factor=2.0,
        retry_on=[TimeoutError, RateLimitError]
    )
)
```

### Batch Processing

```python
prompts = ["Question 1", "Question 2", "Question 3"]
responses = client.batch_complete(prompts, max_concurrent=5)
```

## API Reference

See [API Documentation](../../docs/api/llm-wrappers.md) for detailed API reference.

## Examples

Check out the [examples directory](../../examples/llm-wrappers/) for complete working examples:

- Basic chat completion
- Streaming responses
- Multi-provider switching
- Prompt templating
- Error handling
- Batch processing

## Testing

```bash
# Run all tests
python -m pytest src/test/llm-wrappers/

# Run specific test file
python -m pytest src/test/llm-wrappers/test_client.py

# Run with coverage
python -m pytest --cov=src/main/llm-wrappers src/test/llm-wrappers/
```

## Contributing

See the main [CONTRIBUTING.md](../../CONTRIBUTING.md) for general guidelines.

### LLM Wrapper Specific Guidelines

- Add tests for all new provider implementations
- Update the provider support table
- Include example usage in docstrings
- Follow the ProviderAdapter interface for consistency

## License

MIT License - see [LICENSE](../../LICENSE) file for details.

## Support

For issues specific to LLM wrappers, please tag your issue with `llm-wrappers` label.
