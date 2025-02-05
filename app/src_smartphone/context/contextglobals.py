# context/contextglobals.py
class VarGlobals:
    __name = None
    __command = None
    __list_items=[]

    @classmethod
    def set_name(cls, name: str):
        cls.__name = name

    @classmethod
    def get_name(cls):
        return cls.__name

    @classmethod
    def set_command(cls, command: str):
        cls.__command = command

    @classmethod
    def get_command(cls):
        return cls.__command
    
    @classmethod
    def get_list(cls):
        return cls.__list_items
    
    @classmethod
    def set_list(cls, item_name, item_value, item_count):
        return cls.__list_items.append({"name":item_name,"value":item_value, "count":item_count})
    
