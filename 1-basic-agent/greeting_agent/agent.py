from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Agent for greeting with a motivational thought",
    instruction = """
    You are a helpful assistant that basically greets the user and provides a motivational thought.
    Ask for the user's name and greet them by name followed by a motivational thought.
    """
)