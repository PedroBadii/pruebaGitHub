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

diccionario_reposicion = {001:['tornillos', 10], '002': ['tuercas', 20] }

códigos de artículos como clave y una lista con dos valores: la descripción del artículo y el nivel de 
ventas de cada artículo para solicitar reposición
'''
#NO FUNCIONA
COD_PRODUCTO = 1
CANT_VENTAS = 2

def merge (ventas_1, ventas_2):
    ventas_completas = open('\\ventas_completas.csv','w')
    dicc_ventas_totales = {}

    linea_v1 = ventas_1.readline().strip()
    linea_v2= ventas_2.readline().strip()

    while linea_v1 or linea_v2 :

        #si solo hay datos en linea_v2 o si el dia linea_v2 es mas chico que el de linea_v1
        if not (linea_v1) or (int(linea_v1.split(',')[0]) >= int(linea_v2.split(',')[0])): 

            #en ese caso escribo linea_v2
            ventas_completas.write(f'{linea_v2}, SUC_2\n')
            linea_v2 = ventas_2.readline().strip()

            codigo = linea_v2.split(',')[COD_PRODUCTO]
            cant_ventas = linea_v2.split(',')[COD_PRODUCTO]

            #agrego las ventas en el dicc, si no estaba lo agrego con el codigo
            if codigo not in dicc_ventas_totales:
                dicc_ventas_totales[codigo] = linea_v2.split(',')[CANT_VENTAS]
            else:
                dicc_ventas_totales[codigo] += linea_v2.split(',')[CANT_VENTAS]

        elif (not linea_v2) or (int(linea_v1.split(',')[0]) <= int(linea_v2.split(',')[0])):

            ventas_completas.write(f'{linea_v1}, SUC_1\n')
            linea_v1 = ventas_1.readline().strip()

            codigo = linea_v1.split(',')[COD_PRODUCTO]
            cant_ventas = linea_v2.split(',')[COD_PRODUCTO]

            if codigo not in dicc_ventas_totales:
                dicc_ventas_totales[codigo] = linea_v2.split(',')[CANT_VENTAS]
            else:
                dicc_ventas_totales[codigo] += linea_v2.split(',')[CANT_VENTAS]
    
    ventas_completas.close()
    ventas_1.close()
    ventas_2.close

    return dicc_ventas_totales


def main ():
    dicc_rep = {1:['tornillos', 10], 2: ['tuercas', 20]}
    ventas_1 = open('\\ventas1.csv','r')
    ventas_2 = open('\\ventas2.csv','r')
    
    #merge crea dicc de ventas totales y el archivo merge de ambos
    dicc_ventas_totales = merge(ventas_1,ventas_2) 


