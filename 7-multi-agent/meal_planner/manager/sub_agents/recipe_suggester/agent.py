import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

recipe_suggester_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4.1", api_key=os.getenv("OPENAI_API_KEY")),
    name="recipe_suggester_agent",
    instruction=(
        "Suggest recipes for each meal in the plan, considering the user's available ingredients."
    ),
    output_key="recipes"
)
