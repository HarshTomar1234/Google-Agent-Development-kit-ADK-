"""
Sequential Agent for Customer Support Ticket Processing

This example demonstrates a support ticket processing pipeline that classifies,
prioritizes, and recommends resolutions for customer support tickets.
"""

from google.adk.agents import SequentialAgent

from .sub_agents.classifier import ticket_classifier_agent
from .sub_agents.priority import ticket_priority_agent
from .sub_agents.recommender import resolution_recommender_agent

# Create the sequential agent
root_agent = SequentialAgent(
    name="SupportTicketPipeline",
    sub_agents=[ticket_classifier_agent, ticket_priority_agent, resolution_recommender_agent],
    description="A pipeline that classifies, prioritizes, and recommends resolutions for support tickets",
)


"""
## How It Works
1. The user submits a support ticket with their issue description
2. The Ticket Classifier Agent categorizes the ticket (Technical, Billing, etc.)
3. The classification is passed to the Priority Assessor Agent which determines urgency
4. Both the classification and priority are passed to the Resolution Recommender Agent
5. The final output provides the support team with a complete action plan
"""