"""
Integration Utils - HTTP Client Example

This example demonstrates:
- Creating an HTTP client with retry logic
- Making GET, POST, PUT, DELETE requests
- Handling errors and retries
- Using authentication
"""

import json
from typing import Optional, Dict, Any


class RetryConfig:
    """Configuration for retry behavior."""
    
    def __init__(self, max_retries: int = 3, backoff_factor: float = 2.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor


class HttpClient:
    """Simple HTTP client with retry logic."""
    
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        headers: Optional[Dict[str, str]] = None,
        retry_config: Optional[RetryConfig] = None
    ):
        """
        Initialize HTTP client.
        
        Args:
            base_url: Base URL for all requests
            timeout: Request timeout in seconds
            headers: Default headers for all requests
            retry_config: Retry configuration
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.headers = headers or {}
        self.retry_config = retry_config or RetryConfig()
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a GET request."""
        url = f"{self.base_url}{endpoint}"
        print(f"GET {url}")
        
        # Simulated response
        return {
            "status_code": 200,
            "data": {"message": "GET request successful", "endpoint": endpoint}
        }
    
    def post(self, endpoint: str, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a POST request."""
        url = f"{self.base_url}{endpoint}"
        print(f"POST {url}")
        print(f"Data: {json.dumps(json_data, indent=2)}")
        
        # Simulated response
        return {
            "status_code": 201,
            "data": {"message": "POST request successful", "created": True}
        }
    
    def put(self, endpoint: str, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a PUT request."""
        url = f"{self.base_url}{endpoint}"
        print(f"PUT {url}")
        
        # Simulated response
        return {
            "status_code": 200,
            "data": {"message": "PUT request successful", "updated": True}
        }
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        print(f"DELETE {url}")
        
        # Simulated response
        return {
            "status_code": 204,
            "data": {"message": "DELETE request successful"}
        }


def main():
    """Main example function."""
    
    # Example 1: Basic HTTP requests
    print("Example 1: Basic HTTP Requests")
    print("-" * 50)
    
    client = HttpClient(
        base_url="https://api.example.com",
        timeout=30,
        headers={"Content-Type": "application/json"}
    )
    
    # GET request
    response = client.get("/users")
    print(f"Status: {response['status_code']}")
    print(f"Data: {response['data']}")
    print()
    
    # POST request
    new_user = {"name": "John Doe", "email": "john@example.com"}
    response = client.post("/users", json_data=new_user)
    print(f"Status: {response['status_code']}")
    print(f"Data: {response['data']}")
    print()
    
    # PUT request
    updated_user = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.put("/users/123", json_data=updated_user)
    print(f"Status: {response['status_code']}")
    print(f"Data: {response['data']}")
    print()
    
    # DELETE request
    response = client.delete("/users/123")
    print(f"Status: {response['status_code']}")
    print()
    
    # Example 2: Client with retry configuration
    print("\nExample 2: Client with Retry Configuration")
    print("-" * 50)
    
    retry_config = RetryConfig(max_retries=5, backoff_factor=2.0)
    client_with_retry = HttpClient(
        base_url="https://api.example.com",
        retry_config=retry_config
    )
    
    print(f"Max retries: {client_with_retry.retry_config.max_retries}")
    print(f"Backoff factor: {client_with_retry.retry_config.backoff_factor}")
    
    response = client_with_retry.get("/health")
    print(f"Response: {response}")
    print()
    
    # Example 3: Authenticated requests
    print("\nExample 3: Authenticated Requests")
    print("-" * 50)
    
    auth_client = HttpClient(
        base_url="https://api.example.com",
        headers={
            "Authorization": "Bearer abc123token",
            "Content-Type": "application/json"
        }
    )
    
    response = auth_client.get("/protected/resource")
    print(f"Authenticated request successful")
    print(f"Response: {response['data']}")


if __name__ == "__main__":
    print("=" * 50)
    print("Integration Utils - HTTP Client Example")
    print("=" * 50)
    print("\n")
    
    main()
    
    print("\n")
    print("=" * 50)
    print("Example completed!")
    print("=" * 50)
    print("\nNote: This example uses simulated responses.")
    print("In production, it would make actual HTTP requests.")
