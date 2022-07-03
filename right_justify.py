''' functions in python'''

def right_justify(word, n):
    m = n - len(word)
    message = ' ' * m + word

    print(message)

#right_justify('morty', 70)

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)