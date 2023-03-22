from input import Input
class Logic:
    def check_login(username, password):
        if username in Input.get_person():
            if Input.get_person()[username][password]["password"] == password:
                return True
            else: return False
        else:
            return False
        

        
    
    
