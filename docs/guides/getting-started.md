# Getting Started with Core Public GitHub

This guide will help you get started with the shared frameworks in this repository.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (for LLM Wrappers and Integration Utils)
- **Java 11+** (for Java-based integrations)
- **Git** for version control
- **Visual Studio Code** or your preferred IDE

## Installation

### Clone the Repository

```bash
git clone https://github.com/AzezGlobal/core.public.github.git
cd core.public.github
```

### Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Set Up Java Environment (Optional)

```bash
# Build with Gradle
gradle build

# Or if you have Gradle wrapper
./gradlew build
```

## Quick Start Examples

### Using LLM Wrappers

```python
from src.main.llm_wrappers import LLMClient

# Initialize client
client = LLMClient(
    provider="openai",
    api_key="your-api-key-here"
)

# Generate completion
response = client.complete("What is machine learning?")
print(response.text)
```

### Using Integration Utils

```python
from src.main.integration_utils import HttpClient

# Create HTTP client
client = HttpClient(
    base_url="https://api.example.com",
    timeout=30
)

# Make request
response = client.get("/users")
users = response.json()
```

### Using D365 Extensions

For D365 extensions, refer to the specific documentation:
- [D365 F&O (X++) Guide](../src/main/d365-extensions/README.md)
- [D365 CE (Plugins) Guide](../src/main/d365-extensions/README.md)

## Project Structure Overview

```
core.public.github/
├── src/
│   ├── main/               # Source code
│   │   ├── llm-wrappers/
│   │   ├── d365-extensions/
│   │   └── integration-utils/
│   └── test/              # Tests
├── docs/                  # Documentation
│   ├── api/              # API references
│   └── guides/           # How-to guides
├── examples/             # Example code
├── scripts/              # Build and deploy scripts
└── .github/workflows/    # CI/CD pipelines
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# LLM API Keys
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
AZURE_OPENAI_KEY=your-azure-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# Azure Service Bus
AZURE_SERVICE_BUS_CONNECTION=Endpoint=sb://...

# Database
DB_CONNECTION_STRING=Server=...;Database=...

# General
LOG_LEVEL=INFO
ENVIRONMENT=development
```

### Configuration Files

You can also use JSON configuration files:

```json
{
  "llm": {
    "default_provider": "openai",
    "openai": {
      "model": "gpt-4",
      "temperature": 0.7
    }
  },
  "integration": {
    "timeout": 30,
    "retry_attempts": 3
  }
}
```

## Running Tests

### Python Tests

```bash
# Run all tests
pytest src/test/

# Run with coverage
pytest src/test/ --cov=src/main/ --cov-report=html

# Run specific test file
pytest src/test/llm-wrappers/test_client.py
```

### Java Tests

```bash
# Run tests with Gradle
gradle test

# Or with wrapper
./gradlew test
```

## Building the Project

### Python Build

```bash
# Run build script
./scripts/build.sh
```

### Java Build

```bash
# Run Java build script
./scripts/build-java.sh
```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

3. **Run tests locally**
   ```bash
   pytest src/test/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## Next Steps

- Explore the [API Documentation](../api/)
- Check out [Examples](../../examples/)
- Read framework-specific guides:
  - [LLM Wrappers Guide](../../src/main/llm-wrappers/README.md)
  - [D365 Extensions Guide](../../src/main/d365-extensions/README.md)
  - [Integration Utils Guide](../../src/main/integration-utils/README.md)

## Getting Help

- Check the [FAQ](faq.md)
- Read the [Contributing Guide](../../CONTRIBUTING.md)
- Open an [issue](https://github.com/AzezGlobal/core.public.github/issues) if you need help

## Common Issues

### Python Module Not Found

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Permission Denied on Scripts

```bash
# Make scripts executable
chmod +x scripts/*.sh
```

### Java Build Failures

```bash
# Clean and rebuild
gradle clean build
```

## Resources

- [Python Documentation](https://docs.python.org/)
- [Java Documentation](https://docs.oracle.com/en/java/)
- [Gradle Documentation](https://docs.gradle.org/)
- [Git Documentation](https://git-scm.com/doc)
