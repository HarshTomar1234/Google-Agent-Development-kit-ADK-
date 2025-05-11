from google.adk.agents import Agent

from .prompt import ROOT_AGENT_INSTRUCTION

from .tools import count_characters

root_agent = Agent(
    name="adk_bot",
    model="gemini-2.0-flash",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)