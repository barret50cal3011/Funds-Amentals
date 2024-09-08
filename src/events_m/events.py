import random


class Events:
  def __init__(self, event_name:str, i_description:str = None ,event_duration:float = 0, event_percentage_range:tuple = (0, 0), affected_stock:str = None, actives:str = None):

    self.__event_name:str = event_name

    self.__stock_actives:str = affected_stock

    self.__stock_name:str = actives
    
    self.__description:str = i_description.format(self.__stock_name, self.__stock_actives)

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
  
    
  def get_event_name(self) -> str:
    return self.__event_name
  
  @property
  def description(self):
    if self.__description == None:
      return "a description"
    return self.__description  
  
  def get_impact(self) -> str:
    return self.__impact

  def get_percentage(self) -> float:
    return self.__percentage

  def get_state(self) -> str:
    return self.__state
  
  def get_timer(self) -> float:
    return self.__timer
  
  def get_event_duration(self) -> float:
    return self.__event_duration
  
  # ! Posible elimination 
  # def get_event_percentage_range(self):
  #   return self.__event_percentage_range
  
  def set_timer(self) -> None:
    self.__timer = self.__event_duration

  def set_impact(self, impact:str) -> None:
    self.__impact = impact


  # ! Posible elimination 
  # def set_percentage(self, percentage:float):
  #   self.__percentage = percentage
  


  # Based on a tuple that has percentages, it will selects the tendence of the event 
  def tendence_selector(self) -> None:  
    if self.__state == "Active":
      # gets the tuple and takes his start and ending value
      # for using it to decide the percentage value
      starts:int = self.__event_percentage_range[0]
      ends:int = self.__event_percentage_range[1]
      percentage = ((random.uniform(starts, ends))/100)
      self.set_percentage(percentage=percentage)

  # Depending of the percentage's value, it has 3 options

  def change_impact(self) -> None:
    if self.__state == "Active":
      if self.__percentage > 0:
        self.set_impact("go up")
      elif self.__percentage < 0:
        self.set_impact("go down")
      elif self.__percentage == 0:
        self.set_impact("be stable")

    elif self.__state == "Inactive":
      self.set_impact("be stable")

    

  # Depending on the value of self.__state, it changes its value to the opposite
  # This will be in world, this is an aproximation
  def state_activer(self) -> None:
    if self.__state == "Inactive":
      self.__state = "Active"
      self.set_timer()
      self.tendence_selector()
      self.change_impact()

      

  def state_desactiver(self) -> None:
    if self.__state == "Active" and self.__timer != 0:
      self.__timer -= 1
      if self.__state == "Active" and self.__timer == 0:
        self.__state = "Inactive"
        self.set_percentage(percentage=0)
        self.change_impact()
        
