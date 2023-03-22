from model.Person import Person
class Calculator:

    def calculate_BMI():
        return (Person.get_weight())/((Person.get_weight())**2)
    
    def calculate_body_fat(year): 
        age = Person.get_age(year)
        BMI = Person.get_BMI()
        gender = Person.get_gender()
        
        if age  < 18:
            return ((1.51 * BMI) - (0.7 * age) - (3.6 * gender) + 1.4)
        
        else:
            return ((1.2 * BMI) - (0.23 * age) - (10.8 * gender) - 5.4)
        
    def calculate_LBM():
        weight = Person.get_weight()
        gender = Person.get_gender()
        height = Person.get_height()
        if gender == 1:
            LBM = 0.407 * weight + 0.267 * height - 19.2
        
        else:
            LBM = 0.252 * weight + 0.473 * height - 48.3

        return LBM

    def calculate_BMR():
        weight = Person.get_weight()
        age = Person.get_age()
        height = Person.get_height() * 100
        gender = Person.get_gender()
        if gender == 1:
            BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)            
        
        else:
            BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        
        return BMR
    
    