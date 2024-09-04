import random
from collections import UserList
from events_m.events import Events

class EventsStore:
    def __init__(self,name:str = None,  limit:int = 0, sons_list:list = []):
        super().__init__(sons_list)
        self.__name = name
        self.__sons_list = sons_list
        self.__activation_limit = limit
        self.__sons_active_list = []

    def __repr__(self) -> str:
        return self.__name
    
    # TODO You should use this in a conditional if you wanna use select_son()

    def reach_limit(self):
        return self.__activation_limit == len(self.__sons_active_list)

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

