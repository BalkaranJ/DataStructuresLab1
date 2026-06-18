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

        