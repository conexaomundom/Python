# importando um classe do arquivo pessoa
from pessoa import Person
from pessoa2 import Person2

# em que p1 é da classe Pessoa() e p2 também é da classe pessoa
p1 = Person2('Marina',24)
p2 = Person('Julio', 26)

# usou um molde para criar uma pessoa o molde é a classe Pessoa
# o obejto p1 é uma instancia

# a variavel nome que só pertence à p1 são atributos
# nome é uma variável de instância


p3 = Person.by_birth_year('Marina', 1998)
print(p3.name, p1.age)
print(p3.get_birth_year())

print(Person2.gera_id())
print(p1.gera_id())