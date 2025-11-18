                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba una cadena de caracteres a validar, y un segundo parámetro, que
contenga una cadena con los caracteres válidos. La función debe devolver True, si la cadena a validar, está
formada sólo por caracteres válidos; en caso contrario, deberá devolver False. 
'''

def caracteres_validos(cadena, caracteres_validos):
    '''
    >>> caracteres_validos('Aa!2', 'Aa!2')
    True
    >>> caracteres_validos('aA1#!', 'ASDFasdf1234!"#$')
    True
    >>> caracteres_validos('987=&%', 'ASDFasdf1234!"#$')
    False
    >>> caracteres_validos('546', '')
    False
    '''
    valida = True
    i = 0
    while valida and i<len(cadena):
        if not cadena[i] in caracteres_validos:
            valida = False
        i += 1

    return valida

import doctest
print(doctest.testmod())