# Multi-Agent Systems in ADK

## ADK Concept: Multi-Agent Architecture

In the Google Agent Development Kit (ADK), multi-agent architecture allows complex problems to be broken down into smaller, specialized components handled by individual agents. This approach enables more sophisticated applications by leveraging the strengths of different agents working together in a coordinated manner.

### What is a Multi-Agent System?

According to the [official ADK documentation](https://google.github.io/adk-docs/agents/), a multi-agent system consists of multiple independent agents that work together, often in a hierarchy, to solve complex tasks. Each agent has specific responsibilities and expertise, and they communicate with each other to achieve a common goal.


### Key Components of Multi-Agent Systems

1. **Manager Agent**: The orchestrator that coordinates sub-agents
   - Decides which sub-agent should handle a task
   - Routes information between sub-agents
   - Synthesizes responses from multiple agents

2. **Sub-Agents**: Specialized agents that handle specific tasks
   - Focus on a narrow domain or functionality
   - Can have their own tools and capabilities
   - Typically report back to the manager agent

3. **Communication**: Methods for agents to exchange information
   - Direct delegation from manager to sub-agents
   - Results passed back to the manager
   - Potential for peer-to-peer communication

## Implementation Details

This folder contains a meal planner multi-agent system that demonstrates how to create a hierarchical team of agents in ADK.

### Project Structure
```
7-multi-agent/
├── meal_planner/
│   ├── manager/
│   │   ├── agent.py
│   │   ├── __init__.py
│   │   └── sub_agents/
│   │       ├── user_profile/
│   │       ├── meal_plan_generator/
│   │       ├── recipe_suggester/
│   │       ├── shopping_list/
│   │       └── __init__.py
│   ├── main.py
│   ├── 7 days keto meal plan.txt
│   ├── shopping list for 3 days.txt
│   └── shopping list for 3 days_cold_diet.txt
└── manager/
```

### System Description

The meal planner multi-agent system consists of:

1. **Manager Agent**: Coordinates the overall meal planning process
2. **User Profile Agent**: Analyzes user requests to extract preferences and dietary requirements
3. **Meal Plan Generator Agent**: Creates meal plans based on user preferences
4. **Recipe Suggester Agent**: Suggests recipes for each meal in the plan
5. **Shopping List Agent**: Generates shopping lists based on the meal plan

### Code Explanation

#### 1. Manager Agent Definition (manager/agent.py)

```python
from google.adk.agents import Agent
from manager.sub_agents.user_profile.agent import user_profile_agent
from manager.sub_agents.meal_plan_generator.agent import meal_plan_generator_agent
from manager.sub_agents.recipe_suggester.agent import recipe_suggester_agent
from manager.sub_agents.shopping_list.agent import shopping_list_agent

root_agent = Agent(
    name="manager",
    model = "gemini-2.0-flash",
    description="Meal Planner manager agent",
    instruction="Coordinate the meal planning process by interacting with the respective agents.",
     sub_agents=[
        user_profile_agent,
        meal_plan_generator_agent,
        recipe_suggester_agent,
        shopping_list_agent
    ],
)
```

The manager agent is configured to:
- Use the Gemini 2.0 Flash model
- Coordinate between four specialized sub-agents
- Follow instructions to manage the meal planning workflow

#### 2. Application Setup (main.py)

```python
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from manager.agent import root_agent

# Initialize session service
session_service = InMemorySessionService()

APP_NAME = "MealPlannerBot"
USER_ID = "user_meal_planner"
SESSION_ID = str(uuid.uuid4())

# Create a new session
session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state={}
)

# Initialize the runner with the manager agent
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)

# Process user request
user_input = "Provide a shopping list for healthy, carb-free vegetarian meals for the next 3 days."
```

The main application:
- Sets up a session service to manage conversation state
- Creates a new session for the user
- Initializes a runner with the manager agent
- Processes a user request for a shopping list

### Multi-Agent Workflow

When a user requests a meal plan, the system follows this workflow:

1. **Request Analysis**:
   - The manager agent receives the user's request
   - It delegates to the user profile agent to analyze preferences
   - The user profile agent extracts key information (diet type, duration, restrictions)

2. **Plan Generation**:
   - The manager passes the user profile to the meal plan generator
   - The meal plan generator creates a structured meal plan

3. **Recipe Suggestion**:
   - The manager sends the meal plan to the recipe suggester
   - The recipe suggester adds specific recipes to each meal

4. **Shopping List Creation**:
   - The manager passes the detailed meal plan to the shopping list agent
   - The shopping list agent generates a consolidated shopping list

5. **Response Synthesis**:
   - The manager agent combines the outputs from all sub-agents
   - It presents a comprehensive response to the user

### Benefits of the Multi-Agent Approach

1. **Specialization**: Each agent focuses on a specific aspect of meal planning
2. **Modularity**: Agents can be developed and updated independently
3. **Flexibility**: New capabilities can be added by introducing new sub-agents
4. **Clarity**: The division of responsibilities makes the system easier to understand
5. **Performance**: Specialized agents can be optimized for their specific tasks

## Advanced Multi-Agent Patterns

ADK supports several advanced patterns for multi-agent systems:

### 1. Hierarchical Delegation

In this pattern (used in the meal planner example), a manager agent delegates tasks to specialized sub-agents:

```python
root_agent = Agent(
    name="manager",
    sub_agents=[agent1, agent2, agent3],
    # ...
)
```

The manager decides which sub-agent to call based on the user's request.

### 2. Parallel Processing

Multiple agents can work simultaneously on different aspects of a problem:

```python
from google.adk.agents.workflow import ParallelAgent

parallel_agent = ParallelAgent(
    name="parallel_processor",
    agents=[agent1, agent2, agent3],
    # ...
)
```

### 3. Sequential Processing

Agents can work in a predefined sequence, with each agent building on the output of the previous one:

```python
from google.adk.agents.workflow import SequentialAgent

sequential_agent = SequentialAgent(
    name="sequential_processor",
    agents=[agent1, agent2, agent3],
    # ...
)
```

## Best Practices for Multi-Agent Systems

1. **Clear Role Definition**: Each agent should have a well-defined role and purpose
2. **Effective Communication**: Ensure efficient information flow between agents
3. **Proper Coordination**: The manager agent needs clear instructions on delegation
4. **Error Handling**: Implement strategies for handling failures in individual agents
5. **State Management**: Consider how state is shared between agents
6. **Testing**: Test each agent individually and the system as a whole

## Sample Output

The meal planner system generates comprehensive outputs like:

```
Shopping List for 3 Days of Carb-Free Vegetarian Meals:

Produce:
- Spinach (2 bunches)
- Kale (1 bunch)
- Bell peppers (6, mixed colors)
- Zucchini (3)
- Cauliflower (1 head)
- Broccoli (1 head)
- Mushrooms (12 oz)
- Avocados (4)
- Tomatoes (4)
- Cucumber (2)
- Fresh herbs (basil, cilantro, parsley)
- Lemon (2)
- Lime (2)

Protein:
- Firm tofu (2 packages)
- Tempeh (1 package)
- Eggs (1 dozen)

Dairy and Alternatives:
- Greek yogurt (1 container)
- Feta cheese (4 oz)
- Mozzarella cheese (8 oz)
- Almond milk (1 quart, unsweetened)

Nuts and Seeds:
- Almonds (1 cup)
- Walnuts (1 cup)
- Chia seeds (1/4 cup)
- Flaxseeds (1/4 cup)

Oils and Condiments:
- Olive oil
- Coconut oil
- Apple cider vinegar
- Tamari or soy sauce (low sodium)
- Dijon mustard

Spices:
- Salt and pepper
- Garlic powder
- Onion powder
- Cumin
- Paprika
- Turmeric
- Chili flakes
```

## Next Steps

After understanding multi-agent systems, you might want to explore:
- Creating stateful multi-agent applications (see folder 8-stateful-multi-agent)
- Working with agent callbacks (see folder 9-callbacks)
- Building workflow agents (see folders 10-sequential-agent, 11-parallel-agent, and 12-loop-agent)

For more information, visit the [ADK Multi-Agent documentation](https://google.github.io/adk-docs/agents/multi-agents/#human-in-the-loop-pattern) 