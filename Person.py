from functools import total_ordering
@total_ordering



class Person:
    def __init__(self, name, age, data_type):
        self.name = name
        self.age = age
        self.data_type = data_type
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_data_type(self):
        return self.data_type
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_data_type(self, data_type):
        self.data_type = data_type

    """" Implementing compareTo method but in Python:
    therefor we will use rich comparison methods:
    __eq__ for equality
    __lt__ for less than """

    # Comparison
    def __eq__(self, other):

