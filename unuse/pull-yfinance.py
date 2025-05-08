import yfinance as yf
import pandas as pd
import requests
import time
import os

# Step 1: Get the S&P 500 tickers from Wikipedia
wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
tables = pd.read_html(wiki_url)
# sp500_tickers = tables[0]['Symbol'].tolist()
sp500_tickers = ['NVDA']

# Step 2: Define parameters
start_date = "2015-04-03"  # 5 years ago from today
end_date = "2025-04-05"    # Today

# Step 3: Fetch historical data for each ticker
all_data = {}

output_folder = "/home/kamin/Documents/CPE 241 Project/sp500_data"
os.makedirs(output_folder, exist_ok=True)

for ticker in sp500_tickers:
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if not stock_data.empty:
            file_path = os.path.join(output_folder, f"{ticker}.csv")
            stock_data.to_csv(file_path)
        time.sleep(5)  # Add a 5-second delay between requests
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

# Step 4: Convert to DataFrame and save to CSV
# combined_data = pd.concat(all_data, names=["Ticker", "Date"])
# combined_data.to_csv("sp500_10yr_data.csv")

print("Data saved successfully!")