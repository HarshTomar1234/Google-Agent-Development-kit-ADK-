# ADK Bot

<p align="center">
  <img src="https://google.github.io/adk-docs/assets/agent-development-kit.png" alt="Google Agent Development Kit" width="600">
</p>

A Python-based agent that helps shorten messages using Google's Agent Development Kit (ADK) and Vertex AI.

## Prerequisites

- Python 3.12+
- Poetry (Python package manager)
- Google Cloud account with Vertex AI API enabled
- Google Cloud CLI (`gcloud`) installed and authenticated
  - Follow the [official installation guide](https://cloud.google.com/sdk/docs/install) to install gcloud
  - After installation, run `gcloud init` and `gcloud auth login`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HarshTomar1234/Google-Agent-Development-kit-ADK-.git
cd adk-bot
```

2. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install project dependencies:
```bash
poetry install
```

4. Activate the virtual environment:
```bash
source $(poetry env info --path)/bin/activate
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=your-location  # e.g., us-central1
GOOGLE_CLOUD_STAGING_BUCKET=gs://your-bucket-name
```

2. Set up Google Cloud authentication:
```bash
gcloud auth login
gcloud config set project your-project-id
```

3. Enable required APIs:
```bash
gcloud services enable aiplatform.googleapis.com
```

## Usage

### Local Testing

1. Create a new session:
```bash
poetry run deploy-local --create_session
```

2. List all sessions:
```bash
poetry run deploy-local --list_sessions
```

3. Get details of a specific session:
```bash
poetry run deploy-local --get_session --session_id=your-session-id
```

4. Send a message to shorten:
```bash
poetry run deploy-local --send --session_id=your-session-id --message="Shorten this message: Hello, how are you doing today?"
```

### Remote Deployment

1. Deploy the agent:
```bash
poetry run deploy-remote --create
```

2. Create a session:
```bash
poetry run deploy-remote --create_session --resource_id=your-resource-id
```

3. List sessions:
```bash
poetry run deploy-remote --list_sessions --resource_id=your-resource-id
```

4. Send a message:
```bash
poetry run deploy-remote --send --resource_id=your-resource-id --session_id=your-session-id --message="Hello, how are you doing today? So far, I've made breakfast today, walkted dogs, and went to work."
```

5. Clean up (delete deployment):
```bash
poetry run deploy-remote --delete --resource_id=your-resource-id
```

## Architecture Overview

<p align="center">
  <img src="https://google.github.io/adk-docs/assets/agent-types.png" alt="Agents" width="700">
</p>

The ADK Bot leverages Google's Agent Development Kit to create a message shortening agent. The architecture consists of:

- **Agent Core**: Handles the main logic for message shortening
- **Tools**: Custom function tools for message processing
- **Sessions**: Maintain conversation context
- **Runner**: Orchestrates the execution flow

## Agent Development Kit (ADK) Concepts

Google's ADK provides a framework for building AI agents with the following key components:

### Core Components

- **Agents**: The central entities that make decisions and take actions
- **Tools**: Functions that agents can use to perform specific actions
- **Runners**: Components that manage the execution flow of agents
- **Sessions**: Maintain the context and state of conversations
- **Events**: The communication mechanism between components

### Architectural Patterns

ADK is built around a flexible, event-driven architecture that enables:

- **Modular Design**: Components can be combined and reconfigured
- **Extensibility**: The system can be extended with new tools, models, and agent types
- **Separation of Concerns**: Clear boundaries between reasoning (agents), capabilities (tools), execution (runners), and state management (sessions)

## Project Structure

```
adk-bot/
├── adk_bot/          # Main package directory
│   ├── __init__.py
│   ├── agent.py           # Agent implementation
│   └── prompt.py          # Prompt templates
├── deployment/            # Deployment scripts
│   ├── local.py          # Local testing script
│   └── remote.py         # Remote deployment script
├── .env                  # Environment variables
├── poetry.lock          # Poetry lock file
└── pyproject.toml       # Project configuration
```

## How It Works

<p align="center">
  <img src="https://google.github.io/adk-docs/assets/event-loop.png" alt="Event Loop" width="600">
</p>

<p align="center">
  <img src="https://google.github.io/adk-docs/assets/deploy-agent.png" alt="Deploying your agent" width="600">
</p>

1. **Input Processing**: The agent receives a message to shorten
2. **Analysis**: The message is analyzed for key content and redundancies
3. **Shortening**: The agent uses Vertex AI to generate a concise version while preserving meaning
4. **Response**: The shortened message is returned to the user

## Development

To add new features or modify existing ones:

1. Make your changes in the relevant files
2. Test locally using the local deployment script
3. Deploy to remote using the remote deployment script
4. Update documentation as needed

### Adding Custom Tools

Create new tools by defining Python functions and registering them with the agent:

```python
def custom_tool(input_text: str) -> str:
    """Custom processing function"""
    # Process the input text
    return processed_text

# Register with agent
agent = Agent(
    name="message_shortener",
    tools=[custom_tool],
    # Other parameters
)
```

## Troubleshooting

1. If you encounter authentication issues:
   - Ensure you're logged in with `gcloud auth login`
   - Verify your project ID and location in `.env`
   - Check that the Vertex AI API is enabled

2. If deployment fails:
   - Check the staging bucket exists and is accessible
   - Verify all required environment variables are set
   - Ensure you have the necessary permissions in your Google Cloud project

3. Common error messages and solutions:
   - **"API not enabled"**: Run `gcloud services enable aiplatform.googleapis.com`
   - **"Quota exceeded"**: Request additional quota in Google Cloud Console
   - **"Session not found"**: Ensure the session ID is correct and the session exists

## Resources

- [Official ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Google Cloud API Reference](https://cloud.google.com/apis)
- [ADK Quickstart Guide](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
