class Person:
    def __init__(self, name, username, password, yob, gender, weight, height):
        self.__name = name
        self.__id = username
        self.__yob = yob
        self.__gender = gender
        self.__password = password
        self.__weight = weight
        self.__height =height
    
    def get_name(self):
        return self.__name
    
    def get_username(self):
        return self.__id
    
    def get_yob(self):
        return self.__yob
    
    def get_gender(self):
        return self.__gender
    
    def get_age(self, now):
        return now - Person.get_yob()
    
    def get_password(self):
        return self.__password
    
    def get_weight(self):
        return self.__weight
    
    def get_height(self):
        return self.__height
    
    
    
    
