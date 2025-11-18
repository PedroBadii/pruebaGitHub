                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir en Python una función que reciba una matriz cuadrada (lista de
listas) de enteros y devuelva True si esa matriz es la identidad, (los de
la diagonal principal, la que va de 1,1 a n,n, deben ser 1 y todos los
demás, 0), False de lo contrario.
'''

def es_identidad(matriz):
    '''
    >>> es_identidad([[5, 6, 2], [5, 5, 1], [0, 0, 3]])
    False
    >>> es_identidad([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    True
    '''

    identidad = True
    i = 0
    while identidad and i<len(matriz):
        j = 0
        while identidad and j<len(matriz[i]): #lo pongo así por claridad pero len(matriz)==len(matriz[i])
            if (i==j and matriz[i][j] != 1) or (i != j and matriz[i][j]!= 0):
                identidad = False
            j += 1
        
        i += 1
    
    return identidad

import doctest
print(doctest.testmod())
