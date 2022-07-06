import turtle

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


polygon(bob,7,70)