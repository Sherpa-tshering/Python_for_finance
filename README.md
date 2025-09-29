# Python_for_finance
A self learning financial insights and data-driven decisions by analyzing stock data with Pandas

This Python script performs a comprehensive technical analysis on Apple Inc. using historical data downloaded from Yahoo Finance (yfinance). It calculates and visualize several key technical indicators to help users analyze price trends, momentum, and volatility.

## Features
1. Data Download
2. Moving Averages(MA)
3. Returns
4. Bollinger Bands (BB)
5. Relative Strength Index(RSI)
6. Moving Average Convergence Divergence (MACD)
7. Volume Analysis
8. Multiple Visualizations

## Customization
To analyze a different stock or time frame, simply modify these two lines at the beginning of the script:

--> Change the stock ticker [line 7]
    "ticker = "MSFT" (Microsoft)"

--> change the start and end dates [line 8]
    "stock_data = yf.download(ticker, start= "yyyy-mm-dd", end="yyyy-mm-dd")"