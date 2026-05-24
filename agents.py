from crewai import LLM, Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
import os

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    verbose=True,
    temperature=0.7
)

news_researcher=Agent(
    role='Senior Researcher',
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory='Driven by curiosity, you are at the forefront of innovation, eager to explore and share knowledge that could change the world',
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer=Agent(
    role='Writer',
    goal='Narrate compeling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory='With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner',
    tools=[tool],
    llm=llm,
    allow_delegation=False
)