from crewai_tools import BaseTool
import requests

# Custom Tools
class MarketDataTool(BaseTool):
    name: str = "Market Data Tool"
    description: str = "Fetches trending market sectors and explains reasons behind their trends."

    def _run(self, argument: str) -> str:
        api_url = "https://api.example.com/market-trends"
        response = requests.get(api_url)
        data = response.json()
        trending_sectors = data['trending_sectors']
        reasons = data['reasons']
        report = f"Trending Sectors: {trending_sectors}\nReasons: {reasons}"
        return report

class StockDataTool(BaseTool):
    name: str = "Stock Data Tool"
    description: str = "Fetches and analyzes top-performing stocks in specified sectors."

    def _run(self, sector: str) -> str:
        api_url = f"https://api.example.com/stocks?sector={sector}"
        response = requests.get(api_url)
        data = response.json()
        top_stocks = data['top_stocks']
        report = f"Top Performing Stocks in {sector}: {top_stocks}"
        return report

# Market Analyst Agent
market_tool = MarketDataTool()
stock_tool = StockDataTool()