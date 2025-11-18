
'''
 Listar el archivo de ventas, recorriendolo scuencialmente, separando cada uno # de los datos que 
 vinen en la línea e informando al final el total general de # cantidad y de importe
'''

def leer(ar_ventas):
    ''' 
    Funcion que lee una linea del archivo y devuelve los valores leidos cod_sucursal, cod_articulo, 
    cant_vendida, imp_total. En caso de llegar a fin de archivo devolverá 4 valores vacios separados 
    por comas. 
    ''' 

    linea = ar_ventas.readline() 
    
    if linea: 
        devolver = linea.rstrip("\n").split(",") 
    else: 
        devolver = "","","0","0"

    return devolver

def listar_archivo(): 

    ar_ventas = open('Python\\archivos de texto\\ventas.csv','r') 

    cod_suc, cod_art, cant, imp = leer(ar_ventas) #luego de esto el cursor queda poscisionado en el final de la primera línea
    cant = int(cant) 
    imp = float(imp) 
    cant_total_gral = imp_total_gral = 0 

    # Lectura Total del archivo linea a linea 
    while cod_suc: 

        print('{0:4}\t{1:5}\t{2:5}\t{3:8.2f}'.format(cod_suc, cod_art, cant, imp)) 

        cant_total_gral += cant 
        imp_total_gral += imp 

        cod_suc, cod_art, cant, imp = leer(ar_ventas)#como ya se leyó la primera, ahora lee la segunda línea
        cant = int(cant) 
        imp = float(imp) 

    print("Total General:\t{0:5}\t{1:8.2f} ".format(cant_total_gral, imp_total_gral)) 
    
    ar_ventas.close() 
    
    return

listar_archivo()