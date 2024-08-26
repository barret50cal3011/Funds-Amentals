from stocks.stock import Stock

class Player:
    def __init__(self, i_starting_USD) -> None:
        self.__player_portfolio = {}
        self.__player_portfolio["USD"] = i_starting_USD


    def buy_stock(self, stock: Stock, quantity: int) -> None:
        if(quantity * stock.get_stock_price() > self.__player_portfolio["USD"]):
            raise ValueError("Not enough USD to buy stock")
        if stock in self.__player_portfolio:
            self.__player_portfolio[stock] += quantity
        else:
            self.__player_portfolio[stock] = quantity
        self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()


    def sell_stock(self, stock: Stock, quantity: int) -> None:
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            self.__player_portfolio["USD"] += quantity * stock.get_stock_price()
            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]
        else: 
            raise ValueError("Not enough stock to sell")


    def get_stock_amount(self, stock: Stock) -> int:
        if stock in self.__player_portfolio:
            return self.__player_portfolio[stock]
        else:
            return 0
        
    
    def get_portfolio(self):
        return self.__player_portfolio