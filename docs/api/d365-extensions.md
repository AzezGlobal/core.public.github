# D365 Extensions API Documentation

## X++ Extensions (Finance & Operations)

### Table Extensions

#### Creating a Table Extension

```xpp
[ExtensionOf(tableStr(CustTable))]
final class CustTable_Extension
{
    public void insert()
    {
        // Pre-insert logic
        this.validateCustomFields();
        
        next insert();
        
        // Post-insert logic
        this.logCustomerCreation();
    }
    
    private void validateCustomFields()
    {
        if (!this.MyCustomField)
        {
            throw error("Custom field validation failed");
        }
    }
    
    private void logCustomerCreation()
    {
        // Logging logic
        info(strFmt("Customer %1 created", this.AccountNum));
    }
}
```

### Form Extensions

#### Extending Forms

```xpp
[ExtensionOf(formStr(CustTable))]
final class CustTable_Form_Extension
{
    public void init()
    {
        next init();
        this.setupCustomControls();
    }
    
    private void setupCustomControls()
    {
        FormStringControl customControl;
        customControl = this.design().controlName("MyCustomControl");
        
        if (customControl)
        {
            customControl.visible(true);
        }
    }
}
```

### Class Extensions

```xpp
[ExtensionOf(classStr(CustTableService))]
final class CustTableService_Extension
{
    public void customMethod()
    {
        // Custom logic
    }
}
```

## CE/CRM Plugins (C#)

### IPlugin Interface

All plugins must implement the `IPlugin` interface:

```csharp
public interface IPlugin
{
    void Execute(IServiceProvider serviceProvider);
}
```

### Plugin Structure

```csharp
using Microsoft.Xrm.Sdk;
using System;

namespace D365Extensions.Plugins
{
    public class MyPlugin : IPlugin
    {
        private readonly string _unsecureConfig;
        private readonly string _secureConfig;
        
        // Constructor for configuration
        public MyPlugin(string unsecureConfig, string secureConfig)
        {
            _unsecureConfig = unsecureConfig;
            _secureConfig = secureConfig;
        }
        
        public void Execute(IServiceProvider serviceProvider)
        {
            // Get services
            ITracingService tracingService = 
                (ITracingService)serviceProvider.GetService(typeof(ITracingService));
            
            IPluginExecutionContext context = 
                (IPluginExecutionContext)serviceProvider.GetService(
                    typeof(IPluginExecutionContext));
            
            IOrganizationServiceFactory serviceFactory = 
                (IOrganizationServiceFactory)serviceProvider.GetService(
                    typeof(IOrganizationServiceFactory));
            
            IOrganizationService service = 
                serviceFactory.CreateOrganizationService(context.UserId);
            
            try
            {
                // Plugin logic here
                ProcessEntity(context, service, tracingService);
            }
            catch (Exception ex)
            {
                tracingService.Trace("Error: {0}", ex.ToString());
                throw new InvalidPluginExecutionException(
                    "An error occurred in MyPlugin.", ex);
            }
        }
        
        private void ProcessEntity(
            IPluginExecutionContext context,
            IOrganizationService service,
            ITracingService tracingService)
        {
            // Implementation
        }
    }
}
```

### Plugin Stages

| Stage | Name | Description |
|-------|------|-------------|
| 10 | PreValidation | Before database transaction |
| 20 | PreOperation | Inside database transaction, before save |
| 40 | PostOperation | Inside database transaction, after save |

### Common Plugin Patterns

#### Pre-Validation Plugin

```csharp
public class PreValidationPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider
            .GetService(typeof(IPluginExecutionContext));
        
        if (context.Stage != 10) // PreValidation
            return;
            
        Entity entity = context.InputParameters["Target"] as Entity;
        
        // Validation logic
        if (!entity.Contains("emailaddress1"))
        {
            throw new InvalidPluginExecutionException("Email required");
        }
    }
}
```

#### Post-Operation Plugin

```csharp
public class PostOperationPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider
            .GetService(typeof(IPluginExecutionContext));
        
        if (context.Stage != 40) // PostOperation
            return;
        
        var serviceFactory = (IOrganizationServiceFactory)serviceProvider
            .GetService(typeof(IOrganizationServiceFactory));
        var service = serviceFactory.CreateOrganizationService(context.UserId);
        
        Entity entity = context.InputParameters["Target"] as Entity;
        
        // Create related records, send notifications, etc.
    }
}
```

## Custom Workflow Activities

### Workflow Activity Structure

```csharp
using Microsoft.Xrm.Sdk.Workflow;
using System.Activities;

namespace D365Extensions.Workflows
{
    public class CustomWorkflowActivity : CodeActivity
    {
        [Input("Input Parameter")]
        [Default("Default Value")]
        public InArgument<string> InputParameter { get; set; }
        
        [Output("Output Parameter")]
        public OutArgument<string> OutputParameter { get; set; }
        
        protected override void Execute(CodeActivityContext context)
        {
            IWorkflowContext workflowContext = context
                .GetExtension<IWorkflowContext>();
            
            IOrganizationServiceFactory serviceFactory = context
                .GetExtension<IOrganizationServiceFactory>();
            
            IOrganizationService service = serviceFactory
                .CreateOrganizationService(workflowContext.UserId);
            
            // Get input
            string input = InputParameter.Get(context);
            
            // Process
            string result = ProcessData(input, service);
            
            // Set output
            OutputParameter.Set(context, result);
        }
        
        private string ProcessData(string input, IOrganizationService service)
        {
            // Implementation
            return input.ToUpper();
        }
    }
}
```

## Data Entities (X++)

### Creating Custom Data Entity

```xpp
[DataEntityAttribute("MyCustomEntity")]
public class MyCustomEntityEntity extends common
{
    // Fields
    public CustAccount AccountNum;
    public Name Name;
    
    // Methods
    public void mapToEntity(CustTable _custTable)
    {
        this.AccountNum = _custTable.AccountNum;
        this.Name = _custTable.Name;
    }
    
    public void mapFromEntity(CustTable _custTable)
    {
        _custTable.AccountNum = this.AccountNum;
        _custTable.Name = this.Name;
    }
}
```

## Deployment

### Plugin Registration

1. **Build Assembly**
   ```bash
   dotnet build --configuration Release
   ```

2. **Register with Plugin Registration Tool**
   - Connect to environment
   - Register assembly
   - Register steps and images

### X++ Deployment

1. **Create Deployable Package**
   ```bash
   # Build in Visual Studio
   # Export as deployable package
   ```

2. **Deploy via LCS**
   - Upload to Asset Library
   - Deploy to environment
   - Monitor deployment status

## Best Practices

### Plugin Development
1. Keep plugins stateless
2. Use early-bound types
3. Implement proper error handling
4. Use tracing for debugging
5. Minimize plugin execution time
6. Use plugin images efficiently

### X++ Development
1. Use extension patterns
2. Follow naming conventions
3. Implement proper error handling
4. Use RunBase for batch operations
5. Follow security best practices

## Common Issues

### Plugin Timeout
- Reduce complexity
- Move to asynchronous processing
- Optimize database queries

### X++ Compilation Errors
- Check references
- Verify extension syntax
- Update metadata

## Resources

- [Microsoft Dynamics 365 Documentation](https://docs.microsoft.com/dynamics365/)
- [Plugin Development Guide](https://docs.microsoft.com/power-apps/developer/data-platform/plug-ins)
- [X++ Language Reference](https://docs.microsoft.com/dynamicsax-2012/developer/x-language-reference)
