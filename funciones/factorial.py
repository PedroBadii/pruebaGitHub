                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba un valor y calcule el factorial del mismo.
Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado.
No debe imprimir el valor, debe solamente devolverlo.
Probá la función invoncándola desde el bloque principal, con al menos 3 valores.
'''
def factorial(num):

    '''
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    '''

    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado

import doctest
print(doctest.testmod())


