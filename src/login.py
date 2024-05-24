from user import User

name:str = input("What is your name? ")
age:str = input("How old are you? ")
password:str = input("What is your password? ")
user = User(name, age, password)
while True:
  answer:str=input("Woul you like to change something or view data(y/n)? ")
  if answer.lower() == "y":
    while True:
      print("1. Name\n2. Age\n3. Password\n4. View data\n5. Exit")
      secondAnswer:str=input("What's you're choice? ")
      match secondAnswer:
        case "1":
          name:str = input("What is your name? ")
          user.set_name(name)
        case "2":
          age:str = input("How old are you? ")
          user.set_age(age)
        case "3":
          password:str = input("What is your password (y/n)? ")
          user.sert_password(password)
        case "4":
          print(user)
        case "5":
         break
  elif answer.lower()=="n":
    break