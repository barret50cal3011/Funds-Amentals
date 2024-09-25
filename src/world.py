import random
from typing import Optional
from events_m.events import Events
from stocks_m.stock import Stock
from Player import Player
from events_m.events_storer import EventsStorer
from newtimer import Time
from news import News

class World:

    def __init__(self, events:Optional[dict] = None, stocks:Optional[dict] = None, player:Optional[Player] = None):
        self.global_time = Time(start_date="2024-01-01")
        
        if events == None:
            self.__events:dict = self.load_events()
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
            
        self.news = News(self.__events) 

    def load_stocks(self) -> dict:
        stocks = {
            "Doors": Stock(300, "Doors", 0.5, 0.4, "Technology and software company, sells operating systems and software.", "Software", self.global_time),
            "Edison": Stock(650, "Edison", 0.6, 0.7, "Energy and electrical innovations company, sells electric vehicles and renewable energy solutions.", "Electricity", self.global_time),
            "Game pause": Stock(200, "Game pause", 0.7, 0.6, "Retail and gaming company, sells video games and gaming consoles.", "Retail", self.global_time),
            "ArabOilCompany": Stock(850, "ArabOilCompany", 0.4, 0.5, "Oil company, sells crude oil and petroleum products.", "Oil", self.global_time),
            "MVidia": Stock(500, "MVidia", 0.5, 0.5, "Semiconductor and GPU technology company, sells graphic processing units and AI chips.", "Technology", self.global_time),
            "Pear": Stock(700, "Pear", 0.4, 0.5, "Consumer electronics company, sells smartphones, tablets, and computers.", "Technology", self.global_time),
            "USWeapons": Stock(900, "USWeapons", 0.3, 0.6, "Defense and aerospace company, sells weapons systems and military aircraft.", "Defense", self.global_time)
        }
        return stocks

    def load_events(self) -> dict:
        '''
        event_son_first_w = Events("War", "Description", 5, (-5, 5), "Edison", "Electricity")
        events_son_two_w = Events("War", "Description", 5, (-5, 5), "Doors", "Software")
        events_son_two_T = Events("Technology Advances", "Description", 5, (-5, 5), "Doors", "Software")
        '''
        event_son_w_1 = Events("War", "Conflict affecting electricity sector", 365, (-15, -5), "Edison", "Electricity")
        event_son_w_2 = Events("War", "Conflict affecting software industry", 365, (3, 10), "Doors", "Software")
        event_son_w_3 = Events("War", "Conflict affecting consumer electronics", 365, (-10, -3), "Pear", "Technology")
        event_son_w_4 = Events("War", "Conflict affecting oil industry", 365, (5, 15), "ArabOilCompany", "Oil")
        event_son_w_5 = Events("War", "Conflict affecting defense sector", 365, (10, 20), "USWeapons", "Defense")
        event_son_w_6 = Events("War", "Conflict affecting retail and gaming", 365, (-15, -5), "Game pause", "Retail")
        event_son_w_7 = Events("War", "Conflict affecting semiconductor industry", 365, (5, 15), "MVidia", "Technology")
        
        event_son_a_1 = Events("Accident", "Accident affecting electricity infrastructure", 7, (-15, -5), "Edison", "Electricity")
        event_son_a_2 = Events("Accident", "Accident affecting software development", 7, (-10, -5), "Doors", "Software")
        event_son_a_3 = Events("Accident", "Accident affecting consumer electronics production", 7, (-10, -5), "Pear", "Technology")
        event_son_a_4 = Events("Accident", "Accident affecting oil production", 7, (-20, -10), "ArabOilCompany", "Oil")
        event_son_a_5 = Events("Accident", "Accident affecting defense supply chain", 7, (-10, -5), "USWeapons", "Defense")
        event_son_a_6 = Events("Accident", "Accident affecting gaming retail chain", 7, (-10, -5), "Game pause", "Retail")
        event_son_a_7 = Events("Accident", "Accident affecting semiconductor industry", 7, (-10, -5), "MVidia", "Technology")

        event_son_ta_1 = Events("Technology Advances", "Advances in electricity production", 60, (10, 20), "Edison", "Electricity")
        event_son_ta_2 = Events("Technology Advances", "Advances in software development", 60, (5, 15), "Doors", "Software")
        event_son_ta_3 = Events("Technology Advances", "Advances in consumer electronics", 60, (5, 15), "Pear", "Technology")
        event_son_ta_4 = Events("Technology Advances", "Advances in oil extraction technology", 60, (-10, -5), "ArabOilCompany", "Oil")
        event_son_ta_5 = Events("Technology Advances", "New defense systems", 60, (5, 15), "USWeapons", "Defense")
        event_son_ta_6 = Events("Technology Advances", "Breakthroughs in gaming technology", 60, (5, 20), "Game pause", "Retail")
        event_son_ta_7 = Events("Technology Advances", "New semiconductor technologies", 60, (10, 20), "MVidia", "Technology")

        event_son_nd_1 = Events("Natural Disasters", "Hurricane affecting electricity", 14, (-10, -5), "Edison", "Electricity")
        event_son_nd_2 = Events("Natural Disasters", "Earthquake affecting software infrastructure", 14, (-8, -3), "Doors", "Software")
        event_son_nd_3 = Events("Natural Disasters", "Flood affecting consumer electronics", 14, (-8, -3), "Pear", "Technology")
        event_son_nd_4 = Events("Natural Disasters", "Tornado affecting oil production", 14, (-15, -5), "ArabOilCompany", "Oil")
        event_son_nd_5 = Events("Natural Disasters", "Storm affecting defense logistics", 14, (-8, -3), "USWeapons", "Defense")
        event_son_nd_6 = Events("Natural Disasters", "Wildfire affecting retail sector", 14, (-10, -5), "Game pause", "Retail")
        event_son_nd_7 = Events("Natural Disasters", "Blizzard affecting semiconductor manufacturing", 14, (-8, -3), "MVidia", "Technology")

        event_son_sm_1 = Events("Social Media", "Social media buzz affecting electricity sector", 7, (-10, 10), "Edison", "Electricity")
        event_son_sm_2 = Events("Social Media", "Viral trends affecting software industry", 7, (-5, 5), "Doors", "Software")
        event_son_sm_3 = Events("Social Media", "New viral tech affecting consumer electronics", 7, (-5, 5), "Pear", "Technology")
        event_son_sm_4 = Events("Social Media", "Oil-related trends on social media", 7, (-5, 5), "ArabOilCompany", "Oil")
        event_son_sm_5 = Events("Social Media", "Defense industry discussed on social media", 7, (-5, 5), "USWeapons", "Defense")
        event_son_sm_6 = Events("Social Media", "Gaming trends going viral", 7, (-20, 20), "Game pause", "Retail")
        event_son_sm_7 = Events("Social Media", "Social media buzz about semiconductors", 7, (-5, 5), "MVidia", "Technology")

        
        dad_w = EventsStorer("War", [event_son_w_1, event_son_w_2,event_son_w_3,event_son_w_4,event_son_w_5,event_son_w_6,event_son_w_7])
        dad_a = EventsStorer("Accident", [event_son_a_1,event_son_a_2,event_son_a_3,event_son_a_4,event_son_a_5,event_son_a_6,event_son_a_7])
        dad_ta = EventsStorer("Technology Advances", [event_son_ta_1,event_son_ta_2,event_son_ta_3,event_son_ta_4,event_son_ta_5,event_son_ta_6,event_son_ta_7])
        dad_nd = EventsStorer("Natural Disasters", [event_son_nd_1,event_son_nd_2,event_son_nd_3,event_son_nd_4,event_son_nd_5,event_son_nd_6,event_son_nd_7])
        dad_sm = EventsStorer("Social Media", [event_son_sm_1,event_son_sm_2,event_son_sm_3,event_son_sm_4,event_son_sm_5,event_son_sm_6,event_son_sm_7])

        events = {dad_w: 0.05, dad_a: 0.25, dad_ta: 0.10,dad_nd: 0.30,dad_sm: 0.30}


        return events


    def get_not_reach_limit_storer(self) -> dict:
        return {k: v for k, v in self.__events.items() if not k.reach_limit()}
    
    def active_events_sons(self) -> list:
        return [k for k in self.__events.keys() if k.get_active_sons() != []]

    def verify_all_active(self) -> bool:
        filtred_events_not_reach_limit: dict = self.get_not_reach_limit_storer()
        return filtred_events_not_reach_limit == {}
    
    def posibility_active_event(self) -> bool:
        bools_list: list = [True, False]
        bool_weight: list = [0.4, 0.6]
        selected_bool: bool = random.choices(population = bools_list, weights = bool_weight, k=1)
        return selected_bool[0]
    

    def create_event(self) -> None:

        if self.verify_all_active() == False:
            filtred_events_not_reach_limit: dict = self.get_not_reach_limit_storer()

            father_events: list = list(filtred_events_not_reach_limit.keys())
            weight: list = list(filtred_events_not_reach_limit.values())

            selected_father_event: EventsStorer = random.choices(population = father_events, weights = weight, k=1)
                
            selected_father_event.active_sons()



    def calculate_percentage(self) -> dict:
        fathers_with_active_sons: list = self.active_events_sons()
        
        if fathers_with_active_sons != []:   
            percentage_event: dict = {}

            for father_event in fathers_with_active_sons:
                active_sons: list = father_event.get_active_sons()

                for active_event in active_sons:
                    affected_stock: str = active_event.get_affected_stock()

                    if affected_stock not in percentage_event:
                        percentage_event[affected_stock] = 0

                    percentage_active_event: float = active_event.get_percentage()
                    percentage_event[affected_stock] += percentage_active_event

            return percentage_event
        

    def pass_percentage_to_stocks(self) -> None:
        percentage: dict = self.calculate_percentage()
        stocks_dict: dict = self.__stocks

        for stock in stocks_dict:
            if stock in percentage:
                percentage_of_stock: float = percentage[stock]
                stock_will_be_affeccted: Stock = stocks_dict.get(stock)
                stock_will_be_affeccted.update_stock_price(percentage=percentage_of_stock)
            else:
                raise ValueError("Something happen when passing percentage to stocks")


    def desactive_event(self) -> None:
        fathers_with_active_sons: list = self.active_events_sons()
        if fathers_with_active_sons != []:
            for storer in fathers_with_active_sons:
                storer.desactive_sons()
            self.pass_percentage_to_stocks()


    def run(self):
        timer = 0
        while timer < 10:
            self.create_event()
            timer += 1 
        
    def show_news(self):
        print("Generating news headlines...")
        headlines = self.news.get_news_titles()
        if headlines:
            for headline in headlines:
                print(headline)
        else:
            print("No headlines available.")

            
    def read_news(self, event_name: Optional[str] = None):
        if event_name:
            article = self.news.get_news_article(event_name)
            event = self.__events.get(event_name)
            if event:
                affected_stock = event.affected_stock
            else:
                affected_stock = "No specific stock affected."
                
            if article:
                print(f"Article for {event_name}:\n{article}\nAffected Stock: {affected_stock}")
            else:
                print(f"No articles available for the event: {event_name}")
        else:
            self.show_news()



    def buy_stock(self, stock_name, amount):
        stock = self.__stocks[stock_name]
        self.__player.buy_stock(stock, amount)


    def sell_stock(self, stock_name, amount):
        stock = self.__stocks[stock_name]
        self.__player.sell_stock(stock, amount)


    def next_week(self):
        self.create_event()


    def see_portfolio(self):
        return self.__player.get_portfolio()

    def see_market(self):
        stock_prices = {}
        for stock in self.__stocks:
            price = self.__stocks[stock].get_stock_price()
            stock_prices[stock] = price
        return stock_prices
    

    def candle_stick(self, stock_name):
        stock = self.__stocks[stock_name]
        stock.candlestick() 

 
if __name__ == '__main__':
    stocks_list = [Stock(100.0, "Edison"), Stock(150.0, "ArabOilCompany"),Stock(100.0, "USWeapons"),Stock(100.0, "GamePause"),Stock(100.0, "Doors"),Stock(100.0, "Mvidia"),Stock(100.0, "Pear"),]
    player = Player(i_starting_USD=1000.0)
    events=None
    world = World(events, stocks_list, player)
    world.run()