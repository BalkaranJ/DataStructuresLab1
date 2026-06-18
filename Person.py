class Person:
    def __init__(self, name, age, data):
        self.name = name
        self.age = age
        self.data = data
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_data(self):
        return self.data
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_data(self, data):
        self.data = data

    """" Implementing compareTo method but in Python:
    therefor we will use rich comparison methods:
    __eq__ for equality
    __lt__ for less than """

    # Comparisons
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data == other.data
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data < other.data
    
    def __le__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data <= other.data
    
    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data > other.data
    
    def __ge__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data >= other.data
    
    def __ne__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        if not isinstance(self.data, type(other.data)):
            raise TypeError(f"Cannot compare {type(self.data)} with {type(other.data)}")
        return self.data != other.data
    
