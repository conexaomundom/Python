nome = 'Marina Rodrigues'
idade = 24
altura = 1.77
e_maior = idade >= 18
peso = 83.500
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc, sep=' ')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:2f}')
print('{} tem {} anos de idade e seu imc é {:2f}'.format(nome, idade, imc))
print('{0} tem {1} anos {0} de {2} idade e seu imc é {2:2f}'.format(nome, idade, imc))
print('{a} tem {b} anos {a} de {c} idade e seu imc é {c:2f}'.format(a = nome, b = idade, c = imc))