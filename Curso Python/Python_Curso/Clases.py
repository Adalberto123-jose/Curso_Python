# CLASES

# la forma de llamar las clases es class
class unHumano:
    def __init__(self, altura, edad, peso): # Este es un constructor de clase
        self.altura = altura # self es la forma de guardar cosas
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        print(f'el humano de {self.edad} anos esta comiendo')

humano_1 = unHumano(1.80, 23, 87)
print(f'el humano 1 mide {humano_1.altura}, pesa {humano_1.peso}kg y tiene {humano_1.edad} anos')

humano_1.comer()
