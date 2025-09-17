'''
Definir una función en Python que recibe un string y valida que sea una clave
correcta. Para que sea correcta debe tener
-una longitud de entre 8 y 12 caracteres
-por lo menos una mayúscula
por lo menos una minúscula
por lo menos un dígito numérico
por lo menos un símbolo: $, -, @
Devolver true si cumple, false si no. Anotar casos de prueba.
'''

def clave_correcta(clave):
    '''
    >>> clave_correcta('ASDasd4$12')
    True
    >>> clave_correcta('Pedro1996')
    False
    >>> clave_correcta('Pedro@1996')
    True
    >>> clave_correcta('Pikachu&2')
    False
    >>> clave_correcta('1$aA')
    False
    '''
    valido = True #este es el que se usa para cortar el while si encontramos algo mal
    largo = True
    min = False
    may = False
    dig = False
    sim = False
    lis_sim = ['$', '-', '@']
    MAYUS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    MINUS = MAYUS.lower()

    if 8>len(clave) or len(clave)>12:
        largo = False
    else:
        i=0
        while (i<len(clave) and valido):
            if (clave[i] in MAYUS):
                may = True
            elif (clave[i] in MINUS):
                min = True
            elif (clave[i].isdigit()):
                dig = True
            elif (clave[i] in lis_sim):
                sim = True
            else:
                valido = False
            
            i += 1

    if (valido):
        if not (may and min and dig and sim and largo):
                valido = False
        
    return valido

import doctest
print(doctest.testmod())