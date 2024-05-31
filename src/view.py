import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Controller import Controller
class View:

    COMMANDS = {
        "help",
        "read_news",
        "buy_stock",
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
            print(self.COMMANDS)
        elif command == "exit":
            return -1
        else:
            print(self.controler.eval_comad(command))


    def run(self):
        while(self.read() != -1):
            pass