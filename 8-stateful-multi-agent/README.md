# Stateful Multi-Agent Systems in ADK

## ADK Concept: Stateful Multi-Agent Systems

In the Google Agent Development Kit (ADK), stateful multi-agent systems combine the concepts of multi-agent architecture with session state management. This powerful approach enables complex agent applications that not only delegate tasks to specialized agents but also remember information across interactions and share context between agents.

### What are Stateful Multi-Agent Systems?

A stateful multi-agent system consists of multiple specialized agents working together, all sharing access to a common session state. This shared state enables agents to:

- Maintain context across a conversation
- Share information between agents
- Build upon each other's knowledge
- Remember user preferences and previous interactions
- Create more cohesive and personalized experiences

Stateful multi-agent systems are particularly useful for applications that require both specialized expertise (multi-agent) and memory of past interactions (state management).

### Key Components

1. **Manager Agent**: Coordinates sub-agents and manages the conversation flow
2. **Specialized Sub-Agents**: Handle specific domains or tasks
3. **Shared Session State**: Central repository for information accessible by all agents
4. **State Access Patterns**: Defined ways for agents to read from and write to state
5. **Session Service**: Infrastructure for persisting and retrieving state

## Implementation Details

This folder contains a customer service agent implementation that demonstrates how to build a stateful multi-agent system in ADK.

### Project Structure
```
8-stateful-multi-agent/
├── customer_service_agent/
│   ├── agent.py
│   ├── __init__.py
│   └── sub_agents/
│       ├── course_support_agent/
│       ├── order_agent/
│       ├── policy_agent/
│       └── sales_agent/
├── main.py
└── utils.py
```

### System Description

The customer service agent system consists of:

1. **Manager Agent**: Main customer service agent that routes requests to specialized agents
2. **Policy Agent**: Handles questions about community guidelines and refund policies
3. **Sales Agent**: Manages course purchases and sales inquiries
4. **Course Support Agent**: Provides assistance with course content for purchased courses
5. **Order Agent**: Manages purchase history and processes refunds

### Code Explanation

#### 1. Manager Agent Definition (customer_service_agent/agent.py)

```python
from google.adk.agents import Agent
from .sub_agents.course_support_agent.agent import course_support_agent
from .sub_agents.order_agent.agent import order_agent
from .sub_agents.policy_agent.agent import policy_agent
from .sub_agents.sales_agent.agent import sales_agent

customer_service_agent = Agent(
    name="customer_service",
    model="gemini-2.0-flash",
    description="Customer service agent for AI Developer Accelerator community",
    instruction="""
    You are the primary customer service agent for the AI Developer Accelerator community.
    Your role is to help users with their questions and direct them to the appropriate specialized agent.

    **User Information:**
    <user_info>
    Name: {user_name}
    </user_info>

    **Purchase Information:**
    <purchase_info>
    Purchased Courses: {purchased_courses}
    </purchase_info>

    **Interaction History:**
    <interaction_history>
    {interaction_history}
    </interaction_history>
    """,
    sub_agents=[policy_agent, sales_agent, course_support_agent, order_agent],
)
```

#### 2. State Management (main.py)

```python
# Define Initial State
initial_state = {
    "user_name": "Ash Ketchum",
    "purchased_courses": [],
    "interaction_history": [],
}

# Create a new session with initial state
new_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    state=initial_state,
)
```

### Shared State Access

All agents in the system have access to the same session state, which includes:

1. **user_name**: The name of the current user
2. **purchased_courses**: List of courses the user has purchased
3. **interaction_history**: Record of previous interactions

The state is updated in several ways:

- When the user purchases a course (via the sales agent)
- When interaction history is updated (via the main application)
- When refunds are processed (via the order agent)

### Multi-Agent Workflow with State

The customer service workflow demonstrates how state enhances multi-agent systems:

1. **Context-Aware Routing**:
   - The manager agent routes requests based on both the content of the request and the user's state
   - For example, course support questions are only routed to the course support agent if the user has purchased the relevant course

2. **Personalized Interactions**:
   - Each agent tailors its responses based on the user's information in the state
   - Greetings include the user's name
   - Recommendations consider purchase history

3. **Progressive Conversation**:
   - The system builds upon previous interactions stored in state
   - Agents can reference previous parts of the conversation

4. **State Updates**:
   - Agents can modify the state when important events occur
   - For example, the sales agent updates the purchased_courses list when a user buys a course

### Benefits of Stateful Multi-Agent Systems

1. **Cohesive Experience**: Creates a seamless experience despite multiple specialized agents
2. **Information Sharing**: Prevents redundant questions as information is shared across agents
3. **Context Preservation**: Maintains conversation context even when switching between agents
4. **Personalization**: Enables tailored responses based on user history and preferences
5. **Complex Workflows**: Supports multi-step processes that span different functional areas

## Best Practices for Stateful Multi-Agent Systems

1. **State Design**: Carefully plan what information should be stored in state
2. **Access Patterns**: Define clear patterns for how agents read from and write to state
3. **State Validation**: Implement validation to ensure state remains consistent
4. **Privacy Considerations**: Be mindful of what user information is stored
5. **Default Values**: Always provide defaults when accessing state to handle missing data
6. **Documentation**: Document the expected state structure for all developers

## Sample Interaction

```
You: Hello! I'm interested in your AI Marketing Platform course.

Agent: Hi Ash! I'd be happy to help you with information about our AI Marketing Platform course. This course covers advanced AI techniques for marketing automation, content generation, and analytics.

The course is priced at $149 and comes with a 30-day money-back guarantee. Would you like to purchase it or do you have specific questions about the course content?

You: I'll buy it. Here's my credit card info.

Agent: Great choice, Ash! I'll direct you to our Sales Agent to complete your purchase.

[Sales Agent]: Thank you for your purchase of the AI Marketing Platform course! Your transaction has been processed successfully. The course has been added to your account, and you can access it immediately.

Your purchase comes with our 30-day money-back guarantee. If you have any questions about the course content, feel free to ask our Course Support Agent.

Would you like me to provide you with the course login details now?

You: Yes, please.

Agent: Here are your login details for the AI Marketing Platform course:

- URL: learn.aideveloper.accelerator/courses/ai-marketing
- Username: ash.ketchum
- Password: Your account password remains the same

You can access all course materials, including videos, assignments, and resources through this portal. The course is self-paced, so you can progress at your convenience.

If you have any specific questions about the course content or assignments, please let me know, and I'll be happy to help!

Is there anything else you'd like assistance with regarding your new course?
```

## Next Steps

After understanding stateful multi-agent systems, you might want to explore:
- Working with agent callbacks (see folder 9-callbacks)
- Building more complex workflow agents (see folders 10-sequential-agent, 11-parallel-agent, and 12-loop-agent)

For more information, visit the ADK documentation and Sessions documentation. (https://google.github.io/adk-docs/)