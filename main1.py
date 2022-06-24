''' it is possible to create a variable inside a class
called class variable
and to instance this variable
 in this way I can print tht vc variable using instances
 and you can call diretly the class variable as n line 16
'''

class A:
    vc = 123

a = A()
b = A()

print(a.vc,b.vc)

print(A.vc)

'''It's possible to change the class variable using
the proper class like in the line 26
and it's also possible to change the instance that its using
the class variable like in line 28 that change in all instances
but the changing is diffente like you can see on the dictionary
out put called in lines 30, 31 and 32
'''

#A.vc = 321

a.vc = 321

print(A.__dict__)
print(a.__dict__)
print(b.__dict__)