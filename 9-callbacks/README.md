# Callbacks in ADK

## ADK Concept: Callbacks

In the Google Agent Development Kit (ADK), callbacks are powerful mechanisms that allow you to intercept and modify the behavior of agents at specific points in their execution flow. Callbacks enable you to add custom logic, implement monitoring, override decisions, and extend the functionality of agents.

### What are Callbacks in ADK?

Callbacks in ADK are functions that are triggered at specific points during an agent's execution lifecycle. They provide hooks into the agent's processing pipeline, allowing you to:

- Execute custom code before or after key operations
- Monitor and log agent activities
- Override or modify agent behavior
- Implement business logic that's separate from the agent's core functionality
- Add validation, security checks, or custom processing

### Types of Callbacks in ADK

ADK provides several types of callbacks for different parts of the agent execution flow:

1. **Agent Callbacks**:
   - `before_agent_callback`: Executed before the agent processes a request
   - `after_agent_callback`: Executed after the agent processes a request

2. **Model Callbacks**:
   - `before_model_callback`: Executed before the model generates a response
   - `after_model_callback`: Executed after the model generates a response

3. **Tool Callbacks**:
   - `before_tool_callback`: Executed before a tool is called
   - `after_tool_callback`: Executed after a tool completes execution

[Callbacks](google_adk_images\callbacks.png)

### Callback Context

All callbacks receive a `CallbackContext` object that provides access to:

- The current session state
- The message being processed
- The agent's configuration
- The previous or upcoming model responses (depending on the callback type)
- Tool information (for tool callbacks)

## Implementation Details

This folder contains examples of different callback implementations in ADK:

### Project Structure
```
9-callbacks/
├── before_after_callback_agent/
│   ├── agent.py
│   └── __init__.py
├── before_after_model_callback/
│   ├── agent.py
│   └── __init__.py
└── before_after_tool_callback/
    ├── agent.py
    └── __init__.py
```

### Examples

#### 1. Agent Callbacks (before_after_callback_agent/agent.py)

This example demonstrates how to implement before and after agent callbacks for logging and performance monitoring:

```python
def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent starts processing a request.
    """
    # Get the session state
    state = callback_context.state

    # Record timestamp
    timestamp = datetime.now()

    # Set agent name if not present
    if "agent_name" not in state:
        state["agent_name"] = "SimpleChatBot"

    # Initialize request counter
    if "request_counter" not in state:
        state["request_counter"] = 1
    else:
        state["request_counter"] += 1

    # Store start time for duration calculation in after_agent_callback
    state["request_start_time"] = timestamp

    # Log the request
    print("=== AGENT EXECUTION STARTED ===")
    print(f"Request #: {state['request_counter']}")
    print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    return None


def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent finishes processing a request.
    """
    # Get the session state
    state = callback_context.state

    # Calculate request duration if start time is available
    timestamp = datetime.now()
    duration = None
    if "request_start_time" in state:
        duration = (timestamp - state["request_start_time"]).total_seconds()

    # Log the completion
    print("=== AGENT EXECUTION COMPLETED ===")
    print(f"Request #: {state.get('request_counter', 'Unknown')}")
    if duration is not None:
        print(f"Duration: {duration:.2f} seconds")

    return None


# Create the Agent
root_agent = LlmAgent(
    name="before_after_callback_agent",
    model="gemini-2.0-flash",
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
)
```

#### 2. Model Callbacks (before_after_model_callback/agent.py)

Model callbacks allow you to intercept and modify model inputs and outputs:

```python
def before_model_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Executed before the model generates a response.
    Can modify the model inputs or provide a response directly.
    """
    # Access model inputs
    model_request = callback_context.model_request
    
    # Log the request
    print(f"Model request: {model_request}")
    
    # You could modify the request here if needed
    
    return None  # Return None to continue with normal model processing


def after_model_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Executed after the model generates a response.
    Can modify the model's response or create a completely new one.
    """
    # Access model response
    model_response = callback_context.model_response
    
    # Log the response
    print(f"Model response: {model_response}")
    
    # You could modify the response here if needed
    
    return None  # Return None to use the original model response
```

#### 3. Tool Callbacks (before_after_tool_callback/agent.py)

Tool callbacks intercept tool calls before and after execution:

```python
def before_tool_callback(callback_context: CallbackContext) -> Optional[Any]:
    """
    Executed before a tool is called.
    Can modify the tool inputs or handle the tool call directly.
    """
    # Access tool information
    tool_name = callback_context.tool_name
    tool_args = callback_context.tool_args
    
    # Log the tool call
    print(f"Executing tool: {tool_name}")
    print(f"Arguments: {tool_args}")
    
    # You could modify the arguments here if needed
    
    return None  # Return None to continue with normal tool execution


def after_tool_callback(callback_context: CallbackContext) -> Optional[Any]:
    """
    Executed after a tool completes execution.
    Can modify the tool's result or create a completely new result.
    """
    # Access tool information and result
    tool_name = callback_context.tool_name
    tool_result = callback_context.tool_result
    
    # Log the tool result
    print(f"Tool {tool_name} completed")
    print(f"Result: {tool_result}")
    
    # You could modify the result here if needed
    
    return None  # Return None to use the original tool result
```

### Use Cases for Callbacks

Callbacks enable many powerful capabilities in ADK:

1. **Logging and Monitoring**:
   - Track agent usage and performance
   - Measure response times
   - Log all agent interactions for audit purposes

2. **Dynamic Control**:
   - Override agent behavior based on business rules
   - Implement fallback strategies
   - Apply security and validation checks

3. **State Management**:
   - Initialize or update state before processing
   - Clean up temporary state after processing
   - Synchronize state with external systems

4. **Response Modification**:
   - Add standard headers or footers to responses
   - Filter or redact sensitive information
   - Format responses to match specific requirements

5. **Integration**:
   - Connect with analytics platforms
   - Trigger notifications or alerts
   - Synchronize with external services

## Best Practices for Callbacks

1. **Keep Callbacks Focused**: Each callback should have a single responsibility
2. **Efficient Processing**: Callbacks are executed with every request, so keep them efficient
3. **Error Handling**: Implement robust error handling in callbacks to prevent failures
4. **State Management**: Be careful when modifying state to avoid race conditions
5. **Documentation**: Document the purpose and behavior of each callback
6. **Testing**: Thoroughly test callbacks to ensure they don't have unintended side effects

## Next Steps

After understanding callbacks, you might want to explore:
- Building workflow agents (see folders 10-sequential-agent, 11-parallel-agent, and 12-loop-agent)

For more information, visit the ADK Callbacks documentation. (https://google.github.io/adk-docs/callbacks/)