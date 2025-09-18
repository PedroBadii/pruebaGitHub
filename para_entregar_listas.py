                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Definir una función que reciba tres parámetros que corresponden al día, mes y año de una fecha y
 devuelva el valor de verdad True ó False de acuerdo a si los valores recibidos corresponden a 
 una fecha válida ó no. Indicar algunos casos de prueba, válidos e inválidos utilizando los conceptos
   de DOCTEST.
'''
meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]

def anio_bisiesto (anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def mes_correcto(mes):
    return 1<=mes<=12

def dia_correcto(dia,mes,anio):
    dia_es_correcto = True
    if (mes == 2 and dia > 28 and not anio_bisiesto(anio)) or \
    (mes == 2 and dia > 29) or (dia > 31) or (dia > 30 and mes in meses_30):
        dia_es_correcto = False
    return dia_es_correcto

def fecha_correcta (dia,mes,anio):
    '''
    >>> fecha_correcta(12, 9, 2025)
    'La fecha es válida'
    >>> fecha_correcta(29, 2, 2025)
    'La fecha no es válida'
    >>> fecha_correcta(29, 2, 2024)
    'La fecha es válida'
    >>> fecha_correcta(31, 4, 1955)
    'La fecha no es válida'
    >>> fecha_correcta(32, 10, 1750)
    'La fecha no es válida'
    >>> fecha_correcta(5, 14, 100)
    'La fecha no es válida'
    '''
    valida = ''
    if mes_correcto(mes) and dia_correcto(dia,mes,anio):
        valida = 'La fecha es válida'
    else:
        valida = 'La fecha no es válida'
    return valida

import doctest
print(doctest.testmod())