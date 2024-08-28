# FUNDS-AMENTALS

## Problem

The people don't know how to use a stock market.

## Solution

To solve this situation we intend to make a game that simulates stock market behaviour. For simplicity porposes the game will iniciatially be text base game.

## How we approach the problem

Since the problem is a lack of knowledge on how stock markets work and games have historically been a way in which learning is imparted we decided to make a game as a tutorial to start in stock market investment.

## Class diagram
```mermaid
classDiagram
    class Events {
        -event_name: str
        -description: str
        -impact: str
        -percentage: float
        -state: str
        -event_duration: float
        -timer: float
        -event_percentage_range: tuple
        -affected_stock: str
        +get_event_name() 
        +description
        +get_impact()
        +get_percentage()
        +get_state()
        +get_timer()
        +get_event_duration()
        +get_event_percentage_range()
        +set_timer()
        +set_impact(impact: str)
        +set_percentage(percentage: float)
        +change_percentage()
        +change_impact()
        +state_activer()
        +state_desactiver()
    }

    class EventsStore {
        -name: str
        -activation_limit: int
        -sons_list: list
        -sons_active_list: list
        +reach_limit() 
        +select_son() 
        +desactive_sons() 
    }

    class AbstractStock {
        -stock_price: float
        -company_name: str
        -affected_by: list
        +get_stock_price() 
        +set_stock_price(stock_price: float) 
        +get_affected_by() 
        +add_affected_by(event_name: str) 
        +delete_affected_by(event_name: str) 
    }

    class Stock {
        -stock_price: float
        -company_name: str
        -std: float
        -mean: float
        -affected_by: list
        -stock_variation: list
        +get_company_name() 
        +get_stock_price() 
        +get_stock_variation() 
        +get_affected_by() 
        +set_stock_price(stock_price: float) 
        +add_affected_by(event_name: str) 
        +delete_affected_by(event_name: str) 
        +stock_variation_changer() 
        +event_affect_stock() 
        +stock_price_variation() 
    }

    class Controller {
        -world: World
        +eval_comad(command: str) 
    }

    class Player {
        -player_portfolio: dict
        +buy_stock(stock: Stock, quantity: int) 
        +sell_stock(stock: Stock, quantity: int) 
        +get_stock_amount(stock: Stock) 
        +get_portfolio() 
    }

    class View {
        -controler: Controller
        +read() 
        +run() 
    }

    class World {
        -events: dict
        -stocks: dict
        -player: Player
        +load_stocks() 
        +run() 
        +read_news(news: str) 
        +buy_stock(stock_name: str, amount: int) 
        +sell_stock(stock_name: str, amount: int) 
        +next_week() 
        +see_portfolio() 
    }

    EventsStore *-- Events
    AbstractStock <|-- Stock
    Controller --> World
    Player --* Stock
    View <-- Controller
    World *-- Events
    World *-- Stock
    World *-- Player

```

## Download and usage


