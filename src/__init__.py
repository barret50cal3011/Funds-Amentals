from stocks.doors import Doors
from stocks.edison import Edison
from events import Events
import pdb

evento = Events(event_name="War", event_duration=12, event_percentage_range=(-30, 40))
evento.state_activer()
evento.set_percentage(percentage=10)

puerta = Doors(stock_price=100)

puerta.add_affected_by("Perro")
puerta.add_affected_by("Gato")



for i in puerta.get_affected_by():
    print(i, end = " ")

print(puerta.get_stock_price())

evento.affect_stock(stock=puerta)


def load_stocks():
        stocks = {
            "Doors" : Doors(300),
            "Edison" : Edison(400)
        }
        return stocks
hi = load_stocks()
for affector in hi.values():
    pdb.set_trace()
    evento.affect_stock(affector)

print(hi.get("Doors").get_stock_price())
print(hi.get("Edison").get_stock_price())

print(load_stocks().get("Doors").get_stock_price())