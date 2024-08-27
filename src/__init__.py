from stocks_m.doors import Doors
from stocks_m.edison import Edison
from events_m.events import Events
import pdb
import copy

# evento = Events(event_name="War", event_duration=12, event_percentage_range=(-30, 40))
# evento.state_activer()
# evento.set_percentage(percentage=10)

# puerta = Doors(stock_price=100)


# puerta2 = copy.deepcopy(puerta)

# print(puerta.get_stock_price(), puerta2.get_stock_price())

# puerta.add_affected_by("Perro")
# puerta.add_affected_by("Gato")



# for i in puerta.get_affected_by():
#     print(i, end = " ")

# print(puerta.get_stock_price())

# evento.affect_stock(stock=puerta)


def load_stocks():
        stocks = {
            "Doors" : Doors(300, mean=0.025, std=0.010),
            "Edison" : Edison(400, mean=0.3, std=0.015)
        }
        return stocks

# i dont know how to change the values inside "def load_stocks""
hi = load_stocks()

for affector in hi.values():
    affector.stock_variation_changer()
    # evento.affect_stock(affector)

print(hi.get("Doors").get_stock_price())
print(hi.get("Edison").get_stock_price())


for x in range(22):
    for y in hi.values():
        y.stock_price_variation()

# It could be a comand like "help" or "news"
print(hi.get("Doors").get_stock_variation() )

print(hi.get("Doors").get_stock_price())