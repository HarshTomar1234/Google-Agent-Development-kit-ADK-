from google.adk.agents import Agent
from google.adk.tools import google_search

from google.adk.tools import FunctionTool

def weather_forecast(location: str, days: int = 3) -> str:
    """
    Get a simulated weather forecast for a location.
    
    Args:
        location: The city or location to get weather for
        days: Number of days for the forecast (default: 3)
        
    Returns:
        A simulated weather forecast as a string
    """
    import random
    
    weather_conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Thunderstorms", "Snowy", "Windy"]
    temperature_ranges = {
        "Sunny": (75, 95),
        "Partly Cloudy": (65, 85),
        "Cloudy": (60, 75),
        "Rainy": (55, 70),
        "Thunderstorms": (60, 80),
        "Snowy": (20, 35),
        "Windy": (50, 65)
    }
    
    forecast = f"Weather forecast for {location} for the next {days} days:\n\n"
    
    for day in range(1, days + 1):
        condition = random.choice(weather_conditions)
        temp_range = temperature_ranges[condition]
        temp = random.randint(temp_range[0], temp_range[1])
        
        forecast += f"Day {day}: {condition}, {temp}°F\n"
    
    return forecast



root_agent = Agent(
    name = "tool_agent",
    model = "gemini-2.0-flash",
    description = "An agent that can search the web",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search: Search the web for information
    - weather_forecast: Get a simulated weather forecast for a location
    """,
    # tools =[google_search],
    tools = [weather_forecast],
)

## Only pass in one built in tool at a time and we can't pass in built in tool and custom tool both at the same time