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
print(bicycles)
print(bicycles[0].title()) #first element os th list with fisrt letter upper
print(bicycles[1]) # second element
print(bicycles[3]) # fourth element (last element of the list)
print(bicycles[-1]) # last element of the list (fourth element)
