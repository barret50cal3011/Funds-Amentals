from stocks.stock import Stock

class ArabOilCompany(Stock):
  def __init__(self, stock_price: float):
    super().__init__(stock_price, "ArabOilCompany")

