# Structured Outputs Agent Implementation

## ADK Concept: Structured Outputs

In the Google Agent Development Kit (ADK), structured outputs allow agents to return data in specific, well-defined formats rather than just free-form text. This feature is particularly useful for creating agents that need to provide consistent, parsable responses that can be easily integrated with other systems.

### What are Structured Outputs in ADK?

According to the [official ADK documentation](https://google.github.io/adk-docs/tools/), structured outputs provide a way to constrain an agent's responses to specific formats. This ensures that the agent follows predefined schemas when responding, making it easier to integrate with applications that expect data in particular structures.

Structured outputs rely on Python's [Pydantic](https://docs.pydantic.dev/latest/) library, which provides powerful data validation and settings management using Python type annotations.

### Key Benefits of Structured Outputs

1. **Consistent Response Format**: Ensures responses follow a predefined structure
2. **Type Safety**: Validates that fields contain the expected data types
3. **Automatic Validation**: Pydantic validates that the output matches the schema
4. **Application Integration**: Makes it easy to connect agents to downstream systems
5. **Custom Output Processing**: Enables specialized handling of different output types
6. **Documentation**: Self-documenting through type annotations

## Implementation Details

This folder contains an email generator agent implementation that demonstrates how to use structured outputs in ADK.

### Project Structure
```
4-structured-outputs/
└── email_generator_agent/
    ├── __init__.py
    ├── agent.py
    └── README.md
```

### Agent Description

The `email_generator_agent` is an agent that:
- Generates professional email drafts based on user inputs
- Returns the email in a structured format with distinct subject and body fields
- Uses Gemini 2.0 Flash model for generating content
- Demonstrates how to define and use structured output schemas

### Code Explanation

The agent is created with a structured output definition:

```python
from google.adk.agents import Agent
from pydantic import BaseModel, Field

# Define the structured output schema
class EmailOutput(BaseModel):
    subject: str = Field(description="The subject line of the email")
    body: str = Field(description="The body content of the email")

# Create the agent with structured output
root_agent = Agent(
    name="email_generator_agent",
    model="gemini-2.0-flash",
    description="Agent that generates professional email drafts",
    instruction="""
    You are an expert email writer that helps users draft professional emails.
    Create a well-structured email based on the user's request.
    Structure your response with a clear subject line and appropriate email body.
    Use a professional tone and appropriate greetings and sign-offs.
    """,
    output_schema=EmailOutput
)
```

Key implementation details:

1. **Schema Definition**: We create a Pydantic model (`EmailOutput`) that defines the structure of the output
2. **Field Descriptions**: Each field has a description to guide the agent
3. **Schema Application**: The model is passed to the agent's `output_schema` parameter
4. **Agent Instructions**: The agent is instructed to create well-structured emails

### How Structured Outputs Work

When an agent is configured with an output schema:

1. The agent processes the user's input and generates a response
2. ADK uses the output schema to guide the LLM to format its response correctly
3. The output is validated against the schema to ensure it matches the expected structure
4. If successful, the output is returned as a Pydantic model instance
5. If validation fails, ADK will attempt to fix the output or return an error

### Advanced Structured Output Features

ADK's structured outputs support various advanced features:

#### Nested Models

You can create complex nested output structures:

```python
class ContactInfo(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class CustomerRecord(BaseModel):
    customer_id: str
    primary_contact: ContactInfo
    secondary_contacts: List[ContactInfo] = []
```

#### Enumerations

For fields with a limited set of allowed values:

```python
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(BaseModel):
    title: str
    description: str
    priority: Priority
```

#### Field Validation

For ensuring values meet specific criteria:

```python
class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    age: int = Field(ge=18)  # greater than or equal to 18
```

### Sample Interaction

```
User: I need to write an email to my team about the upcoming project deadline.

Agent: Here's a draft email for your team regarding the upcoming project deadline:

Subject: Important Update: Project Milestone Deadline - Friday, April 15

Body:
Hi Team,

I hope this email finds you well. I wanted to touch base regarding our upcoming project milestone deadline set for Friday, April 15.

As we approach this important date, please ensure all deliverables are finalized and submitted by 5:00 PM. If you anticipate any difficulties meeting this deadline, kindly let me know as soon as possible so we can discuss potential solutions.

I've scheduled a quick check-in meeting for Wednesday at 2:00 PM to address any outstanding questions or concerns.

Thank you for your continued dedication to this project.

Best regards,
[Your Name]
```

## Best Practices for Structured Outputs

1. **Keep Schemas Simple**: Start with simpler schemas and add complexity as needed
2. **Provide Clear Descriptions**: Use detailed field descriptions to guide the model
3. **Use Appropriate Types**: Choose the right data types for each field
4. **Handle Optional Fields**: Clearly mark which fields are required vs. optional
5. **Test Validation**: Verify that your schemas correctly validate different inputs
6. **Consider User Needs**: Design schemas based on how the data will be used

## Integration with Applications

Structured outputs make it easy to integrate agent responses with other applications:

```python
from my_agent import root_agent, EmailOutput

def send_email(email_data: EmailOutput):
    # Send the email using the subject and body from the structured output
    email_service.send(
        subject=email_data.subject,
        body=email_data.body,
        to="recipient@example.com"
    )

# Use the agent to generate an email and send it
response = root_agent.generate_response("Draft an email about the upcoming meeting")
send_email(response.output)
```

## Next Steps

After understanding structured outputs, you might want to explore:
- Creating more complex schemas for specialized applications
- Combining structured outputs with tools
- Using different LLM models with structured outputs
- Implementing multi-agent systems with structured communication

For more information, visit the [ADK  documentation](https://google.github.io/adk-docs/). 