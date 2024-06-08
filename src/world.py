
from events import events, create_event
from stocks.stock import Stock
from Player import Player
from stocks.doors import Doors
from stocks.edison import Edison
import random

class World:

    def __init__(self, events = None, stocks = None, player = None):
        if events == None:
            self.__events = events
        else:
            self.__events = events

        if stocks == None:
            self.__stocks = self.load_stocks()
        else:
            self.__stocks = stocks
        
        if player == None:
            self.__player = Player(i_starting_USD=100000)
        else:
            self.__player = player


    def load_stocks(self):
        stocks = {
            "Doors" : Doors(300),
            "Edison" : Edison(400)
        }
        return stocks


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


    def read_news(news = None):
        if(news != None):
            #TODO: If news is none, the method returns a list of news tittles 
            pass
        else:
            #TODO: f news is true the method returns a the article of the news n question
            pass
        return "this is a news!!!"
    

    def buy_stock(self, stock_name, amount):
        stock = self.__stocks[stock_name]
        self.__player.buy_stock(stock, amount)


    def sell_stock(self, stock_name, amount):
        stock = self.__stocks[stock_name]
        self.__player.sell_stock(stock, amount)


    def next_week(self):
        random_event_name = create_event()
        random_event = self.__events.get(random_event_name)
        random_event.change_state()

        if random_event.get_state() == "Active":
            random_event.set_percentage(random.uniform(-5, 5))
            random_event.affect_stocks(self.__stocks)
        
        self.__current_event = random_event


    def see_portfolio(self):
        return self.__player.get_portfolio()


if __name__ == '__main__':
    stocks_list = [Stock(100.0, "Edison"), Stock(150.0, "ArabOilCompany"),Stock(100.0, "USWeapons"),Stock(100.0, "GamePause"),Stock(100.0, "Doors"),Stock(100.0, "Mvidia"),Stock(100.0, "Pear"),]
    player = Player(starting_usd=1000.0)
    world = World(events, stocks_list, player)
    world.run()
