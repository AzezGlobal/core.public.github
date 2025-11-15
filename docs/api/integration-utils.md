# Integration Utils API Documentation

## Overview

The Integration Utils library provides a comprehensive set of tools for building robust integrations between systems.

## Core Classes

### HttpClient

Main HTTP client for making REST API calls.

#### Constructor

```python
HttpClient(
    base_url: str,
    timeout: int = 30,
    headers: Optional[Dict[str, str]] = None,
    retry_config: Optional[RetryConfig] = None,
    auth: Optional[AuthBase] = None
)
```

**Parameters:**
- `base_url` (str): Base URL for all requests
- `timeout` (int): Request timeout in seconds
- `headers` (dict, optional): Default headers for all requests
- `retry_config` (RetryConfig, optional): Retry configuration
- `auth` (AuthBase, optional): Authentication handler

#### Methods

##### get()

```python
get(endpoint: str, params: Optional[Dict] = None, **kwargs) -> Response
```

Make a GET request.

##### post()

```python
post(endpoint: str, json: Optional[Dict] = None, data: Optional[Any] = None, **kwargs) -> Response
```

Make a POST request.

##### put()

```python
put(endpoint: str, json: Optional[Dict] = None, **kwargs) -> Response
```

Make a PUT request.

##### delete()

```python
delete(endpoint: str, **kwargs) -> Response
```

Make a DELETE request.

### RetryConfig

Configuration for retry behavior.

```python
class RetryConfig:
    max_retries: int = 3
    backoff_factor: float = 2.0
    retry_on: List[Type[Exception]] = [TimeoutError, ConnectionError]
    max_delay: float = 60.0
```

### Authentication

#### OAuth2Client

```python
OAuth2Client(
    client_id: str,
    client_secret: str,
    token_url: str,
    scope: Optional[str] = None
)
```

Methods:
- `get_access_token() -> str`
- `refresh_token() -> str`

#### ApiKeyAuth

```python
ApiKeyAuth(
    api_key: str,
    header_name: str = "X-API-Key"
)
```

### Data Transformation

#### DataMapper

```python
class DataMapper:
    def __init__(self, mapping: Dict[str, str])
    def transform(self, data: Dict) -> Dict
```

#### JsonTransformer

```python
class JsonTransformer:
    def to_xml(self, data: Dict) -> str
    def from_xml(self, xml_str: str) -> Dict
```

### Queue Management

#### ServiceBusClient

```python
ServiceBusClient(
    connection_string: str,
    queue_name: str
)
```

Methods:
- `send_message(message: Dict)`
- `receive_messages(max_messages: int = 1) -> List[Message]`
- `complete_message(message: Message)`

### File Processing

#### CsvProcessor

```python
class CsvProcessor:
    def read(self, file_path: str) -> List[Dict]
    def write(self, file_path: str, data: List[Dict])
```

#### ExcelProcessor

```python
class ExcelProcessor:
    def read_workbook(self, file_path: str) -> Dict[str, List[Dict]]
    def write_workbook(self, file_path: str, sheets: Dict[str, List[Dict]])
```

## Error Handling

### Exception Hierarchy

```
IntegrationError
├── ConnectionError
├── TimeoutError
├── AuthenticationError
├── RetryableError
└── NonRetryableError
```

### Error Handler Decorator

```python
@error_handler(max_retries=3, retry_on=[RetryableError])
def my_integration_function():
    pass
```

## Patterns

### Circuit Breaker

```python
from integration_utils import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    timeout=60,
    expected_exceptions=[RequestException]
)

@breaker.call
def call_external_service():
    return api.get_data()
```

### Rate Limiter

```python
from integration_utils import RateLimiter

limiter = RateLimiter(
    max_calls=100,
    time_window=60
)

@limiter.limit
def api_call():
    return client.get("/resource")
```

### Batch Processor

```python
from integration_utils import BatchProcessor

processor = BatchProcessor(
    batch_size=100,
    max_workers=5,
    process_func=process_record
)

results = processor.process_all(records)
```

## Logging

### IntegrationLogger

```python
logger = IntegrationLogger(
    name="my-integration",
    level="INFO",
    log_to_file=True,
    log_file="integration.log"
)

logger.info("Processing started")
logger.error("Error occurred", exc_info=True)

with logger.operation("sync-data") as op:
    # Work
    op.add_metric("records_processed", 100)
```

## Configuration Examples

### JSON Configuration

```json
{
  "http": {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "max_retries": 3
  },
  "queue": {
    "provider": "azure_service_bus",
    "connection_string": "${AZURE_SERVICE_BUS_CONNECTION}"
  }
}
```

### Environment Variables

```bash
API_BASE_URL=https://api.example.com
API_TIMEOUT=30
MAX_RETRIES=3
AZURE_SERVICE_BUS_CONNECTION=Endpoint=sb://...
```

## Best Practices

1. **Use retry logic** for transient failures
2. **Implement circuit breakers** for failing services
3. **Log appropriately** with structured logging
4. **Handle errors gracefully** with proper exception handling
5. **Use rate limiting** to avoid overwhelming services
6. **Batch operations** when possible for efficiency
7. **Monitor and track** integration metrics
