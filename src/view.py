import os
import sys
import textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Controller import Controller


class View:

    hlp = textwrap.dedent(
        """
        help [name of a command]
        read_news
        buy_stocks <name of the company> <amount of stocks>
        sell_stocks <name of the company> <amount of stocks>
        see_portfolio
        next_week
        exit
        """
    )


    COMMANDS = {
        "help": 
        textwrap.dedent("""
        help [command]. 
        writes a list of commands if no command is given.
        If a command is given, it prints a description of the command that was given(just like this one).
        When using this command <> means that it is obligatory to add the information for the funtionality of the command and [] means that it is optional.
        """),
        "read_news [News tittle]": 
        textwrap.dedent("""
        read_news
        prints a list of the events that are ocurring at that week.
        If a tittle is added the command prints the news article of the news that was selencted.
        """),
        "buy_stocks": 
        textwrap.dedent("""
        buy_stock <company name> <stock amount>
        If the money is abailable, buys the amount of stocks of the company specified.
        """),
        "sell_stocks": 
        textwrap.dedent("""
        sell_stock <company name> <amount>
        If the amount of stocks are abailable, sells the stock to the current price.
        """),
        "see_portfolio": 
        textwrap.dedent("""
        see_portfolio
        prints the information of the player's portfolio.
        """),
        "next_week": 
        textwrap.dedent("""
        next_week
        advance the game to the next week.
        """),
        "exit": 
        textwrap.dedent("""
        exit
        Exits the game.
        Save is currentlly not implemented so progres on the game will be lost.
        """)
    }


    def __init__(self):
        self.controler = Controller()


    def read(self):
        command = input()
        if not command.split(" ")[0] in self.COMMANDS:
            print("Command not recognised.")
        elif command == "help":
            if len(command.split(" ")) == 1:
                print(self.hlp)
            else:
                command = command.split(" ")[1]
                if command in self.COMMANDS:
                    print(self.COMMANDS[command.split(" ")[1]])
                else:
                    print(f"comand {command} not recognized.")
                #TODO
        elif command == "exit":
            return -1
        else:
            try: 
                print(self.controler.eval_comad(command))
            except Exception as e:
                print(str(e))


    def run(self):
        while(self.read() != -1):
            pass