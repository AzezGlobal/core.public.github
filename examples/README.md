# Examples

This directory contains practical examples demonstrating how to use the various frameworks and utilities in this repository.

## Available Examples

### LLM Wrappers

- **llm-wrappers-basic.py** - Basic usage of the LLM wrapper framework
  - Client initialization
  - Making completion requests
  - Error handling
  - Multi-provider support

### Integration Utils

- **integration-utils-http.py** - HTTP client usage examples
  - GET, POST, PUT, DELETE requests
  - Retry configuration
  - Authentication
  - Error handling

### D365 Extensions

- **d365-plugin-example.cs** - D365 CE plugin example
  - Pre-operation validation plugin
  - Contact entity validation
  - Error handling in plugins
  - Registration instructions

## Running the Examples

### Python Examples

```bash
# Make sure you're in the project root
cd /path/to/core.public.github

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Run an example
python examples/llm-wrappers-basic.py
python examples/integration-utils-http.py
```

### C# Examples

```bash
# Compile the plugin example (requires .NET SDK and D365 SDK references)
csc /target:library /reference:Microsoft.Xrm.Sdk.dll examples/d365-plugin-example.cs
```

## Example Structure

Each example is self-contained and includes:
- Clear comments explaining the code
- Error handling demonstrations
- Expected outputs
- Configuration requirements

## Configuration

Some examples require configuration:

### Environment Variables

```bash
# For LLM examples
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"

# For integration examples
export API_BASE_URL="https://api.example.com"
export API_KEY="your-api-key"
```

### Configuration Files

You can also create a `.env` file in the project root:

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
API_BASE_URL=https://api.example.com
```

## Example Categories

### 1. Basic Examples
- Simple, straightforward usage
- Minimal configuration
- Good starting point for beginners

### 2. Advanced Examples
- Complex scenarios
- Multiple components working together
- Production-ready patterns

### 3. Integration Examples
- Real-world integration scenarios
- End-to-end workflows
- Best practices demonstrations

## Contributing Examples

When adding new examples:

1. **Keep it simple** - Focus on one concept at a time
2. **Add comments** - Explain what the code does
3. **Include error handling** - Show how to handle failures
4. **Provide context** - Explain when to use this pattern
5. **Test it** - Make sure the example works

## Tips

- Start with basic examples before moving to advanced ones
- Read the framework documentation for detailed API references
- Modify examples to experiment and learn
- Check example output to understand expected behavior

## Need Help?

- Check the main [README](../README.md)
- Read the [Getting Started Guide](../docs/guides/getting-started.md)
- Review framework-specific documentation in `src/main/*/README.md`
- Open an issue if you have questions

## More Examples Coming Soon

We're continuously adding new examples. Check back regularly or watch the repository for updates.

Planned examples:
- Streaming LLM responses
- Batch processing with integration utils
- D365 workflow activities
- Azure Service Bus integration
- OAuth authentication flows
- Data transformation pipelines
