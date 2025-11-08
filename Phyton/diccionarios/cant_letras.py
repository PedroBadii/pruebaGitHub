                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''Programar una función que dada una palabra, calcule la
cantidad de veces que esta cada una de las letras que
contiene
'''

def cant_letras(palabra):
    ''' 
    >>> cant_letras('palapa')
    {'p': 2, 'a': 3, 'l': 1}
    '''
    cant_letras = {}
    for letra in palabra:
        if letra in cant_letras:
            cant_letras[letra] += 1
        else:
            cant_letras[letra] = 1
    
    return cant_letras

import doctest
print(doctest.testmod())