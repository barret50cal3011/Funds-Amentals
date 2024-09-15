from abc import ABC, abstractmethod

class AbstractStock(ABC):
    def __init__(self, stock_price: float, company_name: str, std: float = None, mean: float = None, description: str = None, actives:str = None):
        self.stock_price: float = stock_price
        self.company_name: str = company_name
        self.std:float = std
        self.mean:float = mean
        self.affected_by:list = []
        self.stock_variation:list = []
        self.stock_description: str = description
        self.actives: str = actives

    @abstractmethod
    def get_company_name(self) -> str:
        pass
    
    @abstractmethod
    def get_stock_price(self) -> float:
        pass
    
    @abstractmethod
    def set_stock_price(self, stock_price: float) -> None:
        pass

    @abstractmethod
    def get_stock_variation(self) -> list:
        pass

    @abstractmethod
    def get_affected_by(self) -> list:
        pass
    
    @abstractmethod
    def get_volatility(self) -> float:
        pass

    @abstractmethod
    def get_stock_description(self) -> str:
        pass

    @abstractmethod
    def get_company_active(self) -> str:
        pass
    
    @abstractmethod
    def add_affected_by(self, event_name: str) -> None:
        pass
    
    @abstractmethod
    def delete_affected_by(self, event_name: str) -> None:
        pass
    
    @abstractmethod
    def event_affect_stock(self) -> None:
        pass

    @abstractmethod
    def stock_price_variation(self) -> None:
        pass