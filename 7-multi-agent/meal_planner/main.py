import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from manager.agent import root_agent

load_dotenv()

# Initialize session service
session_service = InMemorySessionService()

APP_NAME = "MealPlannerBot"
USER_ID = "user_meal_planner"
SESSION_ID = str(uuid.uuid4())

# Create a new session
session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state={}
)

print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)

# Simulate user input
user_input = "Provide a shopping list for healthy, carb-free vegetarian meals for the next 3 days."

new_message = types.Content(role="user", parts=[types.Part(text=user_input)])

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

# Retrieve and display the updated session state
print("\n==== Final Session State ====")
session = session_service.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

for key, value in session.state.items():
    print(f"{key}: {value}")
