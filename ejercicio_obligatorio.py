meses_31 = ['enero','marzo','mayo','julio','agosto','octubre', 'diciembre']
meses_30 = ['abril','junio','septiembre','noviembre']

def anio_bisiesto (anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def mes_correcto(mes):
    return mes in meses_31 or mes in meses_30 or mes == 'febrero'

def dia_correcto(dia,mes,anio):
    dia_es_correcto = True
    if (mes == 'febrero' and dia > 28 and not anio_bisiesto(anio)) or \
    (mes == 'febrero' and dia > 29) or (dia > 31) or (dia > 30 and mes in meses_30):
        dia_es_correcto = False
    return dia_es_correcto

def fecha_correcta (dia,mes,anio):
    '''
    >>> fecha_correcta(12,'septiembre',2025)
    'La fecha es válida'
    >>> fecha_correcta(29,'febrero',2025)
    'La fecha no es válida'
    >>> fecha_correcta(29,'febrero',2024)
    'La fecha es válida'
    >>> fecha_correcta(31,'abril',1955)
    'La fecha no es válida'
    >>> fecha_correcta(32,'octubre',1750)
    'La fecha no es válida'
    >>> fecha_correcta(5,'setiembre',100)
    'La fecha no es válida'
    '''
    valida = ''
    if mes_correcto(mes) and dia_correcto(dia,mes,anio):
        valida = 'La fecha es válida'
    else:
        valida = 'La fecha no es válida'
    return valida

def main ():
    anio = int(input('Ingrese un año: '))
    mes = (input('Ingrese un mes con letras: ')).lower()
    dia = int(input('Ingrese un dia: '))

    fecha_correcta (dia,mes,anio)

#main()

import doctest
doctest.testmod(verbose=True)