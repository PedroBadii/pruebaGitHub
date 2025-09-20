                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba el número de un mes, y devuelva el nombre del mes.
Por ejemplo, si la función recibe un "1", deberá devolver: "Enero"; si recibe un "2", deberá 
devolver: "Febrero"; y así con el resto de los valores.
En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido".
No debe imprimir el nombre del mes, sólo devolver la cadena correspondiente.
Probá la función invoncándola desde el bloque principal, con al menos 3 valores.

Para la construcción del programa, podés utilizar el editor del intérprete o el ide que prefieras.
Luego copia y pega lo que hayas hecho en la caja de texto de esta actividad y efectuá la entrega 
de la misma.
'''

def numero_mes (numero):
    '''
    >>> numero_mes(5)
    'Mayo'
    >>> numero_mes(1)
    'Enero'
    >>> numero_mes(12)
    'Diciembre'
    >>> numero_mes(13)
    'El año solo tiene doce meses'
    '''
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', \
            'Octubre', 'Noviembre', 'Diciembre']

    mes = ''
    if 1<=numero<=12:
        mes = meses[numero-1]
    else:
        mes = 'El año solo tiene doce meses'

    return mes

import doctest
print(doctest.testmod())
    