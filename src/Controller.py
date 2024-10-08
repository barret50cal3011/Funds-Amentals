import textwrap
from world import World

class Controller:
    """
    The Controller class acts as an intermediary between the View and the World.
    It evaluates user commands and invokes corresponding methods on the World instance.
    """
    def __init__(self):
        self.__world = World()

    def eval_command(self, command):
        """
        Evaluates the given command and calls the appropriate method on the World instance.
        
        :param command: A string containing the user command to evaluate.
        :return: The result of the executed command, if applicable.
        :raises Exception: If the command is improperly formatted or has missing parameters.
        """
        command_split = command.split(" ")
        if command_split[0] == "read_news":
            if(len(command_split) == 1):
                return self.__world.read_news()
            else:
                self.__world.read_news(command_split[1])
        elif command_split[0] == "buy_stock":
            if len(command_split) < 3 or command_split[1].isdigit() or not command_split[2].isdigit():
                raise Exception(textwrap.dedent(
                    """
                    buy_stocks command requiers a stock name and an amount of stocks you are going to buy. 
                    buy_stock <name> <amount>.
                    name must be a string and amount a number
                    """
                    ))
            return self.__world.buy_stock(command_split[1], int(command_split[2]))
        elif command_split[0] == "sell_stock":
            if len(command_split) < 3:
                raise Exception(textwrap.dedent(
                    """
                    sell_stocks command requiers a stock name and an amount of stocks you are going to sell. 
                    sell_stock <name> <amount>.
                    name must be a non digit string and amount a number
                    """
                    ))
            return self.__world.sell_stock(command_split[1], int(command_split[2]))
        elif command_split[0] == "next_week":
            self.__world.next_week()
            return "You are going to the next week."
        elif command_split[0] == "see_portfolio":
            portfolio = self.__world.see_portfolio()
            return portfolio
        elif command_split[0] == "see_market":
            if len(command_split) == 1:
                market = self.__world.see_market()
                market_str = "Current market status:\n"
                for stock in market:
                    market_str += f"{stock} : {market[stock]}\n"
                return market_str
            elif len(command_split) == 2:
                return self.__world.candle_stick(command_split[1])
            
        elif command_split[0] == "see_balance":
            return self.__world.see_balance()
            