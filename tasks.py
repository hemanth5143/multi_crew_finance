from crewai import Agent, Task, Crew, Process   
from tools import market_tool, stock_tool
from agents import market_analyst, stock_analyst

# Tasks
market_analysis_task = Task(
    description=(
        "Research and identify which market sectors are currently trending."
        "Explain the reasons behind their trends. Focus on economic indicators,"
        "news trends, and market sentiment."
    ),
    expected_output='A detailed report on trending market sectors and reasons for their trends.',
    tools=[market_tool],
    agent=market_analyst,
)

stock_analysis_task = Task(
    description=(
        "Analyze stocks in the trending sectors identified by the Market Analyst."
        "Identify and report on the top-performing stocks in these sectors."
    ),
    expected_output='A list of top-performing stocks in the trending sectors with analysis.',
    tools=[stock_tool],
    agent=stock_analyst,
    async_execution=False,
    output_file='top-performing-stocks.md'
)