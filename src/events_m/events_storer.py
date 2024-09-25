import random
from src.events_m.events import Events

class EventsStorer:
    def __init__(self, name:str = None, sons_list:list = []):
        self.__name: str = name
        self.__sons_list: list = sons_list
        self.__sons_active_list: list = []

    def __repr__(self) -> str:
        """
        The `__repr__` function in Python returns the name of the object as a string.
        :return: The `__repr__` method is returning the value of the `__name` attribute of the object.
        """
        return self.__name
    
    def __iter__(self):
        """
        The function `__iter__` returns the `__sons_list` attribute for iteration.
        :return: The `__iter__` method is returning `self.__sons_list`, which suggests that the object implementing this method is iterable and iterating over it will yield the elements in `self.__sons_list`.
        """
        return self.__sons_list
    
    def __hash__(self):
        """
        The `__hash__` function in Python uses only immutable attributes to calculate the hash value, specifically using the `name` attribute in this case.
        :return: The `__hash__` method is returning the hash value of the `name` attribute of the object.
        """
        # Usar solo atributos inmutables para calcular el hash
        return hash(self.name)

    def __eq__(self, other):
        """
        The function checks if two objects of type EventsStorer are equal based on their name attribute.
        
        :param other: The `other` parameter in the `__eq__` method represents another object that you want to compare with the current object for equality. In this specific implementation, it checks if the `other` object is an instance of the `EventsStorer` class and if the `name` attribute of
        :return: The `__eq__` method is being used to compare two instances of the `EventsStorer` class. It checks if the `other` object is an instance of `EventsStorer` and if the `name` attribute of both instances is equal. The method will return `True` if both conditions are met, indicating that the two instances are considered equal based on this comparison.
        """
        # Comparar solo atributos inmutables
        return isinstance(other, EventsStorer) and self.name == other.name

    
    # TODO You should use this in a conditional if you wanna use select_son()

    def reach_limit(self) -> bool:
        """
        The function `reach_limit` returns a boolean value indicating whether the length of a private list `__sons_list` is equal to zero.
        :return: The `reach_limit` method is returning a boolean value. It returns `True` if the length of the `__sons_list` attribute is equal to 0, and `False` otherwise.
        """
        return 0 == len(self.__sons_list)

    def select_son(self) -> Events:
        """
        This function selects a random event from a list of events and moves it to an active list while removing it from the original list.
        :return: The `select_son` method returns an active event of type `Events` that is randomly chosen from the `__sons_list`.
        """
        active_event: Events = random.choice(self.__sons_list)
        self.__sons_active_list.append(active_event)
        self.__sons_list.remove(active_event)
        return active_event


    # Implementation with list index and some logic (first enters first ends)

    def active_sons(self) -> None:
        """
        This function selects a son and activates their state.
        """
        select_son: Events = self.select_son()
        select_son.state_activer()

    def desactive_sons(self) -> None:
        """
        The function `desactive_sons` deactivates all active sons and moves them to the inactive sons list if their state is "Desactive".
        """

        for son in self.__sons_active_list:
            son.state_desactiver()
            if son.get_state() == "Inactive":
                self.__sons_active_list.remove(son)
                self.__sons_list.append(son)

    def get_active_sons(self) -> list:
        """
        This function returns a list of active sons.
        :return: The method `get_active_sons` is returning a list of active sons stored in the `__sons_active_list` attribute of the object.
        """
        return self.__sons_active_list
        
    @property
    def name(self) -> str:
        """
        The function `name` returns the value of the private attribute `__name` as a string.
        :return: The `name` method is returning the value of the `__name` attribute of the object.
        """
        return self.__name

    
    
