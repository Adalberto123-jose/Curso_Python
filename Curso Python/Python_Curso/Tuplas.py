# TUPLAS

my_tupla = (53,'perro',7.4,True)
print(type(my_tupla))
# Sirve para buscar lo que queramos en la tupla
print(my_tupla[1])
# El count cuenta el numero de veces del objeto
print(my_tupla.count(53))
# Index encuentra lo que nosotros queramos
print(my_tupla.index(7.4))

# Las tuplas no se pueden modificar

# Tipado debil significa que podemos cambiar una variable
# por otra variable

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla.pop()
print(my_tupla)

my_tupla = tuple(my_tupla)
print(type(my_tupla))
print(my_tupla)

