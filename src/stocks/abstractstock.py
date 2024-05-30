from abc import ABC, abstractmethod

class AbstractStock(ABC):
    def __init__(self, stock_price: float, company_name: str):
        self._stock_price: float = stock_price
        self.company_name: str = company_name

    @abstractmethod
    def get_stock_price(self) -> float:
        pass
    
    @abstractmethod
    def set_stock_price(self, stock_price: float):
        pass
