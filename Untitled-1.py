##nome = 'Marina Rodrigues'
#idade = 24
#altura = 1.77
#e_maior = idade >= 18
#peso = 83.500
#imc = peso / (altura ** 2)

#print(nome, 'tem', idade, 'anos de idade e seu imc é', imc, sep=' ')
#print(f'{nome} tem {idade} anos de idade e seu imc é {imc:2f}')
#print('{} tem {} anos de idade e seu imc é {:2f}'.format(nome, idade, imc))
#print('{0} tem {1} anos {0} de {2} idade e seu imc é {2:2f}'.format(nome, idade, imc))
#print('{a} tem {b} anos {a} de {c} idade e seu imc é {c:2f}'.format(a = nome, b = idade, c = imc))

"""
Condições IF, ELIF, e ELSE - AULA 4
"""

#if True:
#    print('Verdadeiro.')

#    n1 = 2
#    n2 = 4

#    print(n1+n2)

#f False:
#    print('Verdadeiro.')
#    print('A MINHA EXPRESSÃO NÃO É VERDADEIRA.')

#if False:                
#    print('True')
#elif True:
#    print('Agora nesse meio termo teve uma condição verdadeira')
#else:
#    print('ELSEE')

"""
Operadores relacionais - AULA 4
== > >= < <= !=
"""

print(2 == 2)
print(2 == '2')

##

num1 = 2 # int
num2 = '1'  #string
print(num1, num2)

expressao = num1 == num2
print(expressao)

##

var1 = 'Marina'
var2 = 'Rodrigues'
expressao = var1 != var2
print(expressao)

##

#nome = input('Qual o seu nome? ')
#idade = int(input('Qual a sua idade? '))

# Limite para pegar emprestimo
#idade_limite = 18

#if idade >= idade_limite:
#    print(f'{nome} pode pegar o empréstimo.')
#else:
#    print(f'{nome} Não pode pegar o empréstimo')

#nome = 'joaozinho'
#idade = """40"""
#peso = 40.5
#e_maior = True
#idade = int(idade)

#if idade > 18:
#    print(f'{nome} é maior de idade')
#else:
#    print(f'{nome} Não é maior de idade')

"""Operadores lógicos -  AULA 4
and, or, not, in e not in
"""
#a = 0
#if not a:
#    print('preecha o valor de a')
#else:
#    print(f'O valor de a é {a}')


#usuario = input('Nome do usuário: ')
#senha = input('Senha do usuário: ')

#usuario_bd = 'Marina'
#senha_bd = '123456'

#if usuario_bd == usuario and senha_bd == senha:
#    print('Você está logado no sistema')
#else:
#    print('Usuário ou senha inválidos')

if False:
    print('Um')
elif False:
    print('Dois')
    