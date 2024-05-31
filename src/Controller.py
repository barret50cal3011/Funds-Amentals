from world import World

class Controller:

    def __init__(self):
        self.__world = World()

    def eval_comad(self, command):
        command_split = command.split(" ")
        if command_split[0] == "read_news":
            return self.__world.read_news()
        elif command_split[0] == "buy_stocks":
            return self.__world.buy_stock(command_split[1], int(command_split[2]))
        elif command_split[0] == "sell_socks":
            return self.__world.sell_stock(command_split[1], int(command_split[2]))
        elif command_split[0] == "next_week":
            pass