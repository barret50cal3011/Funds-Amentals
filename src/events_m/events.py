import random, json

# with open('../data/events.json', 'r') as file:
#     json_file = json.load(file)





class Events:
  def __init__(self, event_name:str, i_description:str = None ,event_duration:float = 0, event_percentage_range:tuple = (0, 0), affected_stock:'Stocks' = None):

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
    self.__event_percentage_range:tuple = event_percentage_range

    self.affected_stock:str = affected_stock

    
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
  
  def get_event_duration(self):
    return self.__event_duration
  
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
      # gets the tuple and takes his start and ending value
      # for using it to decide the percentage value
      starts:int = self.get_event_percentage_range()[0]
      ends:int = self.get_event_percentage_range()[1]
      percentage = (random.uniform(starts, ends))

      self.set_percentage(percentage=percentage)
      
    elif self.__state == "Inctive":
      self.set_percentage(percentage=0)

  # Depending of the percentage's value, it has 3 options

  def change_impact(self):
    if self.__state == "Active":
      if self.__percentage > 0:
        self.set_impact("go up")
      elif self.__percentage < 0:
        self.set_impact("go down")
      elif self.__percentage == 0:
        self.set_impact("be stable")

    

  # Depending on the value of self.__state, it changes its value to the opposite
  # This will be in world, this is an aproximation
  def state_activer(self):
    if self.__state == "Inactive":
      self.__state = "Active"
      self.set_timer()

      

  def state_desactiver(self):
    if self.__state == "Active" and self.__timer != 0:
      self.__timer -= 1
      if self.__state == "Active" and self.__timer == 0:
        self.__state = "Inactive"
# ______________________________________________________________________________________________________________________________________

# def create_event()->str:
#   verificator:bool = True
#   events_list:list = ["War", "Technology Advances", "Accident", 
#                     "Seasons", "Natural Disasters", "Social Media"]  
  
#   while verificator:
#     random_event:str = random.choice(events_list)
#     if events.get(random_event).get_state() == "Inactive":
#       verificator:bool = False
#       events.get(random_event).state_activer()
#       return random_event
    

# def all_events_active():
#   for event in events.values():
#     if event.get_state() == "Inactive":
#       return False
#   return True

# def desactivate_event()->None:
#   for event in events.values():
#     if event.get_state() == "Active":
#       event.state_desactiver()
#       event.change_percentage()
#       event.change_impact()
