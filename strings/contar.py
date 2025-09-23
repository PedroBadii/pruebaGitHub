
'''
Escribir una función contar que reciba una cadena de caracteres y
devuelve un entero que indica la cantidad de caracteres alfabéticos
distintos que tiene la cadena. No debe distinguir mayúsculas de
minúsculas ni caracteres con tilde.
Llamado                                Devolución            Observaciones
contar(“Aaaaáb”)                           2             Hay dos caracteres distintos:a y b
contar(“$_12 3*”)                          0             Números, símbolos y espacios no cuentan
contar(“Algoritmos y Programación 1”)      13             A, l, g, o, r, i, t, m, s, y, P, c, n
'''

def contar(cadena): #FALTA DIFERENCIAR MINÚSCULAS DE MAYÚSCULAS
    '''
    >>> contar('Aaaaáb')
    2
    >>> contar('$_12 3*')
    0
    >>> contar('Algoritmos y Programación 1')
    13
    '''
    cant_letras = 0
    cadena_min = cadena.lower()
    repetidas = []
    for letra in cadena_min:
        if letra.isalpha() and (not (letra in repetidas)):
            repetidas.append(letra)
            cant_letras += 1
    
    return cant_letras

import doctest
print(doctest.testmod())