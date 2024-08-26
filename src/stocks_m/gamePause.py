from stocks.stock import Stock

class GamePause(Stock):
  def __init__(self, stock_price: float):
    super().__init__(stock_price, "GamePause")
