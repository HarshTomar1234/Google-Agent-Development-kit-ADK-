import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pizza_ordering_agent.agent import pizza_ordering_agent

# Load environment variables
load_dotenv()

# Create a new session service to store state
session_service_stateful = InMemorySessionService()

# Define application and user identifiers
APP_NAME = "PizzaBot"
USER_ID = "user_pizza"
SESSION_ID = str(uuid.uuid4())

# Create a new session with an empty initial state
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state={}
)

print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

# Initialize the runner with the agent and session service
runner = Runner(
    agent=pizza_ordering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

# Define a list of user messages to simulate a conversation
user_messages = [
    "I want to order a pizza.",
    "Large size, please.",
    "Add pepperoni and mushrooms."
    "crust should be stuffed.",
    "Confirm my order."
]

# Process each user message
for user_input in user_messages:
    print(f"\nUser: {user_input}")
    new_message = types.Content(role="user", parts=[types.Part(text=user_input)])
    
    # Run the agent with the user message
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Agent: {event.content.parts[0].text}")

# Retrieve and display the updated session state
print("\n==== Final Session State ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

for key, value in session.state.items():
    print(f"{key}: {value}")
