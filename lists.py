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