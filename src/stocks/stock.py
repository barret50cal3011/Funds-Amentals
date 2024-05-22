class Stock:
  def __init__(self, stock_price: float , company_name: str):
    self.__stock_price: float = stock_price
    self.company_name: str = company_name

  def get_stock_price(self) -> float:
    return self.__stock_price
    
  def set_stock_price(self, stock_price: float):
    if stock_price != float:
      try:
        float(stock_price)
      except ValueError as error:
        print(f'Error: {error}')
    else:
      self.__stock_price = stock_price
