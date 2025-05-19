"""
Ticket Classifier Agent

This agent is responsible for classifying customer support tickets
into appropriate categories/departments.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the classifier agent
ticket_classifier_agent = LlmAgent(
    name="TicketClassifierAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Support Ticket Classification AI.
    
    Analyze the customer support ticket and classify it into one of these categories:
    - Technical: Software bugs, errors, or technical malfunctions
    - Billing: Payment issues, subscription questions, refunds
    - Account: Login problems, account settings, security
    - Product: Product features, usage questions, compatibility
    - Other: Anything that doesn't fit the above categories
    
    Output ONLY the category name and a brief justification.
    
    Example output: 'Technical: User reports application crashes during startup'
    Example output: 'Billing: Customer disputes recent charge on their account'
    """,
    description="Classifies support tickets into appropriate categories.",
    output_key="ticket_category",
)