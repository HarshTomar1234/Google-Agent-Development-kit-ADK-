from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)


# AgentTool --> A tool that wraps an agent.

# This tool allows an agent to be called as a tool within a larger application. The agent's input schema is used to define the tool's input parameters, and the agent's output is returned as the tool's result.
# This is done by wrapping the agent in a function that takes the input parameters as arguments and returns the agent's output. The function is then registered as a tool with the tool registry.
# This is done because we have used built-in tools like google_search, code_interpreter etc. with sub agents......and we can't use them..as per documentation....so in order to use them we have to wrap them in a function and register them as a tool.