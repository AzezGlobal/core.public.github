# Core Public GitHub

A centralized repository for shared frameworks, utilities, and templates used across various projects.

## Overview

This repository contains reusable components and frameworks designed to accelerate development and ensure consistency across projects. It includes:

- **LLM Wrappers**: Framework for working with Large Language Models
- **D365 Extension Templates**: Templates and utilities for Dynamics 365 extensions
- **Integration Utils**: Common utilities for system integrations

## Repository Structure

```
core.public.github/
├── src/                   # Source code
│   ├── main/              # Core implementation
│   │   ├── llm-wrappers/
│   │   ├── d365-extensions/
│   │   └── integration-utils/
│   └── test/              # Test files
├── docs/                  # Documentation
│   ├── api/               # API specifications
│   └── guides/            # Setup and tutorials
├── examples/              # Demo and sample code
├── scripts/               # Build and deployment scripts
├── .github/workflows/     # CI/CD pipelines
├── requirements.txt       # Python dependencies
├── build.gradle           # Java dependencies
└── CONTRIBUTING.md        # Contribution guidelines
```

## Getting Started

Each framework has its own directory with dedicated documentation. Navigate to the specific framework directory for detailed setup and usage instructions.

For a complete getting started guide, see [Getting Started Guide](docs/guides/getting-started.md).

### LLM Wrappers

Located in `src/main/llm-wrappers/`, this framework provides unified interfaces for working with various Large Language Model providers.

[Read more →](src/main/llm-wrappers/README.md)

### D365 Extensions

Located in `src/main/d365-extensions/`, contains templates and utilities for extending Microsoft Dynamics 365.

[Read more →](src/main/d365-extensions/README.md)

### Integration Utils

Located in `src/main/integration-utils/`, provides common utilities for building integrations between systems.

[Read more →](src/main/integration-utils/README.md)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions or issues, please open an issue in this repository.