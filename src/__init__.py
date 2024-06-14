from stocks.stock import Stocks
puerta = Doors(stock_price=25)


puerta.add_affected_by("Perro")
puerta.add_affected_by("Gato")
for i in puerta.get_affected_by():
    print(i, end = " ")


def load_stocks(self):
    stocks = {
        "Doors" : Doors(300),
        "Edison" : Edison(400)
    }
    return stocks