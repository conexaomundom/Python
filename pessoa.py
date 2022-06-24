from datetime import datetime

class Person():
    # Class attribute, is accessible to the person class
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    # constructor and self, name, age are instances
    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking
                    # it is like I've been passing the variable name p1 or p2
                    # in instead, the created vaiable
                    # from person class
    # class method
    @classmethod 
    def by_birth_year(cls, name, get_birth_year):
        age = cls.current_year - get_birth_year
        return cls(name, age)

    # instances methods using usam instance
    def speak(self, subject):
        if self.eating:
            print(f'{self.name} can not speak while it is eating')
            return
        print(f'{self.name} is talking about {subject}')
        self.speaking = True

    def stop_speak(self):
        if not self.speaking:
            print(f'{self.name} is not speaking now.')

        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating {food}')
            return

        if self.speaking:
            print(f'{self.name} can not eat while it is speaking')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True
    # method is a funcion that belongs to class

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return 

        self.eating = False

    def get_birth_year(self):
        return self.current_year - self.age

'''what's a python functin? It is something like that
def func(x,y): 
    pow = x ** y
    return pow
'''