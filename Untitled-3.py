"""Entrada de dados - AULA 3"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nascimento = 2022-int(idade)
print('')
print(f'O usuário digitou {nome} e o tipo de variável é 'f'{type(nome)}')
print('')
print(f'{nome} tem {idade} anos')
print('')
print(f'{nome} nasceu em {ano_nascimento}')

n_1 = int(input('Digite um número: '))
n_2 = int(input('Digite outro número: '))

print(n_1 + n_2)

v = '5.5'
o_v = (int(float(v)))
print(type(o_v))