meses_31 = ["enero","marzo","mayo","julio","agosto","octubre", "diciembre"]
meses_30 = ["abril","junio","septiembre","noviembre"]
anio = int(input("Ingrese un año: "))
mes = (input("Ingrese un mes con letras: ")).lower()
dia = int(input("Ingrese un dia: "))

def anio_bisiesto (anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def mes_correcto(mes):
    return mes in meses_31 or mes in meses_30 or mes == "febrero"

def dia_correcto(dia):
    dia_es_correcto = True
    if (mes == "febrero" and dia > 28 and not anio_bisiesto(anio)) or \
    (mes == "febrero" and dia > 29) or (dia > 31) or (dia > 30 and mes in meses_30):
        dia_es_correcto = False
    return dia_es_correcto

def fecha_correcta ():
    """
    >>> fecha_correcta(30, "febrero", 2023)
    False
    >>> fecha_correcta(5, "julio", 1958)
    True
    >>> fecha_correcta(29, "febrero", 2000)
    True
    >>> fecha_correcta(31, "abril", 1996)
    False
    >>> fecha_correcta(72, "junio", 1999)
    False
    """
    if mes_correcto(mes) and dia_correcto(dia):
        print ("La fecha es válida")
    else:
        print ("La fecha no es válida")

fecha_correcta ()

import doctest
doctest.testmod()