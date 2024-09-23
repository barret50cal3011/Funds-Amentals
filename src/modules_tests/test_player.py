from src.Player import Player
from src.stocks_m.stock import Stock

if __name__ == "__main__":
    player = Player(1000)
    stock = Stock("Edison", 100)
    print(type(stock.get_stock_price()))
    print(type(player.player_money))
    print(player.get_portfolio())
    # print(player.buy_stock(stock, 10))
    # print(player.get_stock_amount("Edison"))    
    