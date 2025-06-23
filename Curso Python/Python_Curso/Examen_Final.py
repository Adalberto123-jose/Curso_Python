#Examen

# en una 'lista' de numero, retorna el segundo numero mas grande

# Ejemplo: [5,7,2,7,9,4,8]
# Respuesta: 8

lista = [5,7,2,7,9,4,8]
lista.sort() # Ordenamos la lista
print(lista[-2]) # Y lo leemos del ultimo en adelante para ver cual es el mayor

#  Crea una funcion que reciba dias, horas, minutos y segundo
# (como 'list") y retorne su resultado en milisegundos.

def miltime(dia = 0, horas = 0, minutos = 0, segundo = 0):
    final_time = 0
    horas =+ dia * 24
    minutos =+ horas * 60
    segundo =+ minutos * 60
    final_time =+ segundo * 1000
    print(final_time)
    
miltime(2,33,23,12)

# Escribe una función que muestre por consola los números 
# de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la #palabra "fizzbuzz".

def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and  a % 5 == 0:
            print('fizzbuzz')
        elif a % 3 == 0:
            print('fizz')
        elif a % 5 == 0:
            print('buzz')
        else:
            print(a)
            
fizzbuzz()