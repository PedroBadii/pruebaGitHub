                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba una cadena de caracteres. La función deberá evaluar si la cadena recibida
representa un número binario, y en ese caso devolver True, de lo contrario, deberá devolver False.
'''

def es_binario(num): #num es una cadena con numeros
    '''
    >>> es_binario('101101')
    True
    >>> es_binario('1j010')
    False
    >>> es_binario('189012')
    False
    '''
    binario = True
    i = 0
    while binario and i<len(num):
        if num[i] != '1' and num[i] != '0':
            binario = False
        i += 1
    
    return binario

import doctest
print(doctest.testmod())
        
