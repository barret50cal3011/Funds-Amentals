import os
import sys
import textwrap
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Controller import Controller


class View:
    """
    The View class handles user interaction and command processing for the stock market game.
    It displays available commands and their descriptions, accepts user input, 
    and communicates with the Controller to execute commands.
    """

    hlp = textwrap.dedent(
        """
        help [name of a command]
        read_news
        buy_stock <name of the company> <amount of stocks>
        sell_stock <name of the company> <amount of stocks>
        see_portfolio
        next_week
        see_market
        see_balance
        exit
        """
    )


    COMMANDS = {
        "help": 
        """
        help [command]. 
        writes a list of commands if no command is given.
        If a command is given, it prints a description of the command that was given(just like this one).
        When using this command <> means that it is obligatory to add the information for the funtionality of the command and [] means that it is optional.
        """,
        "read_news": 
        """
        read_news
        prints a list of the events that are ocurring at that week.
        If a tittle is added the command prints the news article of the news that was selencted.
        """,
        "buy_stock": 
        """
        buy_stock <company name> <stock amount>
        If the money is abailable, buys the amount of stocks of the company specified.
        """,
        "sell_stock": 
        """
        sell_stock <company name> <amount>
        If the amount of stocks are abailable, sells the stock to the current price.
        """,
        "see_portfolio": 
        """
        see_portfolio
        prints the information of the player's portfolio.
        """,
        "next_week": 
        """
        next_week
        advance the game to the next week.
        """,
        "see_market":
        """
        see_market [stock name]
        Shows the market and the prices of the stocks.
        If a name is given, it shows the candle stick of the stock.
        """
        ,
        "see_balance":
        """
        see_balance 
        Shows the player balance (if win or loss money) for all stocks he has bought.
        """
        ,
        "exit": 
        """
        exit
        Exits the game.
        Save is currentlly not implemented so progres on the game will be lost.
        """
    }


    def __init__(self):
        self.controler = Controller()


    def read(self):
        """
        Reads a command from the user input and processes it.
        Validates the command and executes it via the Controller. 
        Displays appropriate feedback or error messages based on the command outcome.
        
        :return: -1 if the exit command is issued, otherwise None.
        """
        command = input()
        if not command.split(" ")[0] in self.COMMANDS:
            print("Command not recognized.\nUse help to see the commands\n")
        elif command.split(" ")[0] == "help":
            if len(command.split(" ")) == 1:
                print(self.hlp)
                
            else:
                command_split = command.split(" ")[1]
                print("command")
                if command_split in self.COMMANDS:
                    print(textwrap.dedent(self.COMMANDS[command_split]))
                else:
                    print(f"command {command_split} not recognized.")
                #TODO
        elif command == "exit":
            print("Thanks for playing")
            time.sleep(5)
            return -1
        else:
            try: 
                print(self.controler.eval_command(command))
            except Exception as e:
                print(str(e))


    def run(self):
        """
        Runs the main loop of the game, prompting the user for commands until they decide to exit.
        Displays a welcome message and instructions for using the commands.
        """
        print("Welcome to the stock market game.\nType help for a list of commands.\n")
        while(self.read() != -1):
            pass