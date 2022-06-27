# Python lists

# A list can has a sigle type of element or elements 
# of different types
# square brackets represent lists in python

bicycles = ['treck','cannodale','redline','specialized']
#print(bicycles)
#print(bicycles[0]) #first elemento of the list

"""It is possible to use methods in elements of a list
but not for the ful list because results an error:
'list' object has no attribute 'title'
"""
"""
print(bicycles)
print(bicycles[0].title()) #first element os th list with fisrt letter upper
print(bicycles[1]) # second element
print(bicycles[3]) # fourth element (last element of the list)
print(bicycles[-1]) # last element of the list (fourth element)"""

# using indidual values from a list 
mesage = 'My fisrt bicycle was a ' + bicycles[0].title() + '.'

#print(mesage)

''' One of the most fundamental data structures of python is list
A list is an ordered collection, as an array, but lists have 
other features '''

integer_list = [2,6,3]
heterogeneous_list = ['string', 0.1, True,False]
# [] is an empty list
# It is possible to have lists as elements of a list (lists within lists)
list_of_list = [integer_list, heterogeneous_list, []] 
list_length = len(heterogeneous_list)
list_sum = sum(integer_list)

# extending the values of a list (adding)
integer_list.extend([1,2,3,4,5,6,7,8,9])



''''But has another way, using the append 
but append accept only one argument.
integer_list.append(987)'''

''' Changing elements insid of the list 
integer_list[0] = 987 # changing the first element to 987
integer_list[-1] = 987 # changing the last ultimo element to 987'''

# maybe you can change several elements at the same time
'''integer_list[0:5] = [987, 987, 987,987, 987, 987,987, 987] 
print(integer_list)
If you put the same amount os element before e after will replace all 
rigth, if you put less element in the positions than in the extend 
new to be considered will add all as an extend from the element
the more and if you put less elements in more positions this will result in an error
'''

#using Insert() you can enter data by entering positions and what 
# will contain in this new position, without being adding at the end and not replacing
# any value

moto = ['honda', 'yamaha','suzuki']
print(moto)
moto.insert(2,'ducati')
print(moto)

# removing elements from the list using del permanently
# in any position of litapy
del moto[2]
print(moto)
