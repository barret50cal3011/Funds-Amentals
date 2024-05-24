class User:
  def __init__(self, name:str, age:str, password:str):
    self.__name=name
    self.__age=age
    self.__password=password
  def __repr__(self) -> str:
    return f"name={self.__name}, age={self.__age}, password={self.__password}"
  def get_name(self):
    return self.__name
  def get_age(self):
    return self.__age
  def get_password(self):
    return self.__password
  def set_name(self, name:str):
    self.__name=name
  def set_age(self, age:str):
    self.__age=age
  def sert_password(self, password:str):
    self.__password=password
