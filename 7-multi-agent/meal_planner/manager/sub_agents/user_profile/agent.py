import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

user_profile_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4.1", api_key=os.getenv("OPENAI_API_KEY")),
    name="user_profile_agent",
    instruction=(
        "Collect and update user dietary preferences, restrictions, and nutritional goals."
    ),
    output_key="user_profile"
)
