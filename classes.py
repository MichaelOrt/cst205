

class ClassName(ParentClass):
    def __init__(self, param1, param2):
        self.__my_param1 = param1
        self.__my_param2 = param2
        #self.default_param = 4
        self.change_my_param(4)

    def change_my_param(self, param):
        self.__default_param = param

    def __convert_to_number(param):
        # etc

our_obj = ClassName(3, "one")

our_obj.change_my_param("two")

our_obj.__my_param2 = 9





