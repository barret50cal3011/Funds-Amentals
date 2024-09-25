import random
from events_m.events import Events

class EventsStorer:
    def __init__(self, name:str = None, sons_list:list = []):
        self.__name: str = name
        self.__sons_list: list = sons_list
        self.__sons_active_list: list = []

    def __repr__(self) -> str:
        return self.__name
    
    def __iter__(self):
        return self.__sons_list
    
    def __hash__(self):
        # Usar solo atributos inmutables para calcular el hash
        return hash(self.name)

    def __eq__(self, other):
        # Comparar solo atributos inmutables
        return isinstance(other, EventsStorer) and self.name == other.name

    
    # TODO You should use this in a conditional if you wanna use select_son()

    def reach_limit(self) -> bool:
        return 0 == len(self.__sons_list)

    def select_son(self) -> Events:
        active_event: Events = random.choice(self.__sons_list)
        self.__sons_active_list.append(active_event)
        self.__sons_list.remove(active_event)
        return active_event


    # Todo Implementation with for

    # def desactive_sons(self):
    #     for son in self.__sons_active_list:
    #         son.state_desactiver()
    #         if son.get_state() == "Desactive":
    #             self.__sons_active_list.remove(son)


    # Implementation with list index and some logic (first enters first ends)

    def active_sons(self) -> None:
        select_son: Events = self.select_son()
        select_son.state_activer()

    def desactive_sons(self) -> None:
        for son in self.__sons_active_list:
            son.state_desactiver()
        if son[0].get_state() == "Desactive":
            self.__sons_active_list.remove(son)
            self.__sons_list.append(son)

    def get_active_sons(self) -> list:
        return self.__sons_active_list
        
    @property
    def name(self) -> str:
        return self.__name

    
    
