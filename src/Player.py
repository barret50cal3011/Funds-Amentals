from src.stocks_m.stock import Stock

class Player:
    def __init__(self, i_starting_USD: float) -> None:
        self.__player_portfolio: dict = {}
        self.__player_portfolio["USD"] = i_starting_USD
        self.__player_money_invested_in_stock: dict = {}
        self.__player_balance: dict = {}

    # Will show the amount of money the player has directly
    @property
    def player_money(self) -> float:
        return self.__player_portfolio["USD"]
    
   
    # Will help to returns the amount of money the player has earn or loss
    def get_player_money_invested_in_stock(self) -> float:
        return self.__player_money_invested_in_stock

    # Returns the money that the player profit/loss along the time for each company 
    def get_player_balance(self) -> float:
        return self.__player_balance

    # Will save the invest of each company in player_money_invested_in_stock
    def save_player_money_invested_in_stock(self, stock: Stock, quantity: int) -> None:
            stock_price = stock.get_stock_price()
            investment = stock_price * quantity
            
            if stock not in self.__player_money_invested_in_stock:
                self.__player_money_invested_in_stock[stock] = 0
            
            self.__player_money_invested_in_stock[stock] += investment


    # Will restart the value of each company in player_money_invested_in_stock if the player solds all the stocks
    def del_player_money_invested_in_stock(self, stock: Stock) -> None:
            if stock in self.__player_money_invested_in_stock:
                self.__player_money_invested_in_stock[stock] = 0

    # Save the info of profits / loss in __player_balance for each company
    def calculate_balance(self, stock: str, sale_value: float) -> None:
        sale_value: float = sale_value
        investment: float = self.__player_money_invested_in_stock.get(stock, 0)
        if investment > 0:
            profit_or_loss = sale_value - investment
            if stock not in self.__player_balance:
                self.__player_balance[stock] = 0
            self.__player_balance[stock] += profit_or_loss

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
        stock_price = stock.get_stock_price()
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            sale_value = quantity * stock_price
            self.__player_portfolio["USD"] += sale_value

            self.calculate_balance(stock = stock, sale_value = sale_value)

            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]

                self.del_player_money_invested_in_stock(stock=stock)
        else: 
            raise ValueError("Not enough stock to sell")


        
    # Show the player the stock amount of all stocks company    
    def get_portfolio(self) -> dict:
        return self.__player_portfolio
    
    def print_generator(self, iterable):
        for gen_key, gen_value in iterable.items():
            if type(gen_key) != str:
                yield f"Company: {gen_key.get_company_name()}, amount: {gen_value}"
            else:
                yield f"Company: {gen_key}, amount: {gen_value}"

    # Will help to show the amount of money the player has earn or loss
    def print_player_money_invested_in_stock(self) -> float:
        string:str = "Money invested in stock:\n"
        for x in self.print_generator(self.get_player_money_invested_in_stock()):
             string += x + "\n"
        return string

    # Returns the money that the player profit/loss along the time for each company 
    def print_player_balance(self) -> float:
        string:str = "Your balance:\n"
        for x in self.print_generator(self.get_player_balance()):
             string += x + "\n"
        return string

    
    # When uses print will show all the portfolio of the player
    def __str__(self):
        string: str = "You have:\n"
        for x in self.print_generator(self.get_portfolio()):
             string += x + "\n"
        return string
