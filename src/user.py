class User:
  def __init__(self, name:str, password:bytes):
    self.__name=name
    self.__password=password
  def get_name(self):
    return self.__name
  def set_name(self, name:str):
    self.__name=name
  def set_age(self, age:int):
    self.__age=age
  def set_password(self, password:str):
    self.__password=password
