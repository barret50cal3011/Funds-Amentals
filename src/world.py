import random
from typing import Optional
from src.events_m.events import Events
from stocks_m.stock import Stock
from Player import Player
from src.events_m.events_storer import EventsStorer


class World:

    def __init__(self, events:Optional[dict] = None, stocks:Optional[dict] = None, player:Optional[Player] = None):
        if events == None:
            self.__events:dict = events.load_events()
        else:
            self.__events = events

        if stocks == None:
            self.__stocks:dict = self.load_stocks()
        else:
            self.__stocks = stocks
        
        if player == None:
            self.__player:Player = Player(i_starting_USD=100000)
        else:
            self.__player = player


    def load_stocks(self):
        stocks = {
            "Doors" : Stock(300, "Doors", 0.5, 0.5, "Description", "Software"),
            "Edison" : Stock(400, "Edison", 0.5, 0.5, "Description", "Electricity")
        }
        return stocks

    def load_events(self):
        event_son_first_w = Events("War", "Description", 5, (-5, 5), "Edison", "Electricity")
        events_son_two_w = Events("War", "Description", 5, (-5, 5), "Doors", "Software")
        events_son_two_T = Events("Technology Advances", "Description", 5, (-5, 5), "Doors", "Software")

        dad_w = EventsStorer("War", [event_son_first_w, events_son_two_w])
        dad_t = EventsStorer("Technology Advances", [events_son_two_T])

        events = {"Random": [{dad_w: 0.40}, {dad_t: 0.60}]}


        return events


# ______________________________________________________________________________________________________________________________________
# ! will be eliminate and add to world

# def create_event()->str:
#   verificator:bool = True
#   events_list:list = ["War", "Technology Advances", "Accident", 
#                     "Seasons", "Natural Disasters", "Social Media"]  
  
#   while verificator:
#     random_event:str = random.choice(events_list)
#     if events.get(random_event).get_state() == "Inactive":
#       verificator:bool = False
#       events.get(random_event).state_activer()
#       return random_event
    
# ! will be eliminate and add to world
# def all_events_active():
#   for event in events.values():
#     if event.get_state() == "Inactive":
#       return False
#   return True

# ! will be eliminate and add to world
# def desactivate_event()->None:
#   for event in events.values():
#     if event.get_state() == "Active":
#       event.state_desactiver()
#       event.change_percentage()
#       event.change_impact()




    def run(self):
        timer = 0
        while timer < 20:
            random_event_name = create_event()
            random_event = self.__events.get(random_event_name)
            
            if not all_events_active():
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
        

        if random_event.get_state() == "Active":
            random_event.set_percentage(random.uniform(-5, 5))
            random_event.affect_stocks(self.__stocks)
        
        self.__current_event = random_event


    def see_portfolio(self):
        return self.__player.get_portfolio()


if __name__ == '__main__':
    stocks_list = [Stock(100.0, "Edison"), Stock(150.0, "ArabOilCompany"),Stock(100.0, "USWeapons"),Stock(100.0, "GamePause"),Stock(100.0, "Doors"),Stock(100.0, "Mvidia"),Stock(100.0, "Pear"),]
    player = Player(i_starting_USD=1000.0)
    world = World(events, stocks_list, player)
    world.run()
