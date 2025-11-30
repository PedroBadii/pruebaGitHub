'''
La ferretería Fede Reía tiene dos sucursales y por cada una guarda un registro diario de cada venta realizada.
Este registro se cierra mensualmente en un archivo CSV (ventas1.csv y ventas2.csv), por lo que queda ordenado
 por día, con el siguiente formato:

dia,codigo_producto,cantidad_vendida

ventas1.csv    dia,codigo_producto,cantidad_vendida ordenado por día
ventas2.csv    dia,codigo_producto,cantidad_vendida ordenado por día

Ejemplo:
1,176,12
1,45,1

Además, se cuenta con un diccionario reposicion, ya cargado, con los códigos de artículos como clave y una 
lista con dos valores: la descripción del artículo y el nivel de ventas de cada artículo para solicitar 
reposición. Por ejemplo, si del artículo 45 se vendieron 3 unidades y el nivel de reposición es 10, no hay 
que solicitar ninguna reposición. En cambio, si se vendieron 13 unidades, hay que reponer solo 3 (la resta 
de la cantidad vendida menos el nivel de reposición).

Si aceptas la misión, deberás realizar un programa en Python que:

Recorriendo una sola vez los archivos de ventas y sin cargarlos completamente en memoria, haga un merge de 
ambos archivos, agregando en cada línea SUC_1 o SUC_2, dependiendo de dónde proviene la información. Este 
archivo unificado, debe estar ordenado por día, y ante igualdad de día, en primer lugar, deben estar las 
ventas de la sucursal 1.

diccionario_reposicion = {1:['tornillos', 10], 2: ['tuercas', 20] }

códigos de artículos como clave y una lista con dos valores: la descripción del artículo y el nivel de 
ventas de cada artículo para solicitar reposición
'''

DIA_MAYOR = 40

def leer (ventas):

    linea = ventas.readline()

    if linea: #si la linea es distinto de vacío
        linea = linea.rstrip()
        dia, codigo, cant_vendida = linea.split(',')
        datos = [int(dia), int(codigo), int(cant_vendida)]
    else:
        datos = [DIA_MAYOR, 0, 0]

    #opcion 1: hay datos: ['1', '176','12']
    #opcion 2: no hay datos: ['40', '', '']

    return datos


def merge (ventas_1, ventas_2, ventas_completas, dicc_rep):

    dicc_ventas= {}
     
    dia_1, cod_prod_1, u_vendidas_1 = leer(ventas_1)
    dia_2, cod_prod_2, u_vendidas_2 = leer(ventas_2)

    while (dia_1 < DIA_MAYOR) or (dia_2 < DIA_MAYOR): #mientras haya datos en algun archivo

        if dia_1 <= dia_2:
            ventas_completas.write(f'{dia_1},{cod_prod_1},{u_vendidas_1}, SUC_1\n')

            if cod_prod_1 not in dicc_ventas: #agrego las ventas al dicc
                dicc_ventas[cod_prod_1] = u_vendidas_1
            else:
                dicc_ventas[cod_prod_1] += u_vendidas_1

            dia_1, cod_prod_1, u_vendidas_1 = leer(ventas_1) #leo la proxima linea

        elif dia_2  < dia_1:
            ventas_completas.write(f'{dia_2},{cod_prod_2},{u_vendidas_2}, SUC_2\n')

            if cod_prod_2 not in dicc_ventas:
                dicc_ventas[cod_prod_2] = u_vendidas_2
            else:
                dicc_ventas[cod_prod_2] += u_vendidas_2

            dia_2, cod_prod_2, u_vendidas_2 = leer(ventas_2)

    return dicc_ventas

'''
ejemplo
dicc_rep = {1:['tornillos', 10], 2: ['tuercas', 20] }
dicc_ventas = {1: 15, 2: 19}

'''
def solicitar_rep (dicc_rep, dicc_ventas):

    U_VENDIDAS = 1
    DESCRIPCION = 0

    for codigo in dicc_rep:

        if codigo in dicc_ventas:

            if dicc_ventas[codigo] > dicc_rep[codigo][U_VENDIDAS]:
                print(f'Se deben reponer {dicc_ventas[codigo]-dicc_rep[codigo][U_VENDIDAS]} unidades de {dicc_rep[codigo][DESCRIPCION]}')



def main ():
    dicc_rep = {1:['tornillos', 10], 2: ['tuercas', 20]}
    ventas_1 = open('Python\\archivos de texto\\ferreteria\\ventas1.csv', 'r')
    ventas_2 = open('Python\\archivos de texto\\ferreteria\\ventas2.csv', 'r')
    ventas_completas = open('Python\\archivos de texto\\ferreteria\\ventas_completas.csv', 'w')

    dicc_ventas = merge (ventas_1, ventas_2, ventas_completas, dicc_rep)

    ventas_1.close()
    ventas_2.close()
    ventas_completas.close()

    solicitar_rep (dicc_rep, dicc_ventas)

main()