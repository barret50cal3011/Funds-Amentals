import random
import pdb 

# * Commented fuctions were changed (events:dict, events __init__, create_event too)

class Events:
  def __init__(self, event_name:str, i_description:str = None ,event_duration:float = 0, event_percentage_range:tuple = (0, 0)):

    self.__event_name:str = event_name

    self.__description = i_description

    self.__impact:str = "Stable"

    self.__percentage:float = 0

    self.__state:str = "Inactive"

    # This is the immutable value of the duration of eache event
    self.__event_duration:float = event_duration

    # This is the timer that will variate along the time
    self.__timer:float = 0
    
    # Range that will have the the variation of percent on of each event
    self.__event_percentage_range = event_percentage_range
    
    # self.__stocks_company:dict = {"ArabOilCompany": "Oil", "Doors": "Software", "Edison": "Electricity", 
    #                               "GamePause": "VideoGames", "mvidia": "PC Components", 
    #                               "pear": "Smartphones", "usWeapons": "Guns" }
  
    
  def get_event_name(self):
    return self.__event_name
  
  @property
  def description(self):
    if self.__description == None:
      return "a description"
    return self.__description  
  

  def get_impact(self):
    return self.__impact

  def get_percentage(self):
    return self.__percentage

  def get_state(self):
    return self.__state
  
  def get_timer(self):
    return self.__timer
  
  def get_event_percentage_range(self):
    return self.__event_percentage_range

  def set_timer(self):
    self.__timer = self.__event_duration

  def set_impact(self, impact:str):
    self.__impact = impact

  def set_percentage(self, percentage:float):
    self.__percentage = percentage
  
  def change_percentage(self):  
    if self.__state == "Active":
      pdb.set_trace()
      # gets the tuple and takes his start and ending value
      # for using it to decide the percentage value
      starts:int = self.get_event_percentage_range()[0]
      ends:int = self.get_event_percentage_range()[1]
      percentage = (random.uniform(starts, ends))

      self.set_percentage(percentage=percentage)
    elif self.__state == "Inctive":
      self.set_percentage(percentage=0)

  def change_impact(self):
    if self.__state == "Active":
      if self.__percentage > 0:
        self.set_impact("go up")
      elif self.__percentage < 0:
        self.set_impact("go down")
      elif self.__percentage == 0:
        self.set_impact("be stable")

    

  # Depending on the value of self.__state, it changes its value to the opposite
  def state_activer(self):
    if self.__state == "Inactive":
      self.__state = "Active"
      self.set_timer()
      

  def state_desactiver(self):
    if self.__state == "Active" and self.__timer != 0:
      self.__timer -= 1
      if self.__state == "Active" and self.__timer == 0:
        self.__state = "Inactive"
    
  
  
  # def change_state(self):
  #   if self.__state == "Active":
  #     self.__state = "Inactive"
  #   else:
  #     self.__state = "Active"
      
# Select an event randomly

def create_event()->str:
  verificator:bool = True
  events_list:list = ["War", "Technology advances", "Accident", 
                    "Seasons", "Natural disasters", "Social Media"]
  while verificator:
    random_event:str = random.choice(events_list)
    if random_event not in active_events:
      verificator:bool = False
      active_events.append(random_event)
      events.get(random_event).state_activer()
      return random_event


def desactivate_event()->None:
  for event in active_events:
    events.get(event).state_desactiver()
    events.get(event).change_percentage()
    events.get(event).change_impact()

events:dict = {"War": Events(event_name="War", event_duration=12, event_percentage_range=(-30, 40)),
              "Technology advances": Events(event_name="Technology advances", event_duration=4, event_percentage_range=(-20, 50)), 
              "Accident": Events(event_name="Accident", event_duration=6, event_percentage_range=(-50, -10)), 
              "Seasons": Events(event_name="Seasons", event_duration=3, event_percentage_range=(-10, 60)), 
              "Natural disasters": Events(event_name="Natural disasters", event_duration=1, event_percentage_range=(-20, -5)), 
              "Social Media": Events(event_name="Social Media", event_duration=2, event_percentage_range=(-60, 80))}

active_events:list = []

# events:dict = {"War": Events(event_name="War"), 
#               "Technology advances": Events(event_name="Technology advances"), 
#               "Accident": Events(event_name="Accident"), 
#               "Seasons": Events(event_name="Seasons"), 
#               "Natural disasters": Events(event_name="Natural disasters"), 
#               "Social Media": Events(event_name="Social Media")}


if __name__ == '__main__':
  
  timer:int = 0

  # The time that the game will stay active
  print("Hello user .......")

  while timer < 10:

    # get and a random event
    random_event:str = create_event()

    # events.get(random_event).change_state()
    
    print(random_event, "is", events.get(random_event).get_state(), "\n")

    # print(random_event, "is", events.get(random_event).get_state(), 
    #       "\n"+ "Description:", events.get(random_event).get_description(), "\n")

    next_week:str =str(input("Would you like to advence to the next week? (y/n)"))
    # * desactivate_event ha de ejecutarse justo despues de pasar a la siguiente semana
    if next_week:
      desactivate_event()
    pdb.set_trace()

    timer += 1
