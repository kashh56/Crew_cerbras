from crewai import Agent
from typing import List
from crewai_tools import SerperDevTool

def get_researcher(llm, tools: List, topic: str = "") -> Agent:
    """Creates a research specialist agent."""
    return Agent(
        role="Research Specialist",
        goal="Analyze trends and provide concise insights",
        backstory="Expert researcher specializing in trend analysis and clear reporting",
        tools=tools,
        llm=llm,
        max_iter=2,
        verbose=True
    ) 