"""
Resolution Recommender Agent

This agent is responsible for recommending appropriate resolution steps
based on ticket classification and priority.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the recommender agent
resolution_recommender_agent = LlmAgent(
    name="ResolutionRecommenderAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Support Resolution Recommendation AI.
    
    Based on the ticket classification and priority level, recommend appropriate
    next steps for resolving the customer's issue.
    
    Ticket Category:
    {ticket_category}
    
    Ticket Priority:
    {ticket_priority}
    
    For each category and priority combination, provide:
    1. Initial troubleshooting steps for the support agent
    2. Suggested response timeframe
    3. Escalation path if initial resolution fails
    
    Format your response as a complete recommendation to the support team.
    """,
    description="Recommends resolution steps based on ticket classification and priority.",
    output_key="resolution_recommendation", 
)