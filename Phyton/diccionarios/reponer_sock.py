                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba por parámetro un diccionario con el siguiente formato:
{ id_producto: [ stock_minimo, stock_actual ],..........}, donde el id_producto será la
clave, de tipo cadena; y la lista asociada a cada clave id_producto, contendrá una
dupla de valores, siendo el primero, el stock mínimo a mantener de dicho producto; y
el segundo, el stock actual del producto; ambos de tipo entero positivo.
La función debe imprimir un listado con los productos a reponer (cuyo stock_actual
sea menor al stock_minimo), indicando el id_producto y la cantidad a reponer.
'''


def reponer_stock(dicc):

    for producto in dicc:
        if dicc[producto][0]>dicc[producto][1]:
            print('{0:<10}{1:>10}'.format(producto,dicc[producto][0]-dicc[producto][1]))

reponer_stock({'banana': [10, 15], 'manzana': [5, 4], 'pera': [20, 8]})
