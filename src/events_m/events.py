import random

class Events:
  def __init__(self, event_name:str, i_description:str = None ,event_duration:float = 0, event_percentage_range:tuple = (0, 0), affected_stock:str = None, actives:str = None):

    self.__event_name:str = event_name

    self.__stock_actives:str = actives

    self.__stock_name:str = affected_stock
    
    self.__description:str = i_description
    # self.__description:str = i_description.format(self.__stock_name, self.__stock_actives)

    self.__impact:str = "Stable"

    self.__percentage:float = 0

    self.__state:str = "Inactive"

    # This is the immutable value of the duration of eache event
    self.__event_duration:float = event_duration

    # This is the timer that will variate along the time
    self.__timer:float = 0
    
    # Range that will have the the variation of percent on of each event
    self.__event_percentage_range:tuple = event_percentage_range
    
    # self.__stocks_company:dict = {"ArabOilCompany": "Oil", "Doors": "Software", "Edison": "Electricity", 
    #                               "GamePause": "VideoGames", "mvidia": "PC Components", 
    #                               "pear": "Smartphones", "usWeapons": "Guns" }
  
    
  def get_event_name(self) -> str:
    """
    The function `get_event_name` returns the event name as a string.
    :return: The method `get_event_name` is returning the private attribute `__event_name` of the class instance.
    """
    return self.__event_name
  
  @property
  def description(self):
    """
    The function `description` returns a description if it is not None, otherwise it returns "a description".
    :return: If the `__description` attribute is `None`, the method `description` will return the string "a description". Otherwise, it will return the value of the `__description` attribute.
    """
    if self.__description == None:
      return "a description"
    return self.__description  
  
  def get_impact(self) -> str:
    """
    This Python function named `get_impact` returns the impact attribute of the object it belongs to as a string.
    :return: The `get_impact` method is returning the value of the `__impact` attribute of the object.
    """
    return self.__impact

  def get_percentage(self) -> float:
    """
    The function `get_percentage` returns the percentage value stored in the private attribute `__percentage`.
    :return: The method `get_percentage` is returning the private attribute `__percentage` of the class.
    """
    return self.__percentage

  def get_state(self) -> str:
    """
    This Python function named `get_state` returns the value of the private attribute `__state` as a string.
    :return: The `get_state` method is returning the value of the `__state` attribute, which is a string.
    """
    return self.__state
  
  def get_timer(self) -> float:
    """
    This function returns the value of the private variable `__timer`.
    :return: The `get_timer` method is returning the value of the `__timer` attribute, which is a float.
    """
    return self.__timer
  
  def get_event_duration(self) -> float:
    """
    The function `get_event_duration` returns the event duration as a float.
    :return: The method `get_event_duration` is returning the value of the private attribute `__event_duration`.
    """
    return self.__event_duration
  
  def get_affected_stock(self):
    """
    This function returns the name of the affected stock.
    :return: The method `get_affected_stock` is returning the value of the private attribute `__stock_name`.
    """
    return self.__stock_name
  
  # ! Posible elimination 
  # def get_event_percentage_range(self):
  #   return self.__event_percentage_range
  
  def set_timer(self) -> None:
    """
    The function `set_timer` sets the timer value to the event duration.
    """
    self.__timer = self.__event_duration

  def set_impact(self, impact:str) -> None:
    """
    The function `set_impact` sets the impact attribute of an object to the specified value.
    
    :param impact: The `set_impact` method is a setter method that takes a string parameter `impact` and sets the private attribute `__impact` to the value of the `impact` parameter
    :type impact: str
    """
    self.__impact = impact


  def set_percentage(self, percentage:float):
    """
    The function `set_percentage` sets the percentage value for a given object.
    
    :param percentage: The `percentage` parameter in the `set_percentage` method is a float type that represents the percentage value to be set for the object's attribute `__percentage`
    :type percentage: float
    """
    self.__percentage = percentage
  


  # Based on a tuple that has percentages, it will selects the tendence of the event 
  def tendence_selector(self) -> None:  
    """
    This function selects a random percentage value within a specified range if the state is "Active".
    """
    if self.__state == "Active":
      # gets the tuple and takes his start and ending value
      # for using it to decide the percentage value
      starts:int = self.__event_percentage_range[0]
      ends:int = self.__event_percentage_range[1]
      percentage = round((random.uniform(starts, ends)), ndigits=2)
      self.set_percentage(percentage=percentage)

  # Depending of the percentage's value, it has 3 options

  def change_impact(self) -> None:
    """
    The function `change_impact` determines the impact based on the state and percentage values.
    """
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
    """
    The function `state_activer` changes the state from "Inactive" to "Active" and calls other methods to set a timer, select tendencies, and change impact.
    """
    if self.__state == "Inactive":
      self.__state = "Active"
      self.set_timer()
      self.tendence_selector()
      self.change_impact()

      

  def state_desactiver(self) -> None:
    """
    The function `state_desactiver` decreases a timer and changes the state to "Inactive" when the timer reaches 0.
    """
    if self.__state == "Active" and self.__timer != 0:
      self.__timer -= 1
      if self.__state == "Active" and self.__timer == 0:
        self.__state = "Inactive"
        self.set_percentage(percentage=0)
        self.change_impact()
        