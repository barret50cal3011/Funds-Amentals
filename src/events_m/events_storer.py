import random
from events_m.events import Events

class EventsStorer:
    def __init__(self, name:str = None, sons_list:list = []):
        self.__name: str = name
        self.__sons_list: list = sons_list
        self.__sons_active_list: list = []
        self.__percentage: dict = {"Doors": 0, "Edison": 0, "Game pause": 0, "ArabOilCompany": 0, "MVidia": 0, "Pear": 0, "USWeapons": 0}

    def __repr__(self) -> str:
        return self.__name
    
    def __iter__(self):
        return self.__sons_list
    
    # TODO You should use this in a conditional if you wanna use select_son()

    def reach_limit(self):
        return 0 == len(self.__sons_list)

    def select_son(self):
        active_event: Events = random.choice(self.__sons_list)
        self.__sons_active_list.append(active_event)
        self.__sons_list.remove(active_event)


    # Todo Implementation with for

    # def desactive_sons(self):
    #     for son in self.__sons_active_list:
    #         son.state_desactiver()
    #         if son.get_state() == "Desactive":
    #             self.__sons_active_list.remove(son)


    # Implementation with list index and some logic (first enters first ends)

    def desactive_sons(self):
        for son in self.__sons_active_list:
            son.state_desactiver()
        if son[0].get_state() == "Desactive":
            self.__sons_active_list.remove(son)
    
    
    def get_percentage(self):
           return self.__percentage


    def get_active_sons(self):
        return self.__sons_active_list
        

    
    
