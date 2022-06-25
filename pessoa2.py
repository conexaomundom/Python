from datetime import datetime
from random import randint

class Person2():
    # class attribute is acessible only to class pessoa
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    # constrctor and self, name, age are instances
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return self.current_year - self.age

    # class method
    @classmethod 
    def by_birth_year(cls, name, get_birth_year):
        age = cls.current_year - get_birth_year
        return cls(name, age)

''' does not need the class or instances is as if it were a normal 
function, but by organization needs to be within the class, 
can not use neither self, nor cls'''

    @staticmethod
        def gera_id():
            #radom.seed(2022)
            rand = randint(10000,19999)
            return rand



