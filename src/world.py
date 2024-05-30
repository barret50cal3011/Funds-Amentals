from events import events, create_event
from stocks import Stock
from Player import Player
import random

class World:
    def __init__(self, events, stocks, player):
        self.events = events
        self.stocks = stocks
        self.player = player

    def run(self):
        timer = 0
        while timer < 10:
            random_event_name = create_event()
            random_event = self.events.get(random_event_name)
            random_event.change_state()

            if random_event.get_state() == "Active":
                random_event.set_percentage(random.uniform(-5, 5))
                random_event.affect_stocks(self.stocks)

            print(f"{random_event_name} is {random_event.get_state()}",
                  f"\nDescription: {random_event.get_description()}",
                  f"\nImpact: {random_event.get_percentage()}%",
                  "\n")

            for stock in self.stocks:
                print(f"{stock.company_name} stock price: {stock.get_stock_price()}")

            timer += 1

if __name__ == '__main__':
    stocks_list = [Stock(100.0, "ABC Corp"), Stock(150.0, "XYZ Inc")]
    player = Player(starting_usd=1000.0)
    world = World(events, stocks_list, player)
    world.run()
