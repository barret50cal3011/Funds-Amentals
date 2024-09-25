from src.Player import Player
from src.stocks_m.stock import Stock

if __name__ == "__main__":
    player = Player(1000)
    stock = Stock(100, "Edison")
    print(stock.get_stock_price())
    print(player.player_money)
    print(player)
    print(player.print_player_balance())


    print(f"Stock price {stock.get_stock_price()}")
    print("Compra")
    player.buy_stock(stock, 10)
    print(player)
    print(player.print_player_balance())


    stock.set_stock_price(200)
    print(f"Stock price {stock.get_stock_price()}")
    print("Vende")
    player.sell_stock(stock, 1)
    print(player)
    print(player.print_player_balance())



    stock.set_stock_price(300)
    print(f"Stock price {stock.get_stock_price()}")
    print("Vende")
    player.sell_stock(stock, 9)
    print(player)
    print(player.print_player_balance())
    

    
    stock.set_stock_price(100)
    print(f"Stock price {stock.get_stock_price()}")
    print("compra")
    player.buy_stock(stock, 10)
    print(player)
    print(player.print_player_balance())
    print(player.print_player_money_invested_in_stock())
    

    stock.set_stock_price(100)
    print(f"Stock price {stock.get_stock_price()}")
    print("Vende")
    player.sell_stock(stock, 9)
    print(player)
    print(player.print_player_balance())
    print(player.print_player_money_invested_in_stock())
