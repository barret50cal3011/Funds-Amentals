from abc import ABC, abstractmethod

class AbstractStock(ABC):
    def __init__(self, stock_price: float, company_name: str, std: float = None, mean: float = None, description: str = None, actives:str = None):
        self.stock_price: float = stock_price
        self.company_name: str = company_name
        self.std:float = std
        self.mean:float = mean
        #self.affected_by:list = []
        self.stock_variation:list = []
        self.stock_description: str = description
        self.actives: str = actives

    @abstractmethod
    def get_company_name(self) -> str:
        """
        This Python function is an abstract method that should be implemented to return a company name as a string.
        """
        pass
    
    @abstractmethod
    def get_stock_price(self) -> float:
        """
        This Python function is an abstract method that should return a float value representing the stock price.
        """
        pass
    
    @abstractmethod
    def set_stock_price(self, stock_price: float) -> None:
        """
        The function `set_stock_price` is an abstract method in a Python class that sets the stock price.
        
        :param stock_price: The `stock_price` parameter in the `set_stock_price` method is expected to be a floating-point number representing the price of a stock
        :type stock_price: float
        """
        pass
    
    @abstractmethod
    def get_stock_variation(self) -> list:
        """
        The `get_stock_variation` function is an abstract method in a Python class that is expected to return a list of stock variations.
        """
        pass
    '''
    @abstractmethod
    def get_affected_by(self) -> list:
        """
        The function `get_affected_by` is an abstract method in a Python class that should return a list of items that are affected by the object.
        """
        pass
    '''
    @abstractmethod
    def get_volatility(self) -> float:
        """
        The function `get_volatility` is defined as an abstract method that should return a float representing the volatility.
        """
        pass

    @abstractmethod
    def get_stock_description(self) -> str:
        """
        This Python function is an abstract method that should return a string representing a stock description.
        """
        pass

    @abstractmethod
    def get_company_active(self) -> str:
        """
        The function `get_company_active` is an abstract method that should return a string representing the active status of a company.
        """
        pass
    '''    
    @abstractmethod
    def add_affected_by(self, event_name: str) -> None:
        """
        The `add_affected_by` function is an abstract method that adds an event name to a list of events that affect the current object.
        
        :param event_name: The `event_name` parameter in the `add_affected_by` method represents the name of an event that is being affected by another event
        :type event_name: str
        """
        pass
    
    @abstractmethod
    def delete_affected_by(self, event_name: str) -> None:
        """
        The `delete_affected_by` function is an abstract method that deletes objects affected by a specified event.
        
        :param event_name: The `event_name` parameter in the `delete_affected_by` method represents the name of the event that is being deleted or affected in some way. This parameter is a string type, indicating the name or identifier of the event that the method will operate on
        :type event_name: str
        """
        pass
    '''    
    @abstractmethod
    def event_affect_stock(self) -> None:
        """
        This function is an abstract method in a Python class that represents an event affecting stock.
        """
        pass

    @abstractmethod
    def stock_price_variation(self) -> None:
        """
        The function `stock_price_variation` is defined as an abstract method in a Python class.
        """
        pass