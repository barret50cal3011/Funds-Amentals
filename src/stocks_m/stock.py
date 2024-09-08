import numpy as np
from stocks_m.abstractstock import AbstractStock


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

  def stock_variation_storer(self) -> None:
    if len(self.__stock_variation) < 22:
      self.__stock_variation.append(self.__stock_price)
    elif len(self.__stock_variation) == 22:
      self.__stock_variation.pop(0)
  

  def event_affect_stock(self, event) -> None:
    self.__stock_price = self.__stock_price(1 + event.get_percentage())


  # This will generates randomly values for each stock and apply the tendence in case the conditional be True
  def stock_price_variation(self) -> None:

    # Creates a instance of a random number generator
    rng = np.random.default_rng()
    # Generates a random number in percentage that will affect stock price
    volatility_change = rng.normal(loc=self.__mean, scale=self.__std, size=1)
    self.__stock_price = self.__stock_price * (1 +  volatility_change)
    self.__stock_price =(round(self.get_stock_price(), 2))

    if len(self.__affected_by) > 0:
      for event in self.__affected_by:
        self.event_affect_stock(event=event)
    self.stock_variation_storer()
    


