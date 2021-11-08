calculation_to_units = 24
name_of_units = "hours"

def days_to_units(number_of_days):
    if number_of_days > 0:
        return f'{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}'
    elif number_of_days == 0:
        return "smart ars"
    else:
        return "you entered dumb shit"

def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("dum dum")
        else:
            print("dum dum negative number dum dum")
    except ValueError:
        print("your input is not valid number. dont dum dum")

user_input = ""
while user_input != "exit":
    user_input = input("enter number of days as a comma seperated list fool\n")
    print(type(user_input.split(", ")))
    for number_of_days_element in user_input.split(", "):
        validate_and_execute()








