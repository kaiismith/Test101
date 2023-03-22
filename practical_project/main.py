from output import Output
from input import Input

Input(Input().load_person_info("person.txt"))

while True:
    user_input = input()
    if user_input == "1":
        Input().input_person_info()
    elif user_input == "2": 
        Output.print()
    else:
        break
