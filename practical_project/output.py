from logic import Logic
from input import Input
class Output:
    
    def login():
        username = input("Enter username: ")
        password =input("Eneter password: ")
        if Logic.check_login(username, password):
            print("welcum")
        else:
            print("cook!")

    def print():
        print(Input().get_person())
        