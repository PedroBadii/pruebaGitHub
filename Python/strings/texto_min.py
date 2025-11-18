
                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba por parámetro un texto todo en mayúsculas.
La función deberá devolver el texto pero respetando la regla que indica que luego de un
punto la primer letra debe ser mayúscula, y el resto minúsculas. 

'''

def texto_min (texto):
    '''
    >>> texto_min('ANITA LAVA LA TINA.POR QUE.NO LO SE.CHAU')
    'anita lava la tina.Por que.No lo se.Chau'
    '''
    texto_min = texto.lower()
    for i in range(1,len(texto_min)):
        if texto_min[i-1] == '.':
            texto_min = texto_min[:i] + texto_min[i].upper() + texto_min[i+1:]
    return texto_min

import doctest
print(doctest.testmod())




