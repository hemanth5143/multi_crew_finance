import os
from crewai import Agent, Task, Crew, Process
from tasks import market_analysis_task,stock_analysis_task
from agents import market_analyst,stock_analyst
from dotenv import load_dotenv
load_dotenv()


crew = Crew(
    agents=[market_analyst, stock_analyst],
    tasks=[market_analysis_task, stock_analysis_task],
    process=Process.sequential
)

# Kickoff the Crew
result = crew.kickoff(inputs={})
print(result)