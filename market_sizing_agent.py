from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from core.schemas import StartupProfile

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

def build_market_sizing_agent(profile: StartupProfile):
    analyst = Agent(
        role="Market-sizing analyst",
        goal="Estimate TAM, SAM, SOM in USD millions.",
        backstory="Former McKinsey consultant specialised in market intelligence.",
        verbose=True,
        llm=llm,
    )

    def _callback(*_):
        return '{ "TAM": 1000, "SAM": 500, "SOM": 100 }'

    task = Task(
        description="Provide TAM, SAM, SOM estimates.",
        agent=analyst,
        expected_output="JSON with TAM/SAM/SOM",
        callback=_callback,
    )
    return analyst, task
