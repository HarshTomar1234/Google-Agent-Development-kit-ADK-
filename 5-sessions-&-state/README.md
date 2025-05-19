# Sessions & State Management in ADK

## ADK Concept: Sessions and State

In the Google Agent Development Kit (ADK), sessions and state management provide mechanisms for agents to maintain context and remember information across multiple interactions with users. This is crucial for creating agents that can carry on coherent, stateful conversations.

### What are Sessions in ADK?

According to the [official ADK documentation](https://google.github.io/adk-docs/sessions/), a **Session** represents an ongoing conversation between a user and an agent. Sessions allow agents to:

- Remember previous messages in a conversation
- Store and retrieve user-specific information
- Track the progression of multi-turn interactions
- Maintain context for more natural conversations

[Sessions Lifecycle](google_adk_images\sessions_lifecycle.png)

Sessions in ADK consist of:
1. **Session Metadata**: Identifiers for the app, user, and specific conversation
2. **Conversation History**: A record of messages exchanged during the session
3. **Session State**: A key-value store for persistent data

### State Management

State management is a critical aspect of building intelligent agents. In ADK, state allows agents to:

- Remember user preferences across conversation turns
- Track the progress of multi-step processes
- Store intermediate results for complex tasks
- Maintain user-specific customizations

The state is stored as a dictionary in the session, with keys and values that can be accessed and modified by the agent during a conversation.

## Implementation Details

This folder contains a pizza ordering agent implementation that demonstrates how to use sessions and state management in ADK.

### Project Structure
```
5-sessions-&-state/
├── basic_stateful_sessions.py
├── pizza_ordering_agent/
│   ├── __init__.py
│   └── agent.py
└── result_imgs/
```

### Agent Description

The `pizza_ordering_agent` is an agent that:
- Helps users order pizzas
- Remembers user preferences like size and toppings across conversation turns
- Uses session state to build up the pizza order incrementally
- Demonstrates how to create and use stateful sessions in ADK

### Code Explanation

The implementation consists of two main parts:

#### 1. Agent Definition (pizza_ordering_agent/agent.py)

```python
import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Define the model using LiteLLM
model = LiteLlm(
    model="openai/gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Create the agent
pizza_ordering_agent = LlmAgent(
    model=model,
    name="pizza_ordering_agent",
    description="Pizza ordering agent",
    instruction=(
        "You are a helpful assistant for ordering pizzas. "
        "Remember the user's preferences such as size and toppings."
    ),
    output_key="last_response"
)
```

#### 2. Session Management (basic_stateful_sessions.py)

```python
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pizza_ordering_agent.agent import pizza_ordering_agent

# Create a new session service to store state
session_service_stateful = InMemorySessionService()

# Define application and user identifiers
APP_NAME = "PizzaBot"
USER_ID = "user_pizza"
SESSION_ID = str(uuid.uuid4())

# Create a new session with an empty initial state
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state={}
)

# Initialize the runner with the agent and session service
runner = Runner(
    agent=pizza_ordering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

# Process user messages and update state
for user_input in user_messages:
    # Run the agent with the user message
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        # Process agent responses
```

Key implementation details:

1. **Session Service**: We use `InMemorySessionService` to create and manage sessions
2. **Session Creation**: A new session is created with unique identifiers and an empty initial state
3. **Runner Configuration**: The runner is initialized with the agent and session service
4. **Conversation Flow**: User messages are processed sequentially, with the agent having access to previous context
5. **State Access**: The agent can read from and write to the session state during the conversation

### Session Services in ADK

ADK provides several session service implementations:

1. **InMemorySessionService**: Stores sessions in memory (used in this example)
2. **FileSessionService**: Persists sessions to disk
3. **CustomSessionService**: Create your own implementation for specific needs (e.g., database storage)

### Working with Session State

Agents can interact with session state in several ways:

#### Reading from State

```python
def get_preference(category: str, tool_context: ToolContext) -> str:
    """Gets a stored user preference."""
    preferences = tool_context.state.get("preferences", {})
    return preferences.get(category, "Not set")
```

#### Writing to State

```python
def set_preference(category: str, value: str, tool_context: ToolContext) -> str:
    """Stores a user preference in the session state."""
    preferences = tool_context.state.get("preferences", {})
    preferences[category] = value
    tool_context.state["preferences"] = preferences
    return f"Preference saved: {category}={value}"
```

### Sample Interaction

The example demonstrates a conversation where the agent remembers pizza preferences:

```
User: I want to order a pizza.
Agent: I'd be happy to help you order a pizza! What size would you like?

User: Large size, please.
Agent: Great! A large pizza it is. What toppings would you like on your pizza?

User: Add pepperoni and mushrooms.
Agent: I've added pepperoni and mushrooms to your large pizza. Would you like any specific type of crust?

User: Crust should be stuffed.
Agent: Perfect! I've updated your order to a large stuffed crust pizza with pepperoni and mushrooms. Would you like to confirm your order or make any changes?

User: Confirm my order.
Agent: Your order has been confirmed! To summarize: You've ordered a large stuffed crust pizza with pepperoni and mushrooms. Thank you for your order!

==== Final Session State ====
pizza_size: Large
toppings: pepperoni, mushrooms
crust_type: stuffed
order_confirmed: True
```

## Best Practices for State Management

1. **Use Meaningful Keys**: Choose descriptive names for state keys
2. **Initialize State**: Always check if a key exists before accessing it
3. **Structure Data**: Use nested dictionaries for complex data
4. **Validate Inputs**: Verify data before storing it in state
5. **Clean Up**: Remove temporary data from state when no longer needed
6. **Error Handling**: Implement robust error handling for state operations

## Next Steps

After understanding sessions and state, you might want to explore:
- Implementing persistent storage (see folder 6-persistent-storage)
- Building multi-agent systems (see folder 7-multi-agent)
- Creating stateful multi-agent applications (see folder 8-stateful-multi-agent)

For more information, visit the [ADK Sessions documentation](https://google.github.io/adk-docs/sessions/). 