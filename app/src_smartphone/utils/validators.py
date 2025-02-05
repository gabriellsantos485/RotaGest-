def checkout_data_of_fieldName_andFieldCommand(fieldName, fieldCommand):
    if fieldName.get_value() and fieldCommand.get_value():
        return 1
    else:
        return 0
        
