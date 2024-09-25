import numpy as np
import yfinance as yf


"""
This module let us generate the std and mean that need each stocks for his init
We copy the info and put this in the init of each stock in world
"""


stock: dict = {"Doors": "MSFT", 
            "Edison": "TSLA",
            "Game pause": "GME",
            "ArabOilCompany": "2222.SR",
            "MVidia": "NVDA",
            "Pear": "AAPL",
            "USWeapons": "LMT"}


stock_std_mean: dict = {"Doors": [], 
            "Edison": [],
            "Game pause": [],
            "ArabOilCompany": [],
            "MVidia": [],
            "Pear": [],
            "USWeapons": []}


for sub_stock in stock:
    name_reference_stock = stock[sub_stock]
    # Download historical data from the stock
    datums = yf.download(name_reference_stock, start='2024-01-01', end='2024-09-05', interval="1d")

    # Get the close price from the stock
    price = datums['Adj Close']
    variation = np.diff(np.log(price))

    mean = np.mean(variation)

    standard_deviation = np.std(variation)

    stock_std_mean[sub_stock].append(standard_deviation)
    stock_std_mean[sub_stock].append(mean)


print(stock_std_mean)