# Strings
# Los string los puedes hacer con comillas dobles o con comillas simples
mi_firts_string ="mi string con comillas dobles"
mi_second_string = 'mi string con comillas simples'

print(mi_firts_string, mi_second_string)
print('esto es un texto de una variables ' + mi_firts_string + ' ' + mi_second_string)

print(f'esto es un texto de una variable{mi_second_string} hola mundo' )

# String con diferentes variables
other_string = 'hola'

a,b,c,d = other_string

print(a)
print(b)
print(c)
print(d)

print(f'{a}{b}{c}{d}')

#funciones mas comunes que se pueden utilizar en un string
print(mi_firts_string.upper())
print(mi_firts_string.capitalize())
print(mi_firts_string.lower())
print(len(mi_firts_string))
print(mi_firts_string.find())
print(mi_firts_string.count())
print(mi_firts_string.upper().isupper)
print(mi_firts_string.lower().isupper)
