import requests
import os



ApiKey = "LRUBTT8K83R72KNM"


class AlphaVantage:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def yesterdayData(self):
        """
        The function retrieves daily time series data for a specified stock symbol using the Alpha
        Vantage API.
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ApiKey}'
        r = requests.get(url)
        rawData = r.json()
        return rawData

data = AlphaVantage()
data = data.yesterdayData()

# The `prompt` variable in your code is a formatted string (using f-string) that serves as a prompt or
# message template for presenting information to the user or displaying it in some way. In this case,
# it seems like the `prompt` is designed to provide guidance and instructions for analyzing historical
# market data and identifying trends based on moving averages, support & resistance levels, volume
# analysis, and other technical indicators.
prompt = f"""
            You are a market trend detective! Your mission is to analyze the provided historical market data (OHLCV format) and crack the case of the current and potential future trends.

Sharpen your tools:

Moving Averages: {MVdata} Calculate SMAs for various periods (e.g., 50-day, 200-day) and compare price action to identify uptrends, downtrends, or sideways movement.
Support & Resistance: Look for historical price action patterns to pinpoint support and resistance levels. Uptrends break above resistance, downtrends break below support, and sideways movement bounces between those levels.
Volume Analysis: Watch how trading volume interacts with price movements. Increasing volume on upticks and decreasing volume on pullbacks suggest uptrends. The opposite suggests downtrends, with a caveat for potential bear traps. Sideways movement often has consistent volume.
Bonus Tools: Consider technical indicators like RSI and MACD for additional confirmation.
Present your findings:

Classify the current trend (uptrend, downtrend, sideways).
Explain your reasoning based on the evidence gathered from moving averages, support & resistance, and volume analysis.
Briefly discuss the possibility of a trend reversal based on the current market conditions.
Remember:

Technical analysis has limitations, and the market is inherently unpredictable.
Account for outliers and data gaps in the provided data.
Case in point:

Analyze the provided OHLCV data {data} for {ticker} and become the ultimate trend detective! Unveil the current market trend, explain your reasoning, and assess the chances of a future shift.
        """
        