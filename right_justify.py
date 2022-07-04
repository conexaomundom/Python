''' Exemples using unctions in python
    Book Think Python
'''

def right_justify(word, qtt):
    '''puts a qtt of blank space until the word
     '''
    message = ' ' * (qtt - len(word)) + word

    print(message)

# right_justify('morty', 70)

def do_twice(func, argument):
    ''' Puts the function to run twice
    
    func is the object that needs to be a funcion
    argument is the function argument     '''
    func(argument)
    func(argument)


def print_spam():
    print('spam')

#do_twice(2,print_spam)

def print_twice(name):
    print(name)
    print(name)
    
# print_twice('spam')
# do_twice(print_twice, 'spam')

def do_four(func, argument):
    ''' Puts the function to run four times '''
    do_twice(func, argument)
    do_twice(func, argument)


# do_four(print,'spam')

def grade():
    ''' Prints grades

    squares are how many squares the user wants
    '''
    plus = '+ '
    menus = '- '
    other = '|'

    print(plus + menus * 4 + plus + menus * 4 + plus)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(plus + menus * 4 + plus + menus * 4 + plus)

 #   print(plus + menus * 4 + plus + menus * 4 + plus)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(other + ' ' * 9 + other + ' ' * 9 + other)
    print(plus + menus * 4 + plus + menus * 4 + plus)

grade()
