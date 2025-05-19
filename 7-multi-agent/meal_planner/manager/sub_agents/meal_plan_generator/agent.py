import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

meal_plan_generator_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4.1", api_key=os.getenv("OPENAI_API_KEY")),
    name="meal_plan_generator_agent",
    instruction=(
        "Generate a 7-day meal plan based on the user's dietary preferences and nutritional goals."
    ),
    output_key="meal_plan"
)
