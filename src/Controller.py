import textwrap
from world import World

class Controller:

    def __init__(self):
        self.__world = World()

    def eval_command(self, command):
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
            market = self.__world.see_market()
            market_str = "Current market status:\n"
            for stock in market:
                market_str += f"{stock} : {market[stock]}\n"
            return market_str