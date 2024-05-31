from stocks.stock import Stock

class Doors(Stock):
  def __init__(self, stock_price: float):
    super().__init__(stock_price, "Doors")
