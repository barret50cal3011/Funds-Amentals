from stocks.abstractstock import AbstractStock

class Stock(AbstractStock):
  def __init__(self, stock_price: float , company_name: str):
    self.__stock_price: float = stock_price
    self.company_name: str = company_name
    self.affected_by:list = []

  def get_stock_price(self) -> float:
    return self.__stock_price
    
  def set_stock_price(self, stock_price: float):
    if stock_price != float:
      try:
        float(stock_price)
        self.__stock_price = stock_price
        
      except ValueError as error:
        print(f'Error: {error}')

    else:
      self.__stock_price = stock_price

  def get_affected_by(self):
      return self.affected_by
  
  def add_affected_by(self, event_name: str):
      self.affected_by.append(event_name)

  def delete_affected_by(self, event_name: str):
      self.affected_by.remove(event_name)
      