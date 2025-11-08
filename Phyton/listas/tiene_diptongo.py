                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba una palabra, y devuelva True, si la palabra tiene diptongo, y
False, en caso contrario.
Asumir que la palabra recibida, solo esta formada por letras.
En español dos vocales en contacto se articulan como diptongo cuando:
1. una es cerrada (i u) átona (no acentuada) y la otra es abierta (a e o) y viceversa.
2. ambas son cerradas, excepto si son iguales (como en chiita), donde forman un hiato
'''

def tiene_diptongo(palabra):
    '''
    >>> tiene_diptongo('perro')
    False
    >>> tiene_diptongo('hiato')
    True
    >>> tiene_diptongo('aire')
    True
    >>> tiene_diptongo('ofiuco')
    True
    >>> tiene_diptongo('chiita')
    False

    '''
    diptongo = False
    vocales_cerradas = ['i', 'u']
    vocales_abiertas = ['a', 'e', 'o']
    
    for i in range(len(palabra)-1):
        if (palabra[i] in vocales_cerradas and palabra[i+1] in vocales_abiertas) or \
        (palabra[i] in vocales_abiertas and palabra[i+1] in vocales_cerradas) or \
        (palabra[i] in vocales_cerradas and palabra[i+1] in vocales_cerradas and palabra[i] != palabra[i+1]):
            diptongo = True

    return diptongo

import doctest
print(doctest.testmod())
