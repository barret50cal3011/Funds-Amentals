from src.stocks_m.stock import Stock
import pdb as pd

class Player:
    def __init__(self, i_starting_USD: float) -> None:
        self.__player_portfolio: dict = {}
        self.__player_portfolio["USD"] = i_starting_USD
        self.__player_money_invested_in_stock_always: dict = {}
        self.__player_total_balance: dict = {}

    @property
    def player_money(self) -> float:
        """
        Returns the player's current money amount.

        Returns:
        float: The amount of money the player has.

        """
        return self.__player_portfolio["USD"]
    
   
    def get_player_money_invested_in_stock(self) -> float:
        """
        Returns a dictionary with stocks as keys and the amount of money the player has invested in each stock as values.

        Returns:
        dict: A dictionary where each key is a stock and each value is the amount of money invested in that stock.
        """
        return self.__player_money_invested_in_stock_always

    def get_player_balance(self) -> float:
        """
        Returns a dictionary with stocks as keys and the player's win/loss amount for each stock as values.

        Returns:
        dict: A dictionary where each key is a stock and each value is the player's win/loss amount for that stock.

        """

        return self.__player_total_balance

    def save_player_money_invested_in_stock(self, stock: Stock, quantity: int) -> None:
        """
        Saves the player's money invested and the balance in a specific stock (win/loss of money).

        Parameters:
        stock (Stock): The stock object that the player is going to buy.
        quantity (int): The number of stocks to buy.

        Returns:
        None
        """

        stock_price: float = stock.get_stock_price()
        investment: float = stock_price * quantity
        
        if stock not in self.__player_money_invested_in_stock_always:
            self.__player_money_invested_in_stock_always[stock] = 0
        self.__player_money_invested_in_stock_always[stock] += investment


        if stock not in self.__player_total_balance:
            self.__player_total_balance[stock] = 0
        self.__player_total_balance[stock] -= investment
                

    def validate_input_quantity(func):
        """
        Decorator that verifies if the quantity is an integer value greater than 0.

        Parameters:
        func (function): The function to be decorated.

        Returns:
        function: The wrapped function with input validation.
        """

        def wrapper(self, stock, quantity, *args, **kwargs):
            """
             Verifies if quantity is an instance of int and greater than 0.

            Parameters:
            stock: The stock object.
            quantity (int): The number of stocks.
            *args: Additional arguments for the function.
            **kwargs: Additional keyword arguments for the function.

            Returns:
            function: The original function if validation passes.
            """
            if not isinstance(quantity, int) and quantity > 0:
                raise ValueError("You should only input integers values greater than 0 for quantity")
            return func(self, stock, quantity, *args, **kwargs)
        
        return wrapper



    @validate_input_quantity
    def buy_stock(self, stock: Stock, quantity: int) -> None:
        """
        Allows the player to buy stocks of a specific company and updates the balance and money invested.

        Parameters:
        stock (Stock): The stock object that the player is going to buy.
        quantity (int): The number of stocks to buy.

        Returns:
        None
        """

        if(quantity * stock.get_stock_price() > self.__player_portfolio["USD"]):
            raise ValueError("Not enough USD to buy stock")
        if stock in self.__player_portfolio:
            self.__player_portfolio[stock] += quantity
            self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()

        else:
            self.__player_portfolio[stock] = quantity
            self.__player_portfolio["USD"] -= quantity * stock.get_stock_price()

        self.save_player_money_invested_in_stock(stock=stock, quantity=quantity)

        print(f"You have bought {quantity} stocks of {stock.get_company_name()}")



    @validate_input_quantity
    def sell_stock(self, stock: Stock, quantity: int) -> None:
        """
        Allows the player to sell stocks of a specific company and updates the balance accordingly.

        Parameters:
        stock (Stock): The stock object that the player is going to sell.
        quantity (int): The number of stocks to sell.

        Returns:
        None
        """
        stock_price = stock.get_stock_price()
        if stock in self.__player_portfolio and self.__player_portfolio[stock] >= quantity:
            self.__player_portfolio[stock] -= quantity
            sale_value: float = quantity * stock_price
            self.__player_portfolio["USD"] += sale_value
            if stock not in self.__player_total_balance:

                self.__player_total_balance[stock] = 0
            self.__player_total_balance[stock] += sale_value

            if self.__player_portfolio[stock] == 0:
                del self.__player_portfolio[stock]
            
            print(f"You have sell {quantity} stocks of {stock.get_company_name()}")
        else: 
            raise ValueError("Not enough stock to sell")


        
    def get_portfolio(self) -> dict:
        """
        Returns a dictionary with all stocks and their quantities, and the player's total money amount.

        Returns:
        dict: A dictionary where each key is a stock and each value is the quantity of that stock.

        """

        return self.__player_portfolio
    


    def print_generator(self, iterable):
        """
        Creates a generator that returns the keys and values of any dictionary for printing without the dict format.

        Yields:
        str: A formatted string representing the key-value pairs.

        """
        for gen_key, gen_value in iterable.items():
            if gen_key == "USD":
                yield f"Money in: {gen_key}, amount: {gen_value}"
            else:
                yield f"Company: {gen_key.get_company_name()}, amount: {gen_value}"
               

    def print_player_money_invested_in_stock(self) -> float:
        """
        Returns the player's money invested in a formatted way.

        Returns:
        str: A formatted string representing the player's money invested in stocks.
        """

        string: str = "Money invested in stock:\n"
        for x in self.print_generator(self.get_player_money_invested_in_stock()):
             string += x + "\n"
        return string

    def print_player_balance(self) -> float:
        """
        Returns the player's balance in a formatted way.

        Returns:
        str: A formatted string representing the player's balance.
        """

        if self.get_player_balance() != {}:
            string: str = "Your balance:\n"
            for x in self.print_generator(self.get_player_balance()):
                string += x + "\n" 
            return string
        else:
            return ("You have not sell any stock, so you have not win or loss money\n")
    
    def __str__(self):
        """
        Returns a formatted string representing the player's portfolio.

        Returns:
        str: A formatted string representing the player's portfolio.

        """

        string: str = "You have:\n"
        for x in self.print_generator(self.get_portfolio()):
             string += x + "\n"
        return string
