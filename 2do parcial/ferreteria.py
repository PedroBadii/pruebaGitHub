'''
ventas1.csv    dia,codigo_producto,cantidad_vendida ordenado por día
ventas2.csv    dia,codigo_producto,cantidad_vendida ordenado por día
Ejemplo:
1,176,12
1,45,1
diccionario_reposicion = {001:['tornillos', 10], '002': ['tuercas', 20] }
códigos de artículos como clave y una lista con dos valores: la descripción del artículo y el nivel de 
ventas de cada artículo para solicitar reposición
'''

def merge (ventas_1, ventas_2):
    ventas_completas = open('\\ventas_completas.csv','w')
    linea_v1 = (ventas_1.readline()).rstrip("\n").split(",")
    linea_v2= (ventas_2.readline()).rstrip("\n").split(",")
    while linea_v1 or linea_v2 :
        if int(linea_v1[0]) > int(linea_v2[0]):
            #hago algo
        if int(linea_v1[0]) > (linea_v2[0]):
            #hago otra cosa
    


def main ():
    dicc_rep = {1:['tornillos', 10], 2: ['tuercas', 20]}
    ventas_1 = open('\\ventas1.csv','r')
    ventas_2 = open('\\ventas2.csv','r')
    merge(ventas_1,ventas_2)


