import random

# * Read all the comments and write in the group if you have any question, 
# * suggestion or anything else to improve the this module

# import pdb i use pdb for debuggin, change state is operative, i will add description soon

class Events:
  def __init__(self, event_name:str):

    self.__event_name:str = event_name

    self.__description:str = "None"

    # * This part below could be change in the future
    # * Its a beta of this part

    self.__impact:str = "Stable"

    self.__percentage:float = 0
    self.__state:str = "Inactive"

    # * Things that gains or lost value and the companies that could be affected

    # Example: An a war starts, the value of the guns could Up, you could invert in usWeapons Stocks
    # ! I dont use this because i dont know if it will be use in the future

    # self.__stocks_company:dict = {"ArabOilCompany": "Oil", "Doors": "Software", "Edison": "Electricity", 
    #                               "GamePause": "VideoGames", "mvidia": "PC Components", 
    #                          "pear": "Smartphones", "usWeapons": "Guns" }
  
    
  def get_event_name(self):
    return self.__event_name
    
  def get_description(self):
    return self.__description
    
  def get_impact(self):
    return self.__impact

  def get_percentage(self):
    return self.__percentage

  def get_state(self):
    return self.__state
    
  def set_impact(self, impact:str):
    self.__impact = impact

  def set_percentage(self, percentage:float):
    self.__percentage = percentage
  

  # Depending on the value of self.__state, it changes its value to the opposite
  def change_state(self):
    if self.__state == "Active":
      self.__state = "Inactive"
    else:
      self.__state = "Active"
      
# Select an event randomly

def create_event()->str:
  events_list:list = ["War", "Technology advances", "Accident", 
                    "Seasons", "Natural disasters", "Social Media"]
  random_event:str = random.choice(events_list)
  return random_event

# Save the the objects in a dict to access it

# ? Could we create a dict for storing the events?
events:dict = {"War": Events(event_name="War"), 
              "Technology advances": Events(event_name="Technology advances"), 
              "Accident": Events(event_name="Accident"), 
              "Seasons": Events(event_name="Seasons"), 
              "Natural disasters": Events(event_name="Natural disasters"), 
              "Social Media": Events(event_name="Social Media")}


if __name__ == '__main__':
  
  # * How will time be implemented, i will add something similar for trying this class
  # * timer and the while cycle will change
  timer:int = 0

  # The time that the game will stay active
  print("Hello user .......")

  while timer < 10:

    # get and a random event
    random_event:str = create_event()
    # pdb.set_trace()

    # Update the state of the ramdon event that was selected
    # I dont know how to determinate the duration of event 
    # ? there is a better way for making it?

    events.get(random_event).change_state()
    # pdb.set_trace()

    print(random_event, "is", events.get(random_event).get_state(), 
          "\n"+ "Description:", events.get(random_event).get_description(), "\n")

    
    #  ? Should i create a method that have the stocks affected by an event?
    # ? Example: War [pear, edison]
    # ? a war could affected the price of oil and guns, so it will make increase the value of 2 diferent stocks


    

    timer += 1
