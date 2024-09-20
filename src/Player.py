from stocks_m.stock import Stock

class Player:
    def __init__(self, i_starting_USD) -> None:
        self.__player_portfolio = {}
        self.__player_portfolio["USD"] = i_starting_USD
        # self.__player_money_invested_in_stock = {"Edison": 0, "ArabOilCompany": 0, "Doors":  0, "GamePause":  0, "Mvidia":  0, "Pear":  0, 'USWeapons':  0}
        # self.__player_earns = {"Edison": 0, "ArabOilCompany": 0, "Doors":  0, "GamePause":  0, "Mvidia":  0, "Pear":  0, 'USWeapons':  0}
        # self.__player_loses = {"Edison": 0, "ArabOilCompany": 0, "Doors":  0, "GamePause":  0, "Mvidia":  0, "Pear":  0, 'USWeapons':  0}

    # Will show the amount of money the player has directly
    @property
    def player_money(self) -> float:
        return self.__player_portfolio["USD"]
    
   
    
    # # Will help to show the amount of money the player has earn or lost
    # def get_player_money_invested_in_stock(self, stock: Stock) -> float:
    #     stock_name = stock.get_company_name()
    #     return self.__player_money_invested_in_stock.get(stock_name)
    

    # # Save the balance of the player for each stock in the dictionary
    # def save_player_money_invested_in_stock(self, stock: Stock) -> None:
    #     stock_name = stock.get_company_name()
    #     stock_price = stock.get_stock_price()
    #     stock_quantity = self.__player_portfolio[stock]
    #     # Increace the money invested in the stock
    #     self.__player_money_invested_in_stock[stock_name] += stock_quantity * stock_price

    # def change_player_money_invested_in_stock(self, stock: Stock) -> None:
    #     stock_name = stock.get_company_name()
    #     stock_price = stock.get_stock_price()
    #     stock_quantity = self.__player_portfolio[stock]

    #     if stock_quantity == 0:
    #         self.__player_money_invested_in_stock[stock_name] = 0
    #     else:
    #         self.__player_money_invested_in_stock[stock_name] -= stock_quantity * stock_price


    # def calculate_player_balance(self, stock: Stock) -> float:
    #     stock_name = stock.get_company_name()
    #     stock_price = stock.get_stock_price()
    #     stock_quantity = self.__player_portfolio[stock]
    #     return  self.__player_money_invested_in_stock[stock_name] - stock_quantity * stock_price

    
    def validate_input_quantity(func):
        def wrapper(self, stock, quantity, *args, **kwargs):
            if not isinstance(quantity, int) and quantity > 0:
                raise ValueError("You should only input integers values greater than 0 for quantity")
            return func(self, stock, quantity, *args, **kwargs)
        return wrapper


    @validate_input_quantity
    def buy_stock(self, stock: Stock, quantity: int) -> None:
        if(quantity * stock.get_stock_price() > self.__player_portfolio["USD"]):
            raise ValueError("Not enough USD to buy stock")
        if stock in self.__player_portfolio:
            self.__player_portfolio[stock] += quantity
            self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()

        else:
            self.__player_portfolio[stock] = quantity
            self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()

        # self.save_player_money_invested_in_stock(stock)

    @validate_input_quantity
    def sell_stock(self, stock: Stock, quantity: int) -> None:
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            self.__player_portfolio["USD"] += quantity * stock.get_stock_price()
            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]
                # self.change_player_money_invested_in_stock(stock)
        else: 
            raise ValueError("Not enough stock to sell")


    def get_stock_amount(self, stock: Stock) -> int:
        if stock in self.__player_portfolio:
            return self.__player_portfolio[stock]
        else:
            return 0
        
    
    def get_portfolio(self):
        return self.__player_portfolio
    

    def __str__(self):
        print("You have bought: ")
        list_items = list(self.__player_portfolio.items())[1::]
        for stock in list_items:
            yield (f"Stock: {stock[0]}, Quantity: {stock[1]}")
    