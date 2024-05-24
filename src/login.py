from user import User
import bcrypt

# Input user name and password
name: str = input("What is your name? ")
password: str = input("What is your password? ")

# Hash the password with a salt
pwd: str = password.encode('utf-8')
hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
user = User(name, hashed)

while True:
    answer: str = input("Would you like to change something (y/n)? ")
    if answer.lower() == "y":
        while True:
            print("1. Name\n2. Password\n3. Exit")
            secondAnswer: str = input("What's your choice? ")
            match secondAnswer:
                case "1":
                    while True:
                        pwds = bytes(input("Input the password: "), 'utf-8')
                        if bcrypt.checkpw(pwds, user._User__password):  # Use the stored hash for verification
                            print("The password is correct")
                            break
                        else:
                            print("The password is incorrect\nTry again")
                    name: str = input("What is your new name? ")
                    user.set_name(name)
                case "2":
                    while True:
                        pwds = bytes(input("Input the current password: "), 'utf-8')
                        if bcrypt.checkpw(pwds, user._User__password):  # Use the stored hash for verification
                            print("The password is correct")
                            break
                        else:
                            print("The password is incorrect\nTry again")
                    second_password: str = input("What is your new password? ")
                    new_pwd: str = second_password.encode('utf-8')
                    new_hash = bcrypt.hashpw(new_pwd, bcrypt.gensalt())
                    user.set_password(new_hash)
                case "3":
                    break
    elif answer.lower() == "n":
        break

print("Goodbye!")
