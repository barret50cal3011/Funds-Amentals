from stocks_m.stock import Stock

class Player:
    def __init__(self, i_starting_USD) -> None:
        self.__player_portfolio = {}
        self.__player_portfolio["USD"] = i_starting_USD
        self.__player_stock_price_buy = {"Edison": {}, "ArabOilCompany": {}, "Doors":  {}, "GamePause":  {}, "Mvidia":  {}, "Pear":  {}, 'USWeapons':  {}}
        
    @property
    def player_balance_money(self):
        return self.__player_portfolio["USD"]

    def register_player_inversion(self, stock: Stock, quantity: float) -> None:

        stock_name = stock.get_company_name()
        stock_price = stock.get_stock_price()

        # Check if the price of the stock is already in the dictionary of the stock
        # If not, add it
        self.__player_stock_price_buy[stock_name].setdefault(stock_price, 0)
    
        # Increace the quantity of the stock ammount
        self.__player_stock_price_buy[stock_name][stock_price] += quantity


    def buy_stock(self, stock: Stock, quantity: int) -> None:
        if(quantity * stock.get_stock_price() > self.__player_portfolio["USD"]):
            raise ValueError("Not enough USD to buy stock")
        if stock in self.__player_portfolio:
            self.__player_portfolio[stock] += quantity
            self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()

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