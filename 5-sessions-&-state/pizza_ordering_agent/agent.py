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
