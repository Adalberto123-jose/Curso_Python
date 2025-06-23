# SETS

# lOS SET no tienen ningun tipo de orden a diferencia de las listas
my_set = {}
print(type(my_set))

my_set = {'Python','Java','C++'}
print(type(my_set))

print(my_set)

# print(my_set[0]) TypeErrror: 'set' object is not subscriptable

# Los set no aceptan repetidos
my_set.add('C++')
print(my_set)
my_set.add('C#')

#Esto es para identificar la diferencia con otro set
my_set_0= {'Python','Java','C++'}

my_set.difference_update(my_set_0)
print(my_set)
