from stocks.abstractstock import AbstractStock

class Stock(AbstractStock):
    def __init__(self, stock_price: float, company_name: str):
        self._stock_price: float = stock_price
        self.company_name: str = company_name

    def get_stock_price(self) -> float:
        return self._stock_price

    def set_stock_price(self, stock_price: float):
        if not isinstance(stock_price, float):
            try:
                stock_price = float(stock_price)
            except ValueError as error:
                print(f'Error: {error}')
                return
        self._stock_price = stock_price
