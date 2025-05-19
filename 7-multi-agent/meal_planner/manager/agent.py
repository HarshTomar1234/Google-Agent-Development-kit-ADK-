from google.adk.agents import Agent
from manager.sub_agents.user_profile.agent import user_profile_agent
from manager.sub_agents.meal_plan_generator.agent import meal_plan_generator_agent
from manager.sub_agents.recipe_suggester.agent import recipe_suggester_agent
from manager.sub_agents.shopping_list.agent import shopping_list_agent

root_agent = Agent(
    name="manager",
    model = "gemini-2.0-flash",
    description="Meal Planner manager agent",
    instruction="Coordinate the meal planning process by interacting with the respective agents.",
     sub_agents=[
        user_profile_agent,
        meal_plan_generator_agent,
        recipe_suggester_agent,
        shopping_list_agent
    ],
)
