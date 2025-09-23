                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir en Python una función que reciba una matriz (lista de listas) de
enteros y devuelva una lista en donde el elemento i sea la suma de la
columna i de la matriz.
'''

def suma_columna(matriz):
    '''
    >>> suma_columna([[5, 6, 2], [5, 5, 1], [0, 0, 3]])
    [10, 11, 6]
    >>> suma_columna([[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 5, 2], [0, 0, 0, 9]])
    [1, 3, 10, 18]
    '''
    suma = [0] * len(matriz[0]) #esto me devuelve una lista en ceros con el len de matriz
    for lista in matriz:
        for i in range(len(lista)):
            suma[i] += lista[i]

    return suma

import doctest
print(doctest.testmod())