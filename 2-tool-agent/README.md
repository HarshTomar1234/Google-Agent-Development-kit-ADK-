# Tool Agent Implementation

## ADK Concept: Tools

In the Google Agent Development Kit (ADK), tools are functions that agents can use to interact with external systems, APIs, or perform specialized tasks that the language model itself cannot do. Tools extend the capabilities of agents beyond simple conversation.

### What are Tools in ADK?

According to the [official ADK documentation](https://google.github.io/adk-docs/tools/), a **Tool** represents a specific capability provided to an AI agent, enabling it to perform actions and interact with the world beyond its core text generation and reasoning abilities. What distinguishes capable agents from basic language models is often their effective use of tools.

Technically, a tool is typically a modular code component—**like a Python function**, a class method, or even another specialized agent—designed to execute a distinct, predefined task. These tasks often involve interacting with external systems or data.

ADK offers several types of tools:

1. **Function Tools**: Custom Python functions that you create for specific tasks
2. **Built-in Tools**: Pre-configured tools provided by ADK (like Google Search)
3. **Third-party Tools**: Integration with tools from popular libraries (LangChain, CrewAI)
4. **Agent-as-a-Tool**: Using another agent as a tool
5. **Long Running Function Tool**: Tools that perform asynchronous operations or take time to complete

## Implementation Details

This folder contains a tool agent implementation that demonstrates how to equip an agent with custom tools.

### Project Structure
```
2-tool-agent/
└── tool_agent/
    ├── __init__.py
    ├── agent.py
    └── result_imgs/
```

### Agent Description

The `tool_agent` is an agent that:
- Has access to custom and built-in tools
- Can provide simulated weather forecasts using a custom tool
- Can search the web for information (built-in tool, currently commented out)
- Uses the Gemini 2.0 Flash model for generating responses

### Code Explanation

The agent is created with access to tools:

```python
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import FunctionTool

def weather_forecast(location: str, days: int = 3) -> str:
    """
    Get a simulated weather forecast for a location.
    
    Args:
        location: The city or location to get weather for
        days: Number of days for the forecast (default: 3)
        
    Returns:
        A simulated weather forecast as a string
    """
    # Function implementation details omitted for brevity
    # The function returns a simulated weather forecast

root_agent = Agent(
    name = "tool_agent",
    model = "gemini-2.0-flash",
    description = "An agent that can search the web",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search: Search the web for information
    - weather_forecast: Get a simulated weather forecast for a location
    """,
    # tools =[google_search],  # Built-in tool (commented out)
    tools = [weather_forecast],  # Custom function tool
)
```

Key tool implementation details:

1. **Function Definition**: We create a Python function `weather_forecast` with typed parameters and a detailed docstring
2. **Tool Integration**: We pass the function directly to the agent's `tools` parameter
3. **Tool Documentation**: The docstring is crucial - it tells the agent what the tool does and how to use it
4. **Agent Instruction**: We explicitly mention available tools in the agent's instructions

### How Tools Work in ADK

When an agent is equipped with tools, the process typically follows these steps:

1. **Reasoning**: The agent analyzes the user's request and decides whether a tool is needed
2. **Selection**: If a tool is needed, the agent selects the appropriate tool based on its description
3. **Invocation**: The agent generates the required arguments and calls the tool
4. **Processing**: The tool executes with the provided arguments
5. **Integration**: The agent incorporates the tool's output into its ongoing reasoning

### Best Practices for Tool Design

Creating effective tools for ADK agents involves several best practices:

1. **Clear Function Naming**: Use descriptive verb-noun based names (e.g., `weather_forecast` not just `weather`)
2. **Detailed Docstrings**: Write comprehensive documentation explaining purpose, parameters, and return values
3. **Type Hints**: Use Python type hints for all parameters to help both ADK and the LLM understand what's expected
4. **Structured Returns**: Return dictionaries with clear status indicators (e.g., `{"status": "success", "data": result}`)
5. **Error Handling**: Implement comprehensive error handling within your tools
6. **Single Responsibility**: Each tool should do one well-defined task

### Sample Interaction

```
User: What's the weather like in New York?
Agent: I'll check the weather forecast for New York for you.

According to the forecast for New York:
- Day 1 (Today): 72°F, Partly Cloudy
- Day 2 (Tomorrow): 75°F, Sunny
- Day 3: 68°F, Light Rain

Would you like to know the weather for any other location or for more days?
```

## Tool Context and Advanced Features

For more advanced scenarios, ADK allows tools to access additional contextual information using the `ToolContext` parameter:

```python
from google.adk.tools.tool_context import ToolContext

def remember_preference(category: str, value: str, tool_context: ToolContext) -> dict:
    """Stores a user preference in the session state."""
    # Access session state
    preferences = tool_context.state.get("user:preferences", {})
    preferences[category] = value
    tool_context.state["user:preferences"] = preferences
    
    return {"status": "success", "message": f"Preference saved: {category}={value}"}
```

The `ToolContext` provides:
- **State Management**: Access to session state for persistent data storage
- **Action Control**: Ability to influence the agent's subsequent behavior
- **Integration**: Access to services like artifacts and memory

## Next Steps

After understanding how to use tools with agents, you might want to explore:
- Working with different LLM models (see folder 3-litellm-agent)
- Creating structured outputs (see folder 4-structured-outputs)
- Building multi-agent systems with specialized capabilities

For more information, visit the [ADK Tools documentation](https://google.github.io/adk-docs/tools/). 