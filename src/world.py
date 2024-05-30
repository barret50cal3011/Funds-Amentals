import events
import stocks
import Player

class World:
    def __init__(self,events,player):
        self.events = events.Events()
        self.stocks = stocks.Stocks()
        self.player = Player.Player()