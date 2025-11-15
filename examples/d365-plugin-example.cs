// D365 CE Plugin Example - Contact Validation
// This example demonstrates a pre-operation plugin for validating Contact entity creation

using System;
using Microsoft.Xrm.Sdk;

namespace D365Extensions.Examples
{
    /// <summary>
    /// Pre-operation plugin for validating Contact creation
    /// </summary>
    /// <remarks>
    /// This plugin should be registered on:
    /// - Message: Create
    /// - Entity: contact
    /// - Stage: Pre-operation
    /// </remarks>
    public class PreContactValidation : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            // Obtain the tracing service
            ITracingService tracingService =
                (ITracingService)serviceProvider.GetService(typeof(ITracingService));

            // Obtain the execution context
            IPluginExecutionContext context =
                (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));

            tracingService.Trace("PreContactValidation: Starting execution");

            // Validate the context
            if (context.InputParameters.Contains("Target") &&
                context.InputParameters["Target"] is Entity)
            {
                Entity entity = (Entity)context.InputParameters["Target"];

                try
                {
                    // Validation 1: Email is required
                    if (!entity.Contains("emailaddress1") || 
                        string.IsNullOrWhiteSpace(entity.GetAttributeValue<string>("emailaddress1")))
                    {
                        throw new InvalidPluginExecutionException(
                            "Email address is required for creating a contact."
                        );
                    }

                    // Validation 2: First name or last name is required
                    bool hasFirstName = entity.Contains("firstname") && 
                        !string.IsNullOrWhiteSpace(entity.GetAttributeValue<string>("firstname"));
                    bool hasLastName = entity.Contains("lastname") && 
                        !string.IsNullOrWhiteSpace(entity.GetAttributeValue<string>("lastname"));

                    if (!hasFirstName && !hasLastName)
                    {
                        throw new InvalidPluginExecutionException(
                            "Either first name or last name is required."
                        );
                    }

                    // Validation 3: Email format validation (basic)
                    string email = entity.GetAttributeValue<string>("emailaddress1");
                    if (!email.Contains("@") || !email.Contains("."))
                    {
                        throw new InvalidPluginExecutionException(
                            "Email address format is invalid."
                        );
                    }

                    tracingService.Trace("PreContactValidation: All validations passed");
                }
                catch (InvalidPluginExecutionException)
                {
                    throw; // Re-throw validation errors
                }
                catch (Exception ex)
                {
                    tracingService.Trace("PreContactValidation: Unexpected error: {0}", ex.ToString());
                    throw new InvalidPluginExecutionException(
                        "An unexpected error occurred during contact validation.", ex
                    );
                }
            }
            else
            {
                tracingService.Trace("PreContactValidation: Target entity not found in InputParameters");
            }
        }
    }
}

/*
 * Registration Steps:
 * 
 * 1. Build the plugin assembly
 * 2. Register using Plugin Registration Tool
 * 3. Register a new step:
 *    - Message: Create
 *    - Primary Entity: contact
 *    - Event Pipeline Stage: PreOperation
 *    - Execution Mode: Synchronous
 * 4. No images required for this validation plugin
 * 
 * Testing:
 * 
 * Test Case 1: Create contact without email
 * Expected: Error message "Email address is required"
 * 
 * Test Case 2: Create contact with email but no name
 * Expected: Error message "Either first name or last name is required"
 * 
 * Test Case 3: Create contact with invalid email format
 * Expected: Error message "Email address format is invalid"
 * 
 * Test Case 4: Create contact with valid data
 * Expected: Contact created successfully
 */
