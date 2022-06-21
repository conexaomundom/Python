# 2.3 someone's name and print a mesage from him
name = 'Julio Garcia' #input('whats is your name? \n')
mesage = 'Olá ' + name.title() + ', would you like to learn a litlle about python today?'
print(mesage)
print('\n\n\n\n\n\n\n')

# all letters lower, then upper and only the first letters upper
name = 'NAME OF SOMEONE'
print(name.lower())
print(name.upper())
print(name.title())
print('\n\n\n\n\n\n\n')

# take a famous quote and show the quote with the autor name

autor = 'bill gates'
citacao = '“Tente uma, duas, três vezes e se possível tente a quarta, a quinta e \nquantas vezes for necessário. Só não desista nas primeiras tentativas, a \npersistência é amiga da conquista. Se você quer chegar aonde a maioria não\n chega, faça o que a maioria não faz.”'
mesage = autor.title() + ' once said:\n' + citacao
print(mesage)

# deleting blank characters
space_name = '\n\t' + autor + '\n\n\t' + name

print(space_name)
print(space_name.rstrip()) # left
print(space_name.rstrip()) #right
print(space_name.strip()) #all


# 2.8 do operations taht resulting 8 
print(4 + 4)
print(24 - 16)
print(1 * 4)
print(32 / 4)

# 2.9 create a variable with a number and show this number in a mesage
fav_num = 73
print('My favorite number is ' + str(fav_num) + '!\nPs: Dr. Sheldon Cooper knows why.')