# Sequential Agents in ADK

## ADK Concept: Sequential Agents

In the Google Agent Development Kit (ADK), sequential agents are workflow agents that execute a series of sub-agents in a predefined order. This allows for creating structured workflows where each agent's output becomes the input for the next agent in the sequence.

### What are Sequential Agents?

A sequential agent orchestrates a linear workflow of specialized agents, where each agent processes information and passes its results to the next agent in the sequence. This pattern is particularly useful for:

- Breaking complex tasks into discrete sequential steps
- Creating clear, structured information processing pipelines
- Ensuring that each step in a process is completed before the next begins
- Implementing multi-stage processing where each stage builds on the previous one

Sequential agents are one of several workflow agent types in ADK, specifically designed for processes that need to follow a strict order of operations.

### How Sequential Agents Work

The `SequentialAgent` class in ADK:

1. Takes a list of sub-agents in the desired execution order
2. When invoked, runs each sub-agent in sequence
3. Passes the output of each agent as input to the next agent
4. Returns the final output from the last agent in the sequence

Sub-agents in the sequence can be any valid ADK agent, including LLM agents, other workflow agents, or custom agents.

[Sequential Agents](../google_adk_images\sequential_agents.png)

## Implementation Details

This folder contains examples of sequential agent implementations in ADK.

### Project Structure
```
10-sequential-agent/
├── lead_qualification_agent/
│   ├── agent.py
│   ├── __init__.py
│   └── sub_agents/
│       ├── recommender.py
│       ├── scorer.py
│       └── validator.py
└── support_ticket_agent/
    ├── agent.py
    ├── __init__.py
    └── sub_agents/
        ├── categorizer.py
        ├── prioritizer.py
        └── resolver.py
```

### Example: Lead Qualification Pipeline

The lead qualification example demonstrates a sequential workflow for processing sales leads:

```python
from google.adk.agents import SequentialAgent

from .sub_agents.recommender import action_recommender_agent
from .sub_agents.scorer import lead_scorer_agent
from .sub_agents.validator import lead_validator_agent

# Create the sequential agent with three sub-agents
root_agent = SequentialAgent(
    name="LeadQualificationPipeline",
    sub_agents=[lead_validator_agent, lead_scorer_agent, action_recommender_agent],
    description="A pipeline that validates, scores, and recommends actions for sales leads",
)
```

This sequential agent implements a three-step pipeline:

1. **Lead Validator**: Checks if the lead information is complete and valid
2. **Lead Scorer**: Analyzes the lead information and assigns a quality score
3. **Action Recommender**: Recommends next actions based on the lead score

### Example: Support Ticket Processing

The support ticket example demonstrates a sequential workflow for handling customer support tickets:

```python
from google.adk.agents import SequentialAgent

from .sub_agents.categorizer import ticket_categorizer_agent
from .sub_agents.prioritizer import ticket_prioritizer_agent
from .sub_agents.resolver import ticket_resolver_agent

# Create the sequential agent with three sub-agents
root_agent = SequentialAgent(
    name="SupportTicketPipeline",
    sub_agents=[ticket_categorizer_agent, ticket_prioritizer_agent, ticket_resolver_agent],
    description="A pipeline that categorizes, prioritizes, and resolves customer support tickets",
)
```

This sequential agent implements a three-step pipeline:

1. **Ticket Categorizer**: Determines the category of the support issue
2. **Ticket Prioritizer**: Assigns a priority level based on the issue category and details
3. **Ticket Resolver**: Generates a resolution approach based on the category and priority

### Workflow and Execution

When a sequential agent processes a user request, it follows this flow:

1. The user sends a request to the sequential agent
2. The sequential agent passes the request to the first sub-agent
3. The first sub-agent processes the request and returns a response
4. The sequential agent takes that response and passes it to the second sub-agent
5. This process continues through all sub-agents in the defined order
6. The response from the final sub-agent becomes the sequential agent's response

### Data Flow Between Sub-agents

Information flows through the pipeline in these ways:

- **State**: All agents can read from and write to the shared session state
- **Message Content**: Each agent receives the output from the previous agent
- **Additional Context**: Agents can add information for subsequent agents in their responses

### Benefits of Sequential Agents

1. **Clear Process Definition**: Explicit ordering creates a clear, predictable process
2. **Modularity**: Each step can be developed, tested, and maintained independently
3. **Reusability**: Sub-agents can be reused in different sequential workflows
4. **Specialization**: Each agent can be optimized for its specific task
5. **Traceability**: The sequence makes it easy to track how information is processed
6. **Maintainability**: Changes to one step minimally impact others when interfaces are preserved

## Best Practices for Sequential Agents

1. **Clear Step Boundaries**: Define clear input and output expectations for each step
2. **Sub-agent Specificity**: Make each sub-agent highly focused on a single task
3. **Appropriate Granularity**: Choose the right level of granularity for your steps
4. **State Management**: Use session state to share information across steps when needed
5. **Error Handling**: Implement proper error handling at each step
6. **Testability**: Design sub-agents to be independently testable
7. **Documentation**: Document the purpose and expectations of each step

## Sample Interaction

Here's an example interaction with a lead qualification sequential agent:

```
User: I have a new lead: John Smith, CTO at TechCorp, interested in our enterprise product. Email: john@techcorp.com, Phone: 555-123-4567

Agent: 

[Lead Validation]
✅ Lead information is valid and complete.
- Name: John Smith
- Position: CTO
- Company: TechCorp
- Interest: Enterprise product
- Contact: Email and phone provided

[Lead Scoring]
Lead Score: 85/100 (High Value)
- C-level executive (+30)
- Enterprise interest (+25)
- Complete contact info (+15)
- Known company (+15)

[Action Recommendation]
Recommended Actions:
1. HIGH PRIORITY: Schedule a discovery call within 24 hours
2. Assign to an enterprise sales representative
3. Prepare a customized enterprise product demo
4. Research TechCorp's current technology stack
5. Send personalized follow-up email with case studies

This is a high-value lead that should be prioritized for immediate follow-up by your enterprise sales team.
```

## Comparison with Other Workflow Agents

Sequential agents are one of several workflow agent types in ADK:

- **Sequential Agent**: Executes sub-agents in a predefined order (A → B → C)
- **Parallel Agent**: Executes sub-agents simultaneously (A+B+C)
- **Loop Agent**: Executes the same sub-agent(s) repeatedly until a condition is met

Choose the appropriate workflow agent based on your specific requirements:

- Use **Sequential Agent** when steps must follow a specific order
- Use **Parallel Agent** when steps can be executed independently
- Use **Loop Agent** when steps need to be repeated until a condition is satisfied

## Next Steps

After understanding sequential agents, you might want to explore:
- Parallel agents (see folder 11-parallel-agent)
- Loop agents (see folder 12-loop-agent)
- Combining different workflow agents for complex applications

For more information, visit the ADK Workflow Agents documentation. (https://google.github.io/adk-docs/agents/workflow-agents/)
