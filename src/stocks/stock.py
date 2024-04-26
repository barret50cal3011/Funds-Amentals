class Stock:
  def __init__(self, stock_price: float , company_name: str):
    self.__stock_price: float = stock_price
    self.company_name: str = company_name

  def get_stock_price(self) -> float:
    return self.__stock_price
    
  def set_stock_price(self, stock_price: float):
    if stock_price == str:
      raise TypeError('Stock price isn\'t a str ')
    
    else:
      self.__stock_price = stock_price
