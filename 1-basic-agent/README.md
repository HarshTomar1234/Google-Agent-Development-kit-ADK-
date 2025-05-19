# Basic Agent Implementation

## ADK Concept: Basic Agents

In the Google Agent Development Kit (ADK), an agent is the fundamental building block for creating AI assistants. The ADK provides a flexible framework for developing and deploying AI agents that can perform various tasks and interact with users.

### What is an Agent in ADK?

According to the [official ADK documentation](https://google.github.io/adk-docs/agents/), an **Agent** is a self-contained execution unit designed to act autonomously to achieve specific goals. Agents can:

- Process natural language inputs from users
- Generate human-like responses
- Make decisions and take actions
- Use tools to interact with external systems
- Coordinate with other agents

The foundation for all agents in ADK is the `BaseAgent` class, but for most practical applications, you'll use one of three main implementations:

1. **LLM Agents** (`LlmAgent`, `Agent`) - Use Large Language Models to understand language, reason, and generate responses
2. **Workflow Agents** (Sequential, Parallel, Loop) - Control execution flow with predefined patterns
3. **Custom Agents** - Extend `BaseAgent` for highly specialized behaviors

![ADK Agent Types](./google_adk_images/agents.png)

## Implementation Details

This folder contains a simple greeting agent implementation that demonstrates the basics of creating an agent with ADK.

### Project Structure
```
1-basic-agent/
└── greeting_agent/
    ├── __init__.py
    └── agent.py
```

### Agent Description

The `greeting_agent` is a simple agent that:
- Greets the user and asks for their name
- Provides a motivational thought after greeting the user by name
- Uses the Gemini 2.0 Flash model for generating responses

### Code Explanation

The agent is created using the `Agent` class from the ADK framework:

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Agent for greeting with a motivational thought",
    instruction = """
    You are a helpful assistant that basically greets the user and provides a motivational thought.
    Ask for the user's name and greet them by name followed by a motivational thought.
    """
)
```

Key components explained:

- **name**: A unique identifier for the agent
- **model**: The underlying LLM model (Gemini 2.0 Flash in this case)
- **description**: A brief description of the agent's purpose - important for multi-agent systems where agents delegate tasks
- **instruction**: Detailed instructions that guide the agent's behavior - like a system prompt that defines what the agent does

### How to Use

1. Make sure you have ADK installed: `pip install google-adk`
2. Run the agent using: `adk run greeting_agent`
3. Interact with the agent in the console - it will ask for your name and provide a motivational thought

### Key ADK Concepts Illustrated

- **Basic Agent Configuration**: Setting up a simple LLM agent with instruction-based behavior
- **Using Gemini Models**: Leveraging Google's Gemini 2.0 Flash model for natural language understanding and generation
- **Agent Deployment**: Running an agent using the ADK CLI tools

### Sample Interaction

```
User: Hello!
Agent: Hi there! My name is Gemini. What's your name?
User: Alex
Agent: Nice to meet you, Alex! Here's a motivational thought for you today: "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle." - Steve Jobs

Is there anything specific I can help you with today?
```

## Next Steps

After understanding basic agents, you might want to explore:
- Adding tools to extend your agent's capabilities (see folder 2-tool-agent)
- Using different LLM models via LiteLLM (see folder 3-litellm-agent)
- Working with structured outputs (see folder 4-structured-outputs)

For more information, visit the [ADK documentation](https://google.github.io/adk-docs/). 
