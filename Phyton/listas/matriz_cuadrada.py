                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir en Python una función que reciba una matriz (lista de listas) de
enteros y devuelva True si esa matriz es cuadrada (las filas y las
columnas tienen que ser de la misma longitud), False de lo contrario
'''

def es_cuadrada(matriz):
    '''
    >>> es_cuadrada([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> es_cuadrada([[1, 2, 3], [4, 5, 6]])
    False
    '''
    es_cuadrada = True
    i = 0
    while es_cuadrada and i<len(matriz):
        if len(matriz[i]) != len(matriz):
            es_cuadrada = False
        i += 1

    return es_cuadrada

import doctest
print(doctest.testmod())

'''
Otra opción es esta:

def es_cuadrada(matriz)
    return all(len(fila) == len(matriz) for fila in matriz)

all devuelve True si para todas las iteraciones de «for fila in matriz» len(fila) == len(matriz) es True
'''