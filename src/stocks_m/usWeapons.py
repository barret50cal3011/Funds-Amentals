from stocks.stock import Stock

class USWeapons(Stock):
  def __init__(self, stock_price: float):
    super().__init__(stock_price, "usWeapons")
