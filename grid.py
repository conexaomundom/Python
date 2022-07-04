# We will do a grid using functions

def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def print_firstRow():
    print('+ - - - - ', end = ' ')

def print_second_():
    print('|         ', end = ' ')

def print_rows():
    do_twice(print_firstRow)
    print('+')

def print_posts():
    do_twice(print_second_)
    print('|')

def print_grid():
        print_rows()
        do_four(print_posts)
        print_rows()

print_grid()
