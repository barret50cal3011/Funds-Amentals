from events import events, create_event
from stocks.stock import Stock
from Player import Player
import random

class World:
    def __init__(self, events = None, stocks = None, player = None):
        self.__events = events
        self.__stocks = stocks
        self.__player = player

    def run(self):
        timer = 0
        while timer < 10:
            random_event_name = create_event()
            random_event = self.__events.get(random_event_name)
            random_event.change_state()

            if random_event.get_state() == "Active":
                random_event.set_percentage(random.uniform(-5, 5))
                random_event.affect_stocks(self.__stocks)

            print(f"{random_event_name} is {random_event.get_state()}",
                  f"\nDescription: {random_event.get_description()}",
                  f"\nImpact: {random_event.get_percentage()}%",
                  "\n")

            for stock in self.__stocks:
                print(f"{stock.company_name} stock price: {stock.get_stock_price()}")

            timer += 1


    def read_news(news = None):
        return "this is a news!!!"
    

    def buy_stock(self, stock_name, amount):
        pass

    def next_week(self):
        random_event_name = create_event()
        random_event = self.__events.get(random_event_name)
        random_event.change_state()

        if random_event.get_state() == "Active":
            random_event.set_percentage(random.uniform(-5, 5))
            random_event.affect_stocks(self.__stocks)

if __name__ == '__main__':
    stocks_list = [Stock(100.0, "ABC Corp"), Stock(150.0, "XYZ Inc")]
    player = Player(starting_usd=1000.0)
    world = World(events, stocks_list, player)
    world.run()
