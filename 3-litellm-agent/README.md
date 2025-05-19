# LiteLLM Agent Implementation

## ADK Concept: Models

The Google Agent Development Kit (ADK) is designed to be model-agnostic, meaning it can work with various language models beyond just Google's Gemini. This flexibility allows developers to choose the most appropriate model for their specific use case.

### Model Flexibility in ADK

According to the [ADK documentation on models](https://google.github.io/adk-docs/agents/models/), ADK strives to make it easy to use different language models with minimal code changes. ADK supports models in two ways:

1. **Direct Integration**: Native support for Google's Gemini models via Google AI Studio
2. **Model Wrappers**: Support for third-party models through wrapper classes (like LiteLLM)

## What is LiteLLM?

[LiteLLM](https://docs.litellm.ai/docs/) is a lightweight, open-source Python library that provides a unified interface for working with different large language models (LLMs). It standardizes the inputs and outputs for different LLM providers, making it easy to switch between them without changing your code.

### Key Features of LiteLLM:

- **Unified API**: LiteLLM translates calls to different LLMs into a consistent format, mimicking OpenAI's API structure
- **100+ Model Support**: Works with models from providers like OpenAI, Anthropic, Hugging Face, and more
- **Standardized Outputs**: Returns a consistent response structure no matter which model you use
- **Streaming Support**: Handles streaming responses from various providers
- **Exception Mapping**: Maps exceptions across providers to consistent types
- **Logging and Observability**: Built-in features for tracking usage, costs, and performance

### LiteLLM Architecture

LiteLLM acts as a translation layer between your application and various LLM providers:

```
Your Application → LiteLLM → Various LLM Providers (OpenAI, Anthropic, etc.)
```

## What is OpenRouter?

[OpenRouter](https://openrouter.ai/) is a platform that provides a unified API endpoint for accessing a wide variety of language models. It serves as an aggregator, allowing developers to use many different models through a single API key and endpoint.

### Key Features of OpenRouter:

- **Model Diversity**: Access to 50+ models from providers like OpenAI, Anthropic, Mistral, Meta, and others
- **Cost Efficiency**: Often offers better pricing than direct providers
- **Unified Endpoint**: One API for all supported models
- **OpenAI-Compatible API**: Uses the same API format as OpenAI, making it easy to integrate
- **Free Tier**: Offers free access to many models for experiments

## Implementation Details

This folder contains a drug information agent that leverages LiteLLM to use different language models.

### Project Structure
```
3-litellm-agent/
└── drug_information_agent/
    ├── __init__.py
    ├── agent.py
    ├── README.md
```

### Agent Description

The `drug_information_agent` is an agent that:
- Provides information about drugs and medications
- Can answer questions about drug interactions, side effects, and dosage
- Uses models from different providers via LiteLLM integration
- Demonstrates how to configure ADK to work with non-Google LLMs

### Code Explanation

The agent uses LiteLLM to integrate with other models:

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

# Set up the model using LiteLLM wrapper
model = LiteLlm(
    model="claude-2.0", 
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Create the agent with the LiteLLM model
root_agent = Agent(
    name="drug_information_agent",
    model=model,
    description="Agent that provides information about drugs and medications",
    instruction="""
    You are a helpful assistant specialized in providing information about drugs and medications.
    You can answer questions about drug interactions, side effects, dosage, and general pharmaceutical knowledge.
    Always prioritize safety and remind users to consult healthcare professionals.
    Never provide information that could lead to harmful use of drugs.
    """
)
```

Key implementation details:

1. **LiteLLM Model Configuration**: We use the `LiteLlm` wrapper class to configure the model
2. **API Key Management**: API keys for the model provider are managed via environment variables
3. **Model Selection**: Different models can be selected by changing the `model` parameter
4. **Agent Configuration**: The agent's instruction is tailored for a drug information use case

### Configuring LiteLLM with OpenRouter

You can easily switch to using OpenRouter models with LiteLLM:

```python
model = LiteLlm(
    model="openrouter/anthropic/claude-3-opus-20240229", 
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1"
)
```

This would use Anthropic's Claude 3 Opus model via OpenRouter, which might provide better pricing or availability.

### Available Models Through LiteLLM

LiteLLM supports a wide range of models that can be used with ADK:

| Provider | Model Example | Configuration |
|----------|---------------|---------------|
| OpenAI | gpt-4 | `model="gpt-4"` |
| Anthropic | claude-3-opus | `model="claude-3-opus"` |
| Mistral AI | mistral-large | `model="mistral-large"` |
| OpenRouter | openrouter/anthropic/claude-3-opus | `model="openrouter/anthropic/claude-3-opus"` |
| Google | gemini-1.5-pro | `model="gemini-1.5-pro"` |
| Meta/Llama | meta-llama/llama-3-70b-instruct | `model="meta-llama/llama-3-70b-instruct"` |

### Benefits of Using LiteLLM with ADK

1. **Model Flexibility**: Easily swap between different models to find the best one for your use case
2. **Provider Diversity**: Reduce dependency on a single provider
3. **Cost Optimization**: Choose models based on price-performance trade-offs
4. **Feature Compatibility**: Access models with specialized capabilities (e.g., vision models, code-focused models)
5. **Fallback Options**: Implement fallback strategies when primary models are unavailable

## Setting Up Your Environment

To use LiteLLM with ADK, you'll need:

1. Install LiteLLM: `pip install litellm`
2. Set up API keys for your chosen providers as environment variables
3. Configure the LiteLlm wrapper in your agent code
4. (Optional) Set up provider-specific configurations

For OpenRouter specifically:
1. Create an account at [OpenRouter](https://openrouter.ai/)
2. Generate an API key
3. Set the `OPENROUTER_API_KEY` environment variable
4. Configure your model with the OpenRouter API base URL

## Next Steps

After understanding how to use different models with ADK, you might want to explore:
- Creating structured outputs (see folder 4-structured-outputs)
- Implementing more complex tool interactions
- Setting up multi-agent systems with different models for different tasks

For more information, visit:
- [ADK Models documentation](https://google.github.io/adk-docs/agents/models/)
- [LiteLLM documentation](https://docs.litellm.ai/docs/)
- [OpenRouter documentation](https://openrouter.ai/docs) 