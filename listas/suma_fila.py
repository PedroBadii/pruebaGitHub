                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir en Python una función que reciba una matriz (lista de listas) de
enteros y devuelva una lista en donde el elemento i sea la suma de la
fila i de la matriz.
'''

def suma_fila (matriz):
    '''
    >>> suma_fila([[5, 6, 2], [5, 5, 1], [0, 0, 3], [2, 3, 5]])
    [13, 11, 3, 10]
    >>> suma_fila([[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 5, 2], [0, 0, 0, 9]])
    [10, 6, 7, 9]
    '''
    suma_filas = []
    for fila in matriz:
        total_fila = 0
        for i in fila:
            total_fila += i
        suma_filas.append(total_fila)

    return suma_filas

import doctest
print(doctest.testmod())
