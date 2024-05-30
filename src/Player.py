from stocks.stock import Stock

class Player:
    def __init__(self, starting_usd: float):
        self.__player_portfolio = {}
        self.__player_portfolio["USD"] = starting_usd

    def buy_stock(self, stock: Stock, quantity: int):
        total_cost = quantity * stock.get_stock_price()
        if total_cost > self.__player_portfolio["USD"]:
            raise ValueError("Not enough USD to buy stock")
        if stock in self.__player_portfolio:
            self.__player_portfolio[stock] += quantity
        else:
            self.__player_portfolio[stock] = quantity
        self.__player_portfolio["USD"] -= total_cost

    def sell_stock(self, stock: Stock, quantity: int):
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            self.__player_portfolio["USD"] += quantity * stock.get_stock_price()
            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]
        else:
            raise ValueError("Not enough stock to sell")
        
    def get_stock_amount(self, stock: Stock) -> int:
        return self.__player_portfolio.get(stock, 0)

    def get_portfolio(self):
        return self.__player_portfolio
