import random, json
import numpy as np
from stocks_m.abstractstock import AbstractStock

# with open('../data/events.json', 'r') as file:
#     json_file = json.load(file)



class Stock(AbstractStock):
  def __init__(self, stock_price: float = None, company_name: str = None, std: float = None, mean: float = None):
    self.__stock_price: float = stock_price
    self.__company_name: str = company_name
    self.__std:float = std
    self.__mean:float = mean
    self.__affected_by:list = []
    self.__stock_variation:list = []

  def get_company_name(self) -> float:
    return self.__company_name

  def get_stock_price(self) -> float:
    return self.__stock_price
  
  def set_stock_price(self, stock_price: float) -> None:
    if stock_price != float:
      try:
        float(stock_price)
        self.__stock_price = stock_price
        
      except ValueError as error:
        print(f'Error: {error}')

    else:
      self.__stock_price = stock_price

  
  def get_stock_variation(self) -> list:
    return self.__stock_variation

  def get_affected_by(self) -> list:
    return self.__affected_by
  
  
  def add_affected_by(self, event_name: str) -> None:
    self.__affected_by.append(event_name)

  def delete_affected_by(self, event_name: str) -> None:
    try:
      self.__affected_by.remove(event_name)
    except ValueError as error:
      print(f'Error: {error}')

  def stock_variation_changer(self) -> None:
    if len(self.__stock_variation) < 22:
      self.__stock_variation.append(self.__stock_price)
    elif len(self.__stock_variation) == 22:
      self.__stock_variation.pop(0)
  
  #! Not ready need json
  def event_affect_stock(self) -> None:
    pass


  # This will generates randomly values for each stock
  def stock_price_variation(self) -> None:
    rng = np.random.default_rng()
    volatility_change = rng.normal(loc=self.__mean, scale=self.__std, size=1)
    self.__stock_price = self.__stock_price * (1 +  volatility_change)
    self.__stock_price =(round(self.get_stock_price(), 2))

    if len(self.__affected_by) > 0:
      self.event_affect_stock()
    self.stock_variation_changer()
    


