import random
from typing import Optional
from src.events_m.events import Events
from src.stocks_m.stock import Stock
from src.Player import Player
from src.events_m.events_storer import EventsStorer
from src.newtimer import Time
from src.news import News

import pdb

class World:

    def __init__(self, events:Optional[dict] = None, stocks:Optional[dict] = None, player:Optional[Player] = None):
        self.time_doors = Time(start_date="2024-01-01")
        self.time_edison = Time(start_date="2024-01-01")
        self.time_game_pause = Time(start_date="2024-01-01")
        self.time_araboilcompany = Time(start_date="2024-01-01")
        self.time_mvidia = Time(start_date="2024-01-01")
        self.time_pear = Time(start_date="2024-01-01")
        self.time_usweapons = Time(start_date="2024-01-01")
        
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
        
        for stock in self.__stocks:
            for i in range(15):
                self.__stocks[stock].stock_price_variation() 

        for stock in self.__stocks:
            for i in range(15):
                self.__stocks[stock].stock_price_variation()


    def load_stocks(self) -> dict:
        """
        This function `load_stocks` creates a dictionary of Stock objects representing various companies with their respective attributes.
        :return: The `load_stocks` method returns a dictionary containing information about various stocks. Each stock is represented by a key-value pair in the dictionary, where the key is the stock name and the value is an instance of the `Stock` class with specific attributes such as price, symbol, growth rate, dividend yield, description, sector, and time data.
        """
        stocks = {
            "Doors": Stock(300, "Doors", 0.5, 0.4, "Technology and software company, sells operating systems and software.", "Software", self.time_doors),
            "Edison": Stock(650, "Edison", 0.6, 0.7, "Energy and electrical innovations company, sells electric vehicles and renewable energy solutions.", "Electricity", self.time_edison),
            "Game pause": Stock(200, "Game pause", 0.7, 0.6, "Retail and gaming company, sells video games and gaming consoles.", "Retail", self.time_game_pause),
            "ArabOilCompany": Stock(850, "ArabOilCompany", 0.4, 0.5, "Oil company, sells crude oil and petroleum products.", "Oil", self.time_araboilcompany),
            "MVidia": Stock(500, "MVidia", 0.5, 0.5, "Semiconductor and GPU technology company, sells graphic processing units and AI chips.", "Technology", self.time_mvidia),
            "Pear": Stock(700, "Pear", 0.4, 0.5, "Consumer electronics company, sells smartphones, tablets, and computers.", "Technology", self.time_pear),
            "USWeapons": Stock(900, "USWeapons", 0.3, 0.6, "Defense and aerospace company, sells weapons systems and military aircraft.", "Defense", self.time_usweapons)
        }
        return stocks

    def load_events(self) -> dict:
        """
        The function `load_events` creates and stores different types of events related to wars, accidents, technology advances, natural disasters, and social media, along with their respective probabilities.
        :return: The `load_events` function returns a dictionary where the keys are instances of `EventsStorer` class representing different categories of events (War, Accident, Technology Advances, Natural Disasters, Social Media) and the values are floating-point numbers representing the weights assigned to each category.
        """
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
        """
        This function returns a dictionary of events that have not reached their limit.
        :return: A dictionary containing key-value pairs from the `self.__events` dictionary where the key does not reach its limit.
        """
        return {k: v for k, v in self.__events.items() if not k.reach_limit()}
    
    def active_events_sons(self) -> list:
        """
        This function returns a list of events that have active sons.
        :return: The `active_events_sons` method returns a list of events from the `self.__events` dictionary where the event has active sons (children) associated with it. The method filters out events that do not have any active sons by checking if the result of calling the `get_active_sons()` method on the event is not an empty list.
        """
        return [k for k in self.__events.keys() if k.get_active_sons() != []]

    def verify_all_active(self) -> bool:
        """
        The function `verify_all_active` checks if all events have reached their limit.
        :return: The `verify_all_active` method is returning a boolean value. It checks if the dictionary `filtred_events_not_reach_limit` is empty by comparing it to an empty dictionary `{}`. If the dictionary is empty, it will return `True`, indicating that all events are active. If the dictionary is not empty, it will return `False`, indicating that there are events that have not reached
        """
        filtred_events_not_reach_limit: dict = self.get_not_reach_limit_storer()
        return filtred_events_not_reach_limit == {}
    
    def posibility_active_event(self) -> bool:
        """
        This function randomly selects a boolean value based on specified weights and returns it.
        :return: The function `posibility_active_event` returns a randomly selected boolean value based on the weights provided in the `bool_weight` list.
        """
        bools_list: list = [True, False]
        bool_weight: list = [0.4, 0.6]
        selected_bool: bool = random.choices(population = bools_list, weights = bool_weight, k=1)
        return selected_bool[0]
    

    def create_event(self) -> None:
        """
        This function creates a new event if not all events have reached their limit.
        It selects a random parent event from those that have not reached their limit
        and activates its active sons (child events).
        """

        if self.verify_all_active() == False:
            filtred_events_not_reach_limit: dict = self.get_not_reach_limit_storer()

            father_events: list = list(filtred_events_not_reach_limit.keys())
            weight: list = list(filtred_events_not_reach_limit.values())

            selected_father_event: EventsStorer = random.choices(population = father_events, weights = weight, k=1)[0]
                
            selected_father_event.active_sons()



    def calculate_percentage(self) -> dict:
        """
        This function calculates the total percentage impact of active son events 
        on their respective stocks. It aggregates the percentages of each active son 
        event associated with each stock.

        :return: A dictionary where the keys are stock names and the values are the 
                total percentage impacts from the active son events.
        """
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
        """
        This function updates the stock prices based on the calculated percentage impacts 
        from active events. It retrieves the percentage impacts and applies them to each 
        corresponding stock's price.
        """
        percentage: dict = self.calculate_percentage()
        stocks_dict: dict = self.__stocks
        for stock in stocks_dict:
            if stock in percentage:
                percentage_of_stock: float = percentage[stock]
                stock_will_be_affeccted: Stock = stocks_dict.get(stock)
                stock_will_be_affeccted.update_stock_price(percentage=percentage_of_stock)


    def desactive_event(self) -> None:
        """
        This function deactivates all active son events of parent events that have active sons.
        After deactivating these events, it updates the stock prices based on the impacts 
        calculated from the deactivated events.
        """
        fathers_with_active_sons: list = self.active_events_sons()
        if fathers_with_active_sons != []:
            for storer in fathers_with_active_sons:
                storer.desactive_sons()
            self.pass_percentage_to_stocks()




    def run(self):
        """
        The `run` method is responsible for executing the main game loop for a specified duration.
        It simulates the passage of time in weeks and allows for the creation and deactivation of events.
        """
        
        timer = 0
        while timer < 1000:
            self.next_week()
            # hi = input("y or n")
            # if hi == "y":
            #     pass
            timer += 1 




    def show_news(self):
        """
        This function generates and displays news headlines related to the events in the game.
        If there are no headlines available, it informs the user accordingly.
        """
        print("Generating news headlines...")
        headlines = self.news.get_news_titles()
        if headlines:
            for headline in headlines:
                print(headline)
        else:
            print("No headlines available.")

            
    def read_news(self, event_name: Optional[str] = None):
        """
        This function retrieves and displays the news article for a specified event.
        If no event name is provided, it shows the latest news headlines.
        
        :param event_name: Optional; the name of the event to retrieve the article for.
        """
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
        """
        This function allows the player to buy a specified amount of shares for a given stock.
        
        :param stock_name: The name of the stock to purchase.
        :param amount: The number of shares to buy.
        """
        stock = self.__stocks[stock_name]
        self.__player.buy_stock(stock, amount)


    def sell_stock(self, stock_name, amount):
        """
        This function allows the player to sell a specified amount of shares for a given stock.
        
        :param stock_name: The name of the stock to sell.
        :param amount: The number of shares to sell.
        """
        stock = self.__stocks[stock_name]
        self.__player.sell_stock(stock, amount)


    def next_week(self):
        """
        This function simulates the passage of one week in the game.
        It updates stock prices, progresses time, deactivates events, and creates new events.
        """
        for stock in self.__stocks:
            for i in range(7):
                self.__stocks[stock].stock_price_variation()
        self.time_doors.get_next_date()
        self.desactive_event()
        self.create_event()

    def see_portfolio(self):
        """
        This function returns the player's stock portfolio.
        
        :return: A dictionary representing the player's portfolio with stock holdings.
        """
        return self.__player.get_portfolio()

    def see_market(self):
        """
        This function provides the current stock prices for all available stocks in the market.
        
        :return: A dictionary containing the stock names and their current prices.
        """
        stock_prices = {}
        for stock in self.__stocks:
            stock_prices[stock] = self.__stocks[stock].get_stock_price()
        return stock_prices
    

    def candle_stick(self, stock_name):
        """
        This function generates and displays a candlestick chart for the specified stock.
        
        :param stock_name: The name of the stock for which to generate the candlestick chart.
        """
        stock = self.__stocks[stock_name]
        stock.candlestick() 

 
if __name__ == '__main__':
    world = World()
    world.run()