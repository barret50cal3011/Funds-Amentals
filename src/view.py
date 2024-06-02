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
        "help",
        "read_news",
        "buy_stocks",
        "sell_stocks",
        "see_portfolio",
        "next_week",
        "exit"
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
                print("Not implemented")
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