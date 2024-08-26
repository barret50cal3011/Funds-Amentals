import random
from events_m.events import Events

class EventsStore:
    def __init__(self,name:str = None,  limit:int = 0, sons_list:list = None):
        self.__name = name
        self.__activation_limit = limit
        self.__sons_list = sons_list
        self.__sons_active_list = []


    
    # TODO You should use this in a conditional if you wanna use select_son()

    def reach_limit(self):
        return self.__activation_limit == len(self.__sons_active_list)

    def select_son(self):
        active_event:Events = random.choice(self.__sons_list)
        self.__sons_active_list.append(active_event)
        self.__sons_list.remove(active_event)

    def desactive_sons(self):
        for son in self.__sons_active_list:
            son.state_desactiver()
            if son.get_state() == "Desactive":
                self.__sons_active_list.remove(son)


