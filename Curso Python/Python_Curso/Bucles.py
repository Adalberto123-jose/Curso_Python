# BUCLES
# Bucles o luts sirve para que se repita algo hasta que indicamos que no se repita

# While es como un If pero que dice que esto se repetira hasta que no se cumpla la condicion
numero = 0
while numero < 10:
    numero += 1
    print(numero)
    if numero == 5:
        print('es un menor que 5')
        break # Lo que hace es terminar todo el bucle hasta donde lo digamos 

print('hola mundo')

lista = [76,43,2,6,7,123]
for number in range(101):
    print(number)
    if number == 5:
        print('es un menor que 5')
        break