from world import World

class Controller:

    def __init__(self):
        self.__world = World()

    def eval_comad(self, command):
        command_split = command.split(" ")
        if command_split[0] == "read_news":
            return self.__world.read_news()
        elif command_split[0] == "buy_stock":
            pass
        elif command_split[0] == "next_week":
            pass