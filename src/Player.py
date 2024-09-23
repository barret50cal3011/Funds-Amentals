from src.stocks_m.stock import Stock

class Player:
    def __init__(self, i_starting_USD: float) -> None:
        self.__player_portfolio: dict = {}
        self.__player_portfolio["USD"] = i_starting_USD
        self.__player_money_invested_in_stock: dict = {"Edison": 0, "ArabOilCompany": 0, "Doors":  0, "GamePause":  0, "Mvidia":  0, "Pear":  0, 'USWeapons':  0}
        self.__player_balance: dict = {"Edison": 0, "ArabOilCompany": 0, "Doors":  0, "GamePause":  0, "Mvidia":  0, "Pear":  0, 'USWeapons':  0}

    # Will show the amount of money the player has directly
    @property
    def player_money(self) -> float:
        return self.__player_portfolio["USD"]
    
   
    # Will help to show the amount of money the player has earn or loss
    def get_player_money_invested_in_stock(self, stock: Stock) -> float:
        stock_name = stock.get_company_name()
        return self.__player_money_invested_in_stock.get(stock_name, 0)

    # Returns the money that the player profit/loss along the time for each company 
    def get_player_balance(self, stock: Stock) -> float:
        stock_name = stock.get_company_name()
        return self.__player_balance.get(stock_name, 0)

    # Will save the invest of each company in player_money_invested_in_stock
    def save_player_money_invested_in_stock(self, stock: Stock, quantity: int) -> None:
            stock_name = stock.get_company_name()
            stock_price = stock.get_stock_price()
            investment = stock_price * quantity
            
            if stock_name not in self.__player_money_invested_in_stock:
                self.__player_money_invested_in_stock[stock_name] = 0
            
            self.__player_money_invested_in_stock[stock_name] += investment


    # Will restart the value of each company in player_money_invested_in_stock if the player solds all the stocks
    def del_player_money_invested_in_stock(self, stock: Stock) -> None:
            stock_name = stock.get_company_name()            
            if stock_name in self.__player_money_invested_in_stock:
                self.__player_money_invested_in_stock[stock_name] = 0

    # Save the info of profits / loss in __player_balance for each company
    def calculate_balance(self, stock_name: str, sale_value: float) -> None:
        stock_name: str = stock_name
        sale_value: float = sale_value
        investment: float = self.__player_money_invested_in_stock.get(stock_name, 0)
        if investment > 0:
            profit_or_loss = sale_value - investment
            if stock_name not in self.__player_balance:
                self.__player_balance[stock_name] = 0
            self.__player_balance[stock_name] += profit_or_loss

    # Validate that quatity is an int value    
    def validate_input_quantity(func):
        def wrapper(self, stock, quantity, *args, **kwargs):
            if not isinstance(quantity, int) and quantity > 0:
                raise ValueError("You should only input integers values greater than 0 for quantity")
            return func(self, stock, quantity, *args, **kwargs)
        return wrapper

    # Will let the player buy stocks for each company
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

        self.save_player_money_invested_in_stock(stock=stock, quantity=quantity)

    # Will let the player sell stocks for each company
    @validate_input_quantity
    def sell_stock(self, stock: Stock, quantity: int) -> None:
        stock_name = stock.get_company_name()
        stock_price = stock.get_stock_price()
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            sale_value = quantity * stock_price
            self.__player_portfolio["USD"] += sale_value

            self.calculate_balance(stock_name = stock_name, sale_value = sale_value)

            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]

                self.del_player_money_invested_in_stock()
        else: 
            raise ValueError("Not enough stock to sell")

    # Show the player the stock amount of a specific stock company
    def get_stock_amount(self, stock: Stock) -> int:
        if stock in self.__player_portfolio:
            return self.__player_portfolio[stock]
        else:
            return 0
        
    # Show the player the stock amount of all stocks company    
    def get_portfolio(self) -> dict:
        return self.__player_portfolio
    
    # When uses print will show all the portfolio of the player
    def __str__(self):
        print("You have bought: ")
        list_items = list(self.__player_portfolio.items())[1::]
        for stock in list_items:
            yield (f"Stock: {stock[0]}, Quantity: {stock[1]}")
    