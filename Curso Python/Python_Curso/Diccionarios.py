# DICCIONARIOS

# Los diccionarios tambien se crean con llaves pero con una diferencia

my_list = {'a' , 'b'}

print(type(my_list))
# Esta es la estructura correcta de un diccionario
my_dict = {'Nombre' : 'Nicolas' , 
           'Apellido': 'Gonzales' , 
           'Apodo': 'Tranformer'}

print(type(my_dict))

print(my_dict['Nombre'])

# Keys imprime todas las llaves del diccionario
print(my_dict.keys())

# values imprime todos los valores del diccionario
print(my_dict.values())
