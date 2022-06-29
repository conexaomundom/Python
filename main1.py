''' it is possible to create a variable inside a class
called class variable
and to instance this variable
 in this way I can print tht vc variable using instances
 and you can call diretly the class variable as n line 16
'''
'''
class A:
    vc = 123

a = A()
b = A()

print(a.vc,b.vc)

print(A.vc)
'''
'''It's possible to change the class variable using
the proper class like in the line 26
and it's also possible to change the instance that its using
the class variable like in line 28 that change in all instances
but the changing is diffente like you can see on the dictionary
out put called in lines 30, 31 and 32
'''
'''
#A.vc = 321

a.vc = 321

print(A.__dict__)
print(a.__dict__)
print(b.__dict__)'''

''' access modifers
methods and attribuers
public - they can be access inside and outside of the class
protected - they can be access only inside of the class or by class's children
private - it is only avaliable inside of the class
'''

class DataBase:
    # constructior
    def __init__(self):
        # an empty dictionary
        self.data = {}

    def putting_customers(self, id, name):
        if 'customers' not in self.data:
            self.data['customers'] = {id: name}
        else:
            self.data['customers'].update({id: name})

    def customer_list(self):
        for id, name in self.data['customers'].items():
            print(id,name)

    def errase_customer(self,id):
        del self.data['customers'][id]

# instantiating a class
bd = DataBase()
bd.putting_customers(1,'Marina Rodrigues')
bd.putting_customers(2,'Julio Garcia')
bd.putting_customers(3,'Regina Rodrigues')
print(bd.data)
bd.errase_customer(2)
print(bd.customer_list())
