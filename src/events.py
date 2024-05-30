import random
class Events:
    def __init__(self, event_name: str):
        self.__event_name: str = event_name
        self.__description: str = "None"
        self.__impact: str = "Stable"
        self.__percentage: float = 0
        self.__state: str = "Inactive"

    def get_event_name(self):
        return self.__event_name

    def get_description(self):
        return self.__description

    def get_impact(self):
        return self.__impact

    def get_percentage(self):
        return self.__percentage

    def get_state(self):
        return self.__state

    def set_impact(self, impact: str):
        self.__impact = impact

    def set_percentage(self, percentage: float):
        self.__percentage = percentage

    def change_state(self):
        if self.__state == "Active":
            self.__state = "Inactive"
        else:
            self.__state = "Active"
            
    def affect_stocks(self, stock_list):
        if self.__state == "Active":
            for stock in stock_list:
                stock_price = stock.get_stock_price()
                new_price = stock_price * (1 + self.__percentage / 100)
                stock.set_stock_price(new_price)

def create_event() -> str:
    events_list: list = ["War", "Technology advances", "Accident", 
                         "Seasons", "Natural disasters", "Social Media"]
    random_event: str = random.choice(events_list)
    return random_event

events: dict = {
    "War": Events(event_name="War"),
    "Technology advances": Events(event_name="Technology advances"),
    "Accident": Events(event_name="Accident"),
    "Seasons": Events(event_name="Seasons"),
    "Natural disasters": Events(event_name="Natural disasters"),
    "Social Media": Events(event_name="Social Media")
}

if __name__ == '__main__':
    from stocks.stock import Stock

    timer: int = 0
    stocks_list = [Stock(100.0, "Edison"), Stock(150.0, "ArabOilCompany"),Stock(150.0, "USWeapons"), Stock(150.0, "GamePause"),Stock(150.0, "Doors"), Stock(150.0, "Mvidia"), Stock(150.0, "Pear")]

    print("Hello user .......")

    while timer < 10:
        random_event_name: str = create_event()
        random_event = events.get(random_event_name)
        random_event.change_state()

        if random_event.get_state() == "Active":
            random_event.set_percentage(random.uniform(-5, 5))
            random_event.affect_stocks(stocks_list)

        print(f"{random_event_name} is {random_event.get_state()}", 
              f"\nDescription: {random_event.get_description()}",
              f"\nImpact: {random_event.get_percentage()}%",
              "\n")

        for stock in stocks_list:
            print(f"{stock.company_name} stock price: {stock.get_stock_price()}")

        timer += 1
