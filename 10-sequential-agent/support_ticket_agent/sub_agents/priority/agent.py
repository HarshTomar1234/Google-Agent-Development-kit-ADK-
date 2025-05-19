"""
Ticket Priority Agent

This agent is responsible for assessing the priority level
of customer support tickets.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the priority agent
ticket_priority_agent = LlmAgent(
    name="TicketPriorityAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Support Ticket Priority Assessment AI.
    
    Based on the ticket information and classification, assign a priority level:
    - Critical: System-wide issues, security breaches, complete loss of service
    - High: Significant impact on business operations, no workaround available
    - Medium: Limited impact, workaround available, affecting multiple users
    - Low: Minor issues, cosmetic problems, affecting single user
    
    Consider factors like impact scope, business criticality, and urgency.
    
    Output ONLY the priority level and ONE sentence justification.
    
    Ticket Category:
    {ticket_category}
    
    Example output: 'Critical: Complete system outage affecting all users'
    Example output: 'Low: Minor UI alignment issue on rarely used screen'
    """,
    description="Assesses priority level of support tickets.",
    output_key="ticket_priority", 
)