#primero cargo los parámetros de las funciones

meses_31 = ["enero","marzo","mayo","julio","agosto","octubre", "diciembre"]
meses_30 = ["abril","junio","septiembre","noviembre"]
febrero = "febrero"

def anio_correcto (anio):
    return len(anio)=4

def mes_correcto(mes):
    lower(mes)
    return mes in meses_31 or mes in meses_30 or mes = "febrero"

def dia_correcto(dia):
    dia_es_correcto = True
    if dia > 31:
        dia_es_correcto = False
    elif dia > 30 and mes in meses_30:
        dia_es_correcto = False
    if dia > 29 and mes = "febrero"
        dia_es_correcto = False


def main ():
anio = int(input("Ingrese un año: "))
mes =  input("Ingrese un mes con letras: ")
dia = int(input("Ingrese un dia: "))
print(anio_correcto and mes_correcto and dia_correcto)