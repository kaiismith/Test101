class Person:
    #Define function to make private variable
    def __init__(self, name, id, password, yob, gender, weight, height):
        self.__name = name
        self.__id = id
        self.__yob = yob
        self.__gender = gender
        self.__password = password
        self.__weight = weight
        self.__height =height
    #Define function to get private variable
    def get_name(self):
        return self.__name
    
    def get_id(self):
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
    
    def get_heigth(self):
        return self.__height
    
    
    def get_BMI(self):
        return Person.get_weight()/ ((Person.get_weight())**2)
    #Define function to calculate body fat percentage with BMI got and age condition
    def get_body_fat(self, year): 
        age = Person.get_age(year)
        BMI = Person.get_BMI()
        gender = Person.get_gender()
        
        if age  < 18:
            body_fat = ((1.51 * BMI) - (0.7 * age) - (3.6 * gender) + 1.4)
        
        else:
            body_fat =  ((1.2 * BMI) - (0.23 * age) - (10.8 * gender) - 5.4)
    
        return body_fat

    
