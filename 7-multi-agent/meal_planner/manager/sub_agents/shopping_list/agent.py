import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

shopping_list_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4.1", api_key=os.getenv("OPENAI_API_KEY")),
    name="shopping_list_agent",
    instruction=(
        "Create a shopping list for ingredients not available at home, based on the meal plan."
    ),
    output_key="shopping_list"
)
