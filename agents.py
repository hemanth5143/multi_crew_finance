from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import market_tool, stock_tool


llm = ChatGoogleGenerativeAI(model = 'google-1.5-flash',
                              verbose = True,
                              temperature = 0.5,
                              google_api_key = "GOOGLE_API_KEY")


from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool




stock_analyst = Agent(
    role='Stock Analyst',
    goal='Analyze top-performing stocks in trending sectors',
    verbose=True,
    memory=True,
    backstory=(
        "With extensive experience in stock analysis, you can quickly"
        "identify which stocks are outperforming within any given sector."
        "You provide detailed insights into stock performance."
    ),
    tools=[stock_tool],
    allow_delegation=False
)



market_analyst = Agent(
    role='Market Analyst',
    goal='Identify trending market sectors and explain reasons behind the trends',
    verbose=True,
    memory=True,
    backstory=(
        "As a market analyst, you have a keen eye for identifying"
        "emerging trends and understanding the underlying factors driving"
        "these trends. You are well-versed in market analysis and data interpretation."
    ),
    tools=[market_tool],
    allow_delegation=True
)
