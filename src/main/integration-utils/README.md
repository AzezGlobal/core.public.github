# Integration Utilities

Common utilities and patterns for building integrations between systems.

## Overview

This library provides reusable utilities for building robust integrations. It includes helpers for API communication, data transformation, error handling, authentication, and more.

## Features

- **HTTP Client Wrapper**: Simplified HTTP/REST API communication
- **Authentication Helpers**: OAuth 2.0, API Key, JWT support
- **Data Transformation**: JSON/XML parsing, mapping, and transformation
- **Retry Logic**: Configurable retry with exponential backoff
- **Logging & Monitoring**: Structured logging and metrics
- **Queue Management**: Message queue utilities (Azure Service Bus, RabbitMQ)
- **File Processing**: CSV, Excel, JSON file handlers
- **Error Handling**: Standardized error handling patterns

## Quick Start

### Installation

```bash
# Python
pip install -r requirements.txt

# Java/Maven
mvn install

# .NET
dotnet restore
```

### Basic HTTP Client Usage

```python
from integration_utils import HttpClient, RetryConfig

# Create client with retry logic
client = HttpClient(
    base_url="https://api.example.com",
    timeout=30,
    retry_config=RetryConfig(max_retries=3, backoff_factor=2.0)
)

# Make authenticated request
response = client.get(
    "/users",
    headers={"Authorization": f"Bearer {token}"}
)

users = response.json()
```

### Authentication Examples

#### OAuth 2.0

```python
from integration_utils.auth import OAuth2Client

auth = OAuth2Client(
    client_id="your-client-id",
    client_secret="your-client-secret",
    token_url="https://auth.example.com/token"
)

token = auth.get_access_token()
```

#### API Key Authentication

```python
from integration_utils.auth import ApiKeyAuth

auth = ApiKeyAuth(api_key="your-api-key", header_name="X-API-Key")
client = HttpClient(auth=auth)
```

## Core Components

### 1. HTTP Client

Simplified HTTP client with built-in retry, timeout, and error handling:

```python
from integration_utils import HttpClient

client = HttpClient(
    base_url="https://api.example.com",
    timeout=30,
    headers={"Content-Type": "application/json"}
)

# GET request
response = client.get("/resource")

# POST request
response = client.post("/resource", json={"key": "value"})

# PUT request
response = client.put("/resource/123", json={"key": "updated"})

# DELETE request
response = client.delete("/resource/123")
```

### 2. Data Transformation

Utilities for transforming data between formats:

```python
from integration_utils.transform import DataMapper, JsonTransformer

# Define field mapping
mapper = DataMapper({
    "source_field": "target_field",
    "nested.source": "flat_target",
    "array[0]": "first_element"
})

# Transform data
source_data = {"source_field": "value", "nested": {"source": "data"}}
target_data = mapper.transform(source_data)

# JSON to XML conversion
transformer = JsonTransformer()
xml_output = transformer.to_xml(json_data)
```

### 3. Queue Management

Work with message queues:

```python
from integration_utils.queue import ServiceBusClient

# Azure Service Bus example
client = ServiceBusClient(
    connection_string="your-connection-string",
    queue_name="integration-queue"
)

# Send message
client.send_message({"event": "user.created", "user_id": 123})

# Receive and process messages
for message in client.receive_messages(max_messages=10):
    process_message(message.body)
    client.complete_message(message)
```

### 4. File Processing

Handle various file formats:

```python
from integration_utils.files import CsvProcessor, ExcelProcessor

# CSV processing
csv_processor = CsvProcessor()
data = csv_processor.read("input.csv")
filtered_data = [row for row in data if row["status"] == "active"]
csv_processor.write("output.csv", filtered_data)

# Excel processing
excel_processor = ExcelProcessor()
sheets = excel_processor.read_workbook("data.xlsx")
excel_processor.write_workbook("output.xlsx", sheets)
```

### 5. Error Handling

Standardized error handling:

```python
from integration_utils.errors import (
    IntegrationError,
    RetryableError,
    NonRetryableError,
    error_handler
)

@error_handler(max_retries=3, retry_on=[RetryableError])
def process_integration():
    try:
        # Integration logic
        result = external_api_call()
        return result
    except TimeoutError as e:
        raise RetryableError("API timeout") from e
    except ValidationError as e:
        raise NonRetryableError("Invalid data") from e
```

### 6. Logging & Monitoring

Structured logging:

```python
from integration_utils.logging import IntegrationLogger

logger = IntegrationLogger(
    name="my-integration",
    level="INFO",
    log_to_file=True,
    log_file="integration.log"
)

logger.info("Integration started", extra={"source": "SystemA", "target": "SystemB"})
logger.error("Integration failed", extra={"error": str(error)}, exc_info=True)

# Context manager for tracking
with logger.operation("sync-users") as op:
    # Work happens here
    op.add_metric("users_processed", 150)
    op.add_metric("duration_ms", 1234)
```

## Configuration

### Configuration File (config.json)

```json
{
  "http": {
    "timeout": 30,
    "max_retries": 3,
    "backoff_factor": 2.0,
    "verify_ssl": true
  },
  "logging": {
    "level": "INFO",
    "format": "json",
    "file": "integration.log"
  },
  "queue": {
    "provider": "azure_service_bus",
    "connection_string": "${AZURE_SERVICE_BUS_CONNECTION}",
    "retry_policy": {
      "max_retries": 3,
      "delay": 1.0
    }
  }
}
```

### Environment Variables

```bash
# API Configuration
export API_BASE_URL="https://api.example.com"
export API_KEY="your-api-key"
export API_TIMEOUT=30

# Queue Configuration
export AZURE_SERVICE_BUS_CONNECTION="Endpoint=sb://..."
export QUEUE_NAME="integration-queue"

# Database Configuration
export DB_CONNECTION_STRING="Server=..."
```

## Patterns & Best Practices

### 1. Retry Pattern

```python
from integration_utils import retry_with_backoff

@retry_with_backoff(max_attempts=3, base_delay=1.0, max_delay=10.0)
def call_unreliable_api():
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
    return response.json()
```

### 2. Circuit Breaker

```python
from integration_utils import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    timeout=60,
    expected_exceptions=[RequestException]
)

@breaker.call
def call_external_service():
    return external_api.get_data()
```

### 3. Rate Limiting

```python
from integration_utils import RateLimiter

limiter = RateLimiter(max_calls=100, time_window=60)

@limiter.limit
def api_call():
    return client.get("/resource")
```

### 4. Batch Processing

```python
from integration_utils import BatchProcessor

processor = BatchProcessor(
    batch_size=100,
    max_workers=5,
    process_func=process_record
)

records = fetch_records()
results = processor.process_all(records)
```

## Testing

```bash
# Python tests
python -m pytest src/test/integration-utils/

# With coverage
python -m pytest --cov=src/main/integration-utils src/test/integration-utils/

# Specific test
python -m pytest src/test/integration-utils/test_http_client.py
```

### Example Test

```python
import pytest
from integration_utils import HttpClient

def test_http_client_get():
    client = HttpClient(base_url="https://api.example.com")
    response = client.get("/users")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_retry_on_timeout(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.side_effect = [Timeout(), Response(200)]
    
    client = HttpClient(max_retries=2)
    response = client.get("/resource")
    
    assert response.status_code == 200
    assert mock_get.call_count == 2
```

## API Reference

See [Integration Utils API Documentation](../../docs/api/integration-utils.md) for detailed API reference.

## Examples

Check out the [examples directory](../../examples/integration-utils/) for complete working examples:

- REST API integration with retry logic
- OAuth 2.0 authentication flow
- Azure Service Bus message processing
- CSV to API data synchronization
- Error handling and logging
- Batch processing pipeline

## Supported Platforms

- **Python**: 3.8+
- **Java**: 11+
- **.NET**: 6.0+
- **Node.js**: 16+ (coming soon)

## Dependencies

### Python
- requests
- pyjwt
- azure-servicebus
- pandas (for file processing)

### Java
- Apache HttpClient
- Jackson (JSON processing)
- Spring Framework (optional)

### .NET
- System.Net.Http
- Newtonsoft.Json
- Azure.Messaging.ServiceBus

## Contributing

See the main [CONTRIBUTING.md](../../CONTRIBUTING.md) for general guidelines.

### Integration Utils Specific Guidelines

- Keep utilities generic and framework-agnostic
- Include comprehensive error handling
- Add unit tests with mocking
- Document all public APIs
- Provide usage examples

## License

MIT License - see [LICENSE](../../LICENSE) file for details.

## Support

For issues specific to integration utilities, please tag your issue with `integration-utils` label.
