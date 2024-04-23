from stocks.stock import Stock

class Edison(Stock):
  def __init__(self, stock_price: float, company_name: str):
    super().__init__(stock_price, company_name)
