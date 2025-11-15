# D365 Extension Templates

Templates and utilities for extending Microsoft Dynamics 365 with best practices and reusable components.

## Overview

This framework provides pre-built templates, utilities, and patterns for developing Dynamics 365 extensions. It supports both Finance & Operations (X++) and Customer Engagement (plugins/workflows).

## Features

- **X++ Extension Templates**: Common patterns for D365 F&O extensions
- **Plugin Templates**: C# plugin scaffolding for CE/CRM
- **Workflow Templates**: Custom workflow activities
- **Integration Patterns**: Common integration scenarios
- **Data Migration Utilities**: Tools for data import/export
- **Deployment Scripts**: Automated deployment helpers

## Quick Start

### Prerequisites

- Visual Studio 2019 or later
- Dynamics 365 SDK (for CE plugins)
- X++ development environment (for F&O)
- .NET Framework 4.6.2+ or .NET 6+

### Project Structure

```
d365-extensions/
├── xpp/                    # X++ extensions for F&O
│   ├── classes/           # Custom classes
│   ├── forms/             # Form extensions
│   └── tables/            # Table extensions
├── plugins/               # CE/CRM plugins (C#)
│   ├── pre-operation/    # Pre-operation plugins
│   └── post-operation/   # Post-operation plugins
├── workflows/             # Custom workflow activities
├── webresources/          # Web resources (JS, CSS, HTML)
└── data-entities/         # Custom data entities
```

## X++ Extensions (Finance & Operations)

### Example: Custom Table Extension

```xpp
[ExtensionOf(tableStr(CustTable))]
final class CustTable_Extension
{
    public void validateWrite()
    {
        next validateWrite();
        
        // Custom validation logic
        if (!this.MyCustomField)
        {
            error("Custom field is required");
        }
    }
}
```

### Example: Form Extension

```xpp
[ExtensionOf(formStr(CustTable))]
final class CustTable_Form_Extension
{
    public void init()
    {
        next init();
        
        // Custom initialization
        this.setupCustomControls();
    }
    
    private void setupCustomControls()
    {
        // Control setup logic
    }
}
```

## CE/CRM Plugins (C#)

### Example: Pre-Operation Plugin

```csharp
using Microsoft.Xrm.Sdk;
using System;

namespace D365Extensions.Plugins
{
    public class PreContactCreate : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            ITracingService tracingService = 
                (ITracingService)serviceProvider.GetService(typeof(ITracingService));
            
            IPluginExecutionContext context = 
                (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
            
            IOrganizationServiceFactory serviceFactory = 
                (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
            
            IOrganizationService service = 
                serviceFactory.CreateOrganizationService(context.UserId);
            
            try
            {
                if (context.InputParameters.Contains("Target") && 
                    context.InputParameters["Target"] is Entity)
                {
                    Entity entity = (Entity)context.InputParameters["Target"];
                    
                    // Custom pre-create logic
                    if (!entity.Contains("emailaddress1"))
                    {
                        throw new InvalidPluginExecutionException("Email is required");
                    }
                }
            }
            catch (Exception ex)
            {
                tracingService.Trace("PreContactCreate: {0}", ex.ToString());
                throw;
            }
        }
    }
}
```

## Templates Available

### 1. CRUD Operations Template
- Standard Create, Read, Update, Delete patterns
- Error handling and validation
- Audit logging integration

### 2. Integration Service Template
- RESTful API integration
- OAuth authentication
- Retry logic and error handling

### 3. Batch Processing Template
- Large data set processing
- Progress tracking
- Cancellation support

### 4. Custom Workflow Activity
- Workflow activity scaffolding
- Input/output parameters
- Error handling

## Configuration

### X++ Configuration

Create a configuration class:

```xpp
class D365ExtensionConfig
{
    public static str getConfigValue(str configKey)
    {
        // Retrieve from parameters table
        D365ExtensionParameters parameters = D365ExtensionParameters::find();
        
        switch (configKey)
        {
            case 'ApiEndpoint':
                return parameters.ApiEndpoint;
            case 'ApiKey':
                return parameters.ApiKey;
            default:
                return '';
        }
    }
}
```

### Plugin Configuration

Use Plugin Configuration or Environment Variables:

```csharp
public class PluginConfig
{
    public string ApiEndpoint { get; set; }
    public int TimeoutSeconds { get; set; }
    
    public static PluginConfig FromUnsecureConfig(string config)
    {
        return JsonConvert.DeserializeObject<PluginConfig>(config);
    }
}
```

## Deployment

### X++ Deployment

1. Build the model
2. Create deployable package
3. Deploy via LCS

```bash
# Using scripts/deploy-d365-xpp.ps1
.\scripts\deploy-d365-xpp.ps1 -Environment "UAT" -Package "MyExtension.axdeployablepackage"
```

### Plugin Deployment

1. Build the plugin assembly
2. Register using Plugin Registration Tool
3. Configure steps and images

```bash
# Using scripts/deploy-d365-plugin.ps1
.\scripts\deploy-d365-plugin.ps1 -Assembly "MyPlugin.dll" -Environment "Production"
```

## Testing

### X++ Unit Tests

```xpp
class MyExtension_Test extends SysTestCase
{
    public void testCustomValidation()
    {
        CustTable custTable;
        
        // Arrange
        custTable.initValue();
        custTable.AccountNum = 'TEST001';
        
        // Act & Assert
        this.assertTrue(custTable.validateWrite());
    }
}
```

### Plugin Unit Tests

```csharp
[TestClass]
public class PreContactCreateTests
{
    [TestMethod]
    public void TestContactCreate_WithEmail_Success()
    {
        // Arrange
        var plugin = new PreContactCreate();
        var serviceProvider = CreateMockServiceProvider();
        
        // Act
        plugin.Execute(serviceProvider);
        
        // Assert
        // Assertions here
    }
}
```

## Best Practices

1. **Use Extension Pattern**: Prefer extensions over overlayering
2. **Handle Errors Gracefully**: Always include proper error handling
3. **Log Appropriately**: Use tracing for debugging
4. **Test Thoroughly**: Unit test all custom logic
5. **Document Changes**: Keep documentation up-to-date
6. **Version Control**: Use proper branching strategy
7. **Security**: Never hardcode credentials

## API Reference

See [D365 Extensions API Documentation](../../docs/api/d365-extensions.md) for detailed API reference.

## Examples

Check out the [examples directory](../../examples/d365-extensions/) for complete working examples:

- Table extensions with validation
- Form extensions with custom controls
- Plugin with external API integration
- Custom workflow activity
- Data entity creation

## Resources

- [Microsoft Dynamics 365 Documentation](https://docs.microsoft.com/dynamics365/)
- [X++ Language Reference](https://docs.microsoft.com/dynamicsax-2012/developer/x-language-reference)
- [Plugin Development](https://docs.microsoft.com/power-apps/developer/data-platform/plug-ins)

## Contributing

See the main [CONTRIBUTING.md](../../CONTRIBUTING.md) for general guidelines.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.

## Support

For issues specific to D365 extensions, please tag your issue with `d365-extensions` label.
