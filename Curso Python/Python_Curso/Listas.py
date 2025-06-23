# LISTAS

my_list = ['Python', 53, False,43, 'Hola mundo']
print(type(my_list))

print(my_list)
# Esto sirve para buscar en la lista lo que buscamos
print(my_list[1])
# El append sirve para añadir un objeto en la lista
my_list.append(53)
print(my_list)
# El insert sirve para añadir un objeto en la lista donde queramos
my_list.insert(3, 'suscribanse')
print(my_list)
# El remove quita lo que queramos en la lista
my_list.remove('Hola mundo')
print(my_list)
# El pop quita lo que quieramos en la posicion que le digamos
print(my_list.pop(2))
print(my_list)
# El count cuenta el numero de veces de esa variables que le digas
print(my_list.count(53))
# El reverse pone la lista arreves
my_list.reverse()
print(my_list)
# El clear borra toda la lista y la deja limpia
my_list.clear()
print(my_list)

# !HAY MUCHAS MAS FUNCIONES PARA LAS LISTAS! 