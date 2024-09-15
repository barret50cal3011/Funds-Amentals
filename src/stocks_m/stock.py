import random
import pandas as pd
import mplfinance as mpf
import numpy as np
from stocks_m.abstractstock import AbstractStock
from events_m.events import Events
from newtimer import Time

class Stock(AbstractStock):
    def __init__(self, stock_price: float = None, company_name: str = None, std: float = None, mean: float = None, description: str = None, actives: str = None):
        super().__init__(stock_price, company_name, std, mean, description, actives)
        self.__stock_price: float = stock_price
        self.__company_name: str = company_name
        self.__std: float = std  # Standard deviation, used for volatility
        self.__mean: float = mean  # Mean value for stock changes
        self.__affected_by: list = []  # Stores events that affect the stock price
        self.__stock_variation: list = []  # Stores the daily stock variations (open, close, high, low)
        self.__stock_description: str = description
        self.__actives: str = actives
        self.percentage_change = 0.0
        self.current_price: float = self.__stock_price
        self.previous_close: float = self.__stock_price
        self.time_manager = Time()

    def get_company_name(self) -> str:
        return self.__company_name

    def get_stock_price(self) -> float:
        return self.current_price

    def set_stock_price(self, stock_price: float) -> None:
        try:
            self.__stock_price = float(stock_price)
            self.current_price = self.__stock_price
        except ValueError as error:
            print(f'Error: {error}')

    def get_stock_variation(self) -> list:
        return self.__stock_variation

    def get_affected_by(self) -> list:
        return self.__affected_by

    def get_volatility(self) -> float:
        return round((self.__std * 100), 2)

    def get_stock_description(self) -> str:
        return self.__stock_description

    def get_company_active(self) -> str:
        return self.__actives

    def add_affected_by(self, event_name: str) -> None:
        self.__affected_by.append(event_name)

    def delete_affected_by(self, event_name: str) -> None:
        try:
            self.__affected_by.remove(event_name)
        except ValueError as error:
            print(f'Error: {error}')

    def event_affect_stock(self, event: Events) -> None:
        """
        Apply the effect of an event on the stock price. The event object has a percentage impact.
        """
        self.current_price = self.current_price * (1 + event.get_percentage())
    
    def stock_price_variation(self) -> None:
        """
        Simulates random price variation based on stock volatility and previous closing prices.
        """
        rng = np.random.default_rng()
        volatility_change = rng.normal(loc=self.__mean, scale=self.__std, size=10)
        prices = [self.previous_close * (1 + change) for change in volatility_change]
        prices.sort()
        open = random.choice(prices[1:-2])
        close = random.choice(prices[1:-2])
        high = prices[-1]
        low = prices[0]
        self.current_price = close
        self.previous_close = close
        self.stock_variation_storer(open, close, high, low)

        if len(self.__affected_by) > 0:
            for event in self.__affected_by:
                self.event_affect_stock(event=event)

    def stock_variation_storer(self, open=None, close=None, high=None, low=None) -> None:
        """
        Stores stock data (open, close, high, low) for the day. Maintains only 30 days of history.
        """
        current_date = self.time_manager.get_next_date()
        if len(self.__stock_variation) < 30:
            self.__stock_variation.append({
                "Date": current_date,
                "Open": open,
                "Close": close,
                "High": high,
                "Low": low
            })
        elif len(self.__stock_variation) == 30:
            self.__stock_variation.pop(0)
            self.__stock_variation.append({
                "Date": current_date,
                "Open": open,
                "Close": close,
                "High": high,
                "Low": low
            })

    def candlestick(self):
        """
        Plots a candlestick chart of the stock's recent performance.
        """
        if len(self.__stock_variation) > 0:
            df = pd.DataFrame(self.__stock_variation)
            df.index = pd.to_datetime(df['Date'])
            df.drop(columns=['Date'], inplace=True) # Removes the 'Date' column from the original DataFrame, modifying it in place (inplace=True).
            mpf.plot(df, type='candle', style='charles', title=self.__company_name)
        else:
            print('No data available for this stock')

    def update_stock_price(self, percentage: float) -> None:
        """
        Updates the stock price based on a given percentage change.
        :param percentage: The percentage change to apply to the stock price.
        """
        self.percentage_change = percentage
        self.current_price += self.current_price * (percentage / 100)
        self.previous_close = self.current_price

    def get_previous_close(self) -> float:
        return self.previous_close

    def get_percentage(self) -> float:
        """
        Returns the most recent percentage change in stock price.
        """
        return self.percentage_change
      
    def generate_initial_stock_data(self, num_days=30) -> None:
        """
        Generates stock price variation data for a specified number of days.
        :param num_days: Number of days to generate data for.
        """
        for _ in range(num_days):
            self.stock_price_variation()
