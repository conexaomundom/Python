import turtle
import math

bob = turtle.Turtle()
'''
# A square using turtle
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

# another way to do
'''

# Function square

def square(t):
    for i in range(4):
        t.lt(100)
        t.fd(90)

# square(bob)

def polygon(t,n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polygon(bob,7,70)

'''generalizing and clearing the code'''

def circle(t, r):
    '''Drawing a circle using turtle'''
    circunference = 2 * math.pi * r
    n = int(circunference / 3) + 1
    length = circunference / n
    polygon(t, n, length)

# circle(bob,70)


def circle(t, r, angle):
    '''Drawing a arc using turtle'''
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    
    polygon(t, n, length)

