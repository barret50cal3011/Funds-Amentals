class User:
<<<<<<< HEAD
  def __init__(self, name:str, password:bytes):
=======
  def __init__(self, name:str, age:str, password:str):
>>>>>>> b4c195fc3bbe0f640a68509c6e83becfb18c6216
    self.__name=name
    self.__password=password
  def get_name(self):
    return self.__name
  def set_name(self, name:str):
    self.__name=name
  def set_age(self, age:str):
    self.__age=age
  def set_password(self, password:str):
    self.__password=password
