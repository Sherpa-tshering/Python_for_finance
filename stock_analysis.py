import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Lets download the stock data for Apple Inc. (AAPL)
ticker = "AAPL"
stock_data = yf.download(ticker, start="2022-01-01", end="2025-01-01")

# Lets see the first few rows of the data for clear image
print(stock_data.head())

# Calculating moving average
stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()

# Calculating daily returns
stock_data['Daily_Return'] = stock_data['Close'].pct_change()

# Calculating cumulative returns
stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod()

# Plot closing prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['20_MA'], label='20-Day MA')
plt.plot(stock_data['50_MA'], label='50-Day MA')
plt.title('AAPL Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot daily returns
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Daily_Return'], label='Daily Return')
plt.title('AAPL Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.show()


# Plot cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Cumulative_Return'], label='Cumulative Return')
plt.title('AAPL Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.show()

# Calculate Bollinger Bands
stock_data['Middle_Band'] = stock_data['Close'].rolling(window=20).mean()
stock_data['Upper_Band'] = stock_data['Middle_Band'] + 2 * stock_data['Close'].rolling(window=20).std()
stock_data['Lower_Band'] = stock_data['Middle_Band'] - 2 * stock_data['Close'].rolling(window=20).std()

# Plot Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['Middle_Band'], label='Middle Band')
plt.plot(stock_data['Upper_Band'], label='Upper Band')
plt.plot(stock_data['Lower_Band'], label='Lower Band')
plt.title('AAPL Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate RSI
stock_data['RSI'] = calculate_rsi(stock_data)


# Calculate MACD and Signal Line
stock_data['MACD'] = stock_data['Close'].ewm(span=12, adjust=False).mean() - stock_data['Close'].ewm(span=26, adjust=False).mean()
stock_data['Signal_Line'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()

# Plot MACD and Signal Line
plt.figure(figsize=(12, 6))
plt.plot(stock_data['MACD'], label='MACD')
plt.plot(stock_data['Signal_Line'], label='Signal Line')
plt.title('AAPL MACD and Signal Line')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Plot Volume
plt.figure(figsize=(12, 6))
plt.bar(stock_data.index, stock_data['Volume'], color='blue', alpha=0.5)
plt.title('AAPL Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()


# Plot RSI
plt.figure(figsize=(12, 6))
plt.plot(stock_data['RSI'], label='RSI')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')
plt.title('AAPL RSI')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.show()

# Plot Closing Prices with Moving Averages and Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['20_MA'], label='20-Day MA')
plt.plot(stock_data['50_MA'], label='50-Day MA')
plt.plot(stock_data['Middle_Band'], label='Middle Band')
plt.plot(stock_data['Upper_Band'], label='Upper Band')
plt.plot(stock_data['Lower_Band'], label='Lower Band')
plt.title('AAPL Stock Price and Moving Averages with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot MACD and Signal Line
plt.figure(figsize=(12, 6))
plt.plot(stock_data['MACD'], label='MACD')
plt.plot(stock_data['Signal_Line'], label='Signal Line')
plt.title('AAPL MACD and Signal Line')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


