''' functions in python'''

def right_justify(word, n):
    m = n - len(word)
    message = ' ' * m + word

    print(message)

#right_justify('morty', 70)

def do_twice(n, f):
    for i in range(n):
        f()


def print_spam():
    print('spam')

do_twice(2,print_spam)