#Programa que comprueba una serie de input

import re

def compruebaExpresiones():

    test_1 = input("Introduzca una expresion con el siguiente formato: 'Palabra seguida de espacio y una letra': ")
    print("Resultado test_1: {}".format(bool(re.search(r'^\w\s+[A-Z]$', test_1))))

    test_2 = input("Introduzca una direccion de correo electronico: ")
    print("Resultado test_2: {}".format(bool(re.search(r'^[a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', test_2))))

    test_3 = input("Introduzca una tarjeta de crédito: ")
    print("Resultado test_3: {}".format(bool(re.search(r'^[0-9]{4}([\s-]){1}[0-9]{4}\1[0-9]{4}\1[0-9]{4}$', test_3))))


compruebaExpresiones()
