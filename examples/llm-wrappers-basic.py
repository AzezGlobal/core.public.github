"""
Basic example of using the LLM Wrappers framework.

This example demonstrates:
- Initializing an LLM client
- Making a simple completion request
- Handling responses
- Basic error handling
"""

import os
from typing import Optional


class LLMClient:
    """Example LLM Client implementation."""
    
    def __init__(self, provider: str, api_key: Optional[str] = None):
        """
        Initialize LLM client.
        
        Args:
            provider: The LLM provider ('openai', 'anthropic', etc.)
            api_key: API key for authentication
        """
        self.provider = provider
        self.api_key = api_key or os.getenv(f"{provider.upper()}_API_KEY")
        
        if not self.api_key:
            raise ValueError(f"API key required for {provider}")
    
    def complete(self, prompt: str, max_tokens: int = 100) -> dict:
        """
        Generate a completion for the given prompt.
        
        Args:
            prompt: The input prompt
            max_tokens: Maximum tokens to generate
            
        Returns:
            Dictionary with completion response
        """
        # This is a placeholder - actual implementation would call the provider API
        return {
            "text": f"[Response to: {prompt[:50]}...]",
            "tokens_used": max_tokens,
            "model": f"{self.provider}-model"
        }


def main():
    """Main example function."""
    
    # Example 1: Basic completion
    print("Example 1: Basic Completion")
    print("-" * 50)
    
    try:
        # Initialize client (using environment variable for API key)
        client = LLMClient(provider="openai")
        
        # Make a simple request
        prompt = "Explain what machine learning is in simple terms."
        response = client.complete(prompt, max_tokens=150)
        
        print(f"Prompt: {prompt}")
        print(f"Response: {response['text']}")
        print(f"Tokens used: {response['tokens_used']}")
        print(f"Model: {response['model']}")
        
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set OPENAI_API_KEY environment variable")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n")
    
    # Example 2: Multiple providers
    print("Example 2: Using Multiple Providers")
    print("-" * 50)
    
    providers = ["openai", "anthropic"]
    prompt = "What is Python?"
    
    for provider in providers:
        try:
            client = LLMClient(provider=provider)
            response = client.complete(prompt)
            print(f"{provider}: {response['text']}")
        except ValueError:
            print(f"{provider}: API key not configured")
    
    print("\n")
    
    # Example 3: Error handling
    print("Example 3: Error Handling")
    print("-" * 50)
    
    try:
        # This will raise an error due to missing API key
        client = LLMClient(provider="test_provider", api_key=None)
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    # Set up example environment (in real usage, use actual API keys)
    os.environ["OPENAI_API_KEY"] = "sk-example-key-not-real"
    os.environ["ANTHROPIC_API_KEY"] = "sk-ant-example-key-not-real"
    
    print("=" * 50)
    print("LLM Wrappers - Basic Example")
    print("=" * 50)
    print("\n")
    
    main()
    
    print("\n")
    print("=" * 50)
    print("Example completed!")
    print("=" * 50)
    print("\nNote: This is a simplified example.")
    print("In production, use actual API keys and error handling.")
