# EXCEPCIONES
 
# try y except  lo que haces es que si esto funciona sino manda un error
try:
    print(5 + '3')
   
except NameError as error: # para saber cual fue el error utilizamos as
    print('error de NameError')
    print(error)
except TypeError:
    print('eror de TypoErrror')
else: # El else funciona con las excepciones pero si funciona el try sino no sirve
    print('hola mundo')
finally: # Pase lo que pase si el codigo no sirve finally imprime lo que le mandemos
    print('Hola bro')
    
