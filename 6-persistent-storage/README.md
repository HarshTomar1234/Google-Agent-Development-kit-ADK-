# Persistent Storage in ADK

## ADK Concept: Persistent Storage

In the Google Agent Development Kit (ADK), persistent storage extends the concept of sessions and state management by allowing agent data to persist beyond the lifetime of the application. This is crucial for creating agents that maintain context and user data across multiple sessions, application restarts, or even server deployments.

### Why Persistent Storage Matters

According to the [ADK documentation](https://google.github.io/adk-docs/sessions), persistent storage provides several key benefits:

1. **Long-term Memory**: Agents can remember information across multiple conversations
2. **User Continuity**: Users can pick up where they left off, even after extended periods
3. **Data Resilience**: Information is not lost when the application restarts or crashes
4. **Scale**: User data can be distributed across multiple instances of an application


### Storage Options in ADK

ADK offers several options for persistent storage:

1. **DatabaseSessionService**: Store sessions in a SQL database
   - SQLite (for development/testing)
   - PostgreSQL (for production)
   - MySQL/MariaDB
   
2. **FileSessionService**: Store sessions as files on disk
   - Simpler than database storage
   - Works well for smaller applications
   
3. **Custom Implementations**: Create your own session service
   - Connect to NoSQL databases
   - Integrate with cloud storage
   - Use in-memory caches with persistence

## Implementation Details

This folder contains a memory agent implementation that demonstrates how to use persistent storage with ADK.

### Project Structure
```
6-persistent-storage/
├── memory_agent/
│   ├── __init__.py
│   └── agent.py
├── agent_data.db
├── main.py
└── utils.py
```

### Agent Description

The `memory_agent` is an agent that:
- Helps users manage their reminders
- Remembers user information and reminders across application restarts
- Uses a SQLite database for persistent storage
- Demonstrates CRUD operations (Create, Read, Update, Delete) on persistent data

### Code Explanation

The implementation consists of several key components:

#### 1. Database Session Service Setup (main.py)

```python
from google.adk.sessions import DatabaseSessionService

# Using SQLite database for persistent storage
db_url = "sqlite:///./agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```

The `DatabaseSessionService` connects to a SQLite database file (`agent_data.db`) using SQLAlchemy's connection string format.

#### 2. Session Management (main.py)

```python
# Check for existing sessions for this user
existing_sessions = session_service.list_sessions(
    app_name=APP_NAME,
    user_id=USER_ID,
)

# If there's an existing session, use it, otherwise create a new one
if existing_sessions and len(existing_sessions.sessions) > 0:
    # Use the most recent session
    SESSION_ID = existing_sessions.sessions[0].id
    print(f"Continuing existing session: {SESSION_ID}")
else:
    # Create a new session with initial state
    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )
    SESSION_ID = new_session.id
    print(f"Created new session: {SESSION_ID}")
```

This code checks for existing sessions for a user, and either continues with the most recent one or creates a new session with initial state.

#### 3. Agent with State-Aware Tools (memory_agent/agent.py)

The agent includes several tools that interact with the persistent state:

```python
def add_reminder(reminder: str, tool_context: ToolContext) -> dict:
    """Add a new reminder to the user's reminder list."""
    # Get current reminders from state
    reminders = tool_context.state.get("reminders", [])
    
    # Add the new reminder
    reminders.append(reminder)
    
    # Update state with the new list of reminders
    tool_context.state["reminders"] = reminders
    
    return {
        "action": "add_reminder",
        "reminder": reminder,
        "message": f"Added reminder: {reminder}",
    }
```

Each tool follows a similar pattern:
1. Read the current state from `tool_context.state`
2. Perform operations on the data
3. Write the updated data back to `tool_context.state`
4. Return a structured response

### Database Schema and Operation

The `DatabaseSessionService` automatically creates the necessary tables in the database:

- **sessions**: Stores session metadata (ID, app name, user ID, timestamps)
- **session_states**: Stores the serialized state data for each session
- **messages**: Stores conversation history for each session

When the agent modifies the state through tools, the changes are automatically persisted to the database by the session service.

### Continuity Across Restarts

A key feature of this implementation is that it maintains continuity across application restarts:

1. When the application starts, it checks for existing sessions
2. If found, it loads the most recent session's state
3. The agent has access to all previously stored reminders and user information
4. New interactions continue to update the same persistent storage

### Sample Interaction

First Run:
```
Created new session: 3f7e8d9a-1c2b-4b5c-9d8e-7f6a5b4c3d2a

You: Hi, my name is Alice
Agent: Hello Alice! It's nice to meet you. I'm your reminder assistant. I can help you add, view, update, or delete reminders. How can I assist you today?

You: Add a reminder to call mom tomorrow
Agent: I've added a reminder for you: "call mom tomorrow". Is there anything else you'd like me to remind you about, Alice?

You: exit
Ending conversation. Your data has been saved to the database.
```

Second Run (after restarting the application):
```
Continuing existing session: 3f7e8d9a-1c2b-4b5c-9d8e-7f6a5b4c3d2a

You: Hi again
Agent: Welcome back, Alice! I still have your reminder to "call mom tomorrow" saved. Would you like to add more reminders or make any changes to your existing one?
```

## Setting Up a Production Database

While the example uses SQLite, for production environments, you would typically use PostgreSQL or another robust database system:

```python
# PostgreSQL connection
db_url = "postgresql://username:password@hostname:port/database"
session_service = DatabaseSessionService(db_url=db_url)
```

The `DatabaseSessionService` uses SQLAlchemy, which supports multiple database backends without changing your application code.

## Best Practices for Persistent Storage

1. **Database Selection**: Choose the right database for your needs
   - SQLite: Great for development and small applications
   - PostgreSQL/MySQL: Better for production applications
   - Cloud-managed databases: For scalability and managed operations

2. **Data Modeling**:
   - Keep state data structures simple and serializable
   - Use consistent key names across your application
   - Document the expected state structure

3. **Error Handling**:
   - Implement proper error handling for database operations
   - Add retry mechanisms for transient database errors
   - Provide fallback behaviors when the database is unavailable

4. **Security Considerations**:
   - Secure database credentials
   - Limit permissions for database users
   - Consider encryption for sensitive data
   - Implement proper user authentication

## Next Steps

After understanding persistent storage, you might want to explore:
- Building multi-agent systems (see folder 7-multi-agent)
- Creating stateful multi-agent applications (see folder 8-stateful-multi-agent)
- Working with callbacks (see folder 9-callbacks)

For more information, visit the [ADK Sessions Persistence documentation](https://google.github.io/adk-docs/sessions/) 