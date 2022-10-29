# lists
from traceback import print_tb


x = list()
y = ['a', 25, 'dog', 7.32]
tuple1 = (10, 20)
z = list(tuple1)
print(z)

#tuples
tuple = (1, 2, 3)
print(tuple)
tuple_list = ([1,2], 3)
del(tuple_list[0][1])
print(tuple_list)
tuple_list+= (4,)
print(tuple_list)

#sets
set1 = {3, 5, 3, 5}
print(set1)
s = set()
print(s)
list1 = [2, 3, 4]
z = set(list1)
print(z)

#dictionaries
dict1 = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(dict1)
dict1 = dict ([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
print(dict1)
dict1 = dict(pork= 25.3, beef= 33.8, chicken= 22.7)
print(dict1)

dict1['shrimp'] = 38.2 #add or update
del(dict1['shrimp']) #delate