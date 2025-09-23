'''
Escribir en Python una función que reciba una matriz cuadrada (lista de
listas) de enteros y devuelva True si esa matriz es diagonal superior
(los elementos que están debajo de la diagonal principal, la que va de
1,1 a n,n, deben ser 0), False de lo contrario.
'''

def diagonal_sup(matriz):
    '''
    >>> diagonal_sup([[5, 6, 2], [5, 5, 1], [0, 0, 3]])
    False
    >>> diagonal_sup([[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 5, 2], [0, 0, 0, 9]])
    True
    '''
    diagonal = True
    i = 1
    while diagonal and i<len(matriz):
        j = 0
        while diagonal and j<i: #así se garantiza que j deje de iterar en la diagonal
            if matriz[i][j] != 0:
                diagonal = False
            j += 1
    
        i += 1

    return diagonal

import doctest
print(doctest.testmod())