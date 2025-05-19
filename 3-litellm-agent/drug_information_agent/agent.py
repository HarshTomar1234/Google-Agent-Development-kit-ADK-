import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# https://docs.litellm.ai/docs/providers/openrouter
model = LiteLlm(
    model="openai/gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# model = LiteLlm(
#     model="openrouter/openai/gpt-4.1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )

root_agent = Agent(
    name="drug_information_agent",
    model=model,
    description="Drug information agent",
    instruction="""
    You are a medical assistant and researcher that can provide details about drugs and its applications, symptoms, use-cases. 
    """,
)
