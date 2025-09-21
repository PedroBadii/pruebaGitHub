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
    >>> factorial(-3)
    0
    >>> factorial(2.6)
    0
    '''
    resultado = 1
    if num % 1 == 0 and num >= 0: #num tiene que ser entero y mayor o igual a 0
        for i in range(1, num+1):
            resultado *= i
    else:
        resultado = 0

    return resultado

import doctest
print(doctest.testmod())


