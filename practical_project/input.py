from model.Person import Person
import os
import pickle
from Calculator import Calculator
class Input:
    
    def __init__(self, person ={}):
        self.__person = {}
        self.__person = person        
    def get_person(self):
        return self.__person
     
    def input_person_info(self):
        num = int(input("Enter number of human being: "))

        for i in range (num):
            username = input("Enter id: ")
            name = input("Enter name: ")
            password = input("Enter password: ")
            while True:
                if len(password) <= 6:
                    password = input("Do you want your account being hacked????????????")
                else:
                    break
            yob = int(input("Enter year of birth: "))
            gender = int(input("Enter gender (1 for male, 0 for female): "))
            while True:
                if gender !=0 and gender !=1:
                    gender = int(input("Enter gender (1 for male, 0 for female): "))
                else:
                    break
            weight = int(input("Enter weight: "))
            height =int(input("Enter height: "))
            person = Person(name, username, password, yob, gender, weight, height)
            self.get_person()[person.get_username()] = {"name": person.get_name(), "password": person.get_password(), "yob": person.get_yob(), "weight": person.get_weight(), "height": person.get_height()}
        
        self.compress_person_info("person.txt")
        self.__init__(self.get_person())
        
    
    def compress_person_info(self, file):
        file = open(file, "ab")
        pickle.dump(self.get_person(), file)
        file.close()
                 
    def load_person_info(self, file):
        if os.path.exists(file):
            file = open(file, "rb")
            load_person_data = pickle.load(file)
            file.close()
            return (load_person_data)    
        else:
            pass
    

            
