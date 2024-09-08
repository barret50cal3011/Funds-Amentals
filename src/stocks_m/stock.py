import pandas as pd
import mplfinance as mpf
import numpy as np
from stocks_m.abstractstock import AbstractStock
from events_m.events import Events
import time

class Stock(AbstractStock):
  def __init__(self, stock_price: float = None, company_name: str = None, std: float = None, mean: float = None, description: str = None, actives: str = None):
    super().__init__(stock_price, company_name, std, mean, description, actives)
    self.__stock_price: float = stock_price
    self.__company_name: str = company_name
    self.__std: float = std
    self.__mean: float = mean
    self.__affected_by: list = []
    self.__stock_variation: list = []
    self.__stock_description: str = description
    self.__actives: str = actives
    self.percentage_change = 0.0
    self.current_price: float = self.__stock_price
    
  #change the type float to string
  def get_company_name(self) -> str:
    return self.__company_name
  
  def get_stock_price(self) -> float:
    return self.current_price
  
  def update_stock_price(self,percentage: float) -> None:
    self.percentage_change = percentage
    self.current_price +=self.current_price*(percentage/100)
    
  def get_percentage(self):
    return self.percentage_change
    
  def set_stock_price(self, stock_price: float) -> None:
    try:
      self.__stock_price = float(stock_price)
    except ValueError as error:
      print(f'Error: {error}')
  
  def get_stock_variation(self) -> list:
    return self.__stock_variation

  def get_affected_by(self) -> list:
    return self.__affected_by
  
  # Will return daily volatility
  def get_volatility(self) -> float:
    return round((self.__std * 100), 2)

  def get_stock_description(self) -> str:
    return self.__stock_description
  
  def get_actives(self) -> float:
    return self.__actives

  def add_affected_by(self, event_name: str) -> None:
    self.__affected_by.append(event_name)

  def delete_affected_by(self, event_name: str) -> None:
    try:
      self.__affected_by.remove(event_name)
    except ValueError as error:
      print(f'Error: {error}')
  
  def stock_variation_storer(self, open=None, close=None, high=None, low=None) -> None:
    if len(self.__stock_variation) < 30:
      self.__stock_variation.append({
        "Open":open,
        "Close":close,
        "High":high,
        "Low":low})
      
      # The `candlestick` method uses the data stored in `__stock_variation` to create a DataFrame and plot a candlestick chart.
      # For this method to work correctly:
      # Data Structure: The `__stock_variation` list must contain dictionaries with stock price data.
      # Each dictionary should have keys "Open", "Close", "High", and "Low", which are needed to create the candlestick chart.

      
    elif len(self.__stock_variation) == 30:
      self.__stock_variation.pop(0)
  
  def event_affect_stock(self, event: Events):
    ###self.__stock price is an atributte, not a method (*) and event type is Event
    self.__stock_price = self.__stock_price*(1 + event.get_percentage())

  # This will generates randomly values for each stock and apply the tendence in case the conditional be True
  def stock_price_variation(self) -> None:
    # Creates a instance of a random number generator
    rng = np.random.default_rng()
    #Generates a random number in percentage that will affect stock price
    volatility_change = rng.normal(loc=self.__mean, scale=self.__std, size=5)
    '''
    self.__stock_price = self.__stock_price * (1 +  volatility_change)
    self.__stock_price =(round(self.get_stock_price(), 2))
    #Generate the second variation of the stock price
    second_volatility_change = rng.normal(loc=self.__mean, scale=self.__std*2, size=1)
    '''
    prices=[self.__stock_price*(1+change) for change in volatility_change]
    open=prices[0]
    close=prices[-1]
    high=max(prices)
    low=min(prices)
    
    self.stock_variation_storer(open, close, high, low)
    if len(self.__affected_by) > 0:
      for event in self.__affected_by:
        self.event_affect_stock(event=event)
  
  def candlestick(self):
      if len(self.__stock_variation) > 0:
          # Create a DataFrame from the stock variations
          df = pd.DataFrame(self.__stock_variation)
          # Define the columns explicitly for the DataFrame
          df.columns = ['Open', 'Close', 'High', 'Low']
          time_manager = Time()
          # Generate a list of dates for the DataFrame index
          date_index = [time_manager.get_next_date() for _ in range(len(df))]
          # Convert the list of dates to a datetime index
          df.index = pd.to_datetime(date_index)
          mpf.plot(df, type='candle', style='charles', title=self.__company_name)
      else:
          print('No data available for this stock')
          
  def generate_initial_stock_data(self, num_days=30) -> None:
      '''
      Generates initial stock data for a given number of days using stock price variations.
      :param num_days: The number of days for which to generate stock data.
      '''
      for _ in range(num_days):
          self.stock_price_variation()
