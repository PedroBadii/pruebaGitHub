                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Se tiene cargado en memoria un diccionario llamado Stock con clave
Producto y valores cantidad y precio. Se pide calcular el valor total del
inventario
stock={1:[2,300],2:[5000,3],5:[60,400]}
producto 1: 2 unidades, 300 cada una
'''

def valor_stock (stock): #stock es un dicc como en el ejemplo
    '''
    >>> valor_stock({1:[2,300],2:[5000,3],5:[60,400]})
    39600
    '''
    valor_stock = 0
    for producto in stock:
        valor_stock += stock[producto][0] * stock[producto][1]

    return valor_stock
    
import doctest
print(doctest.testmod())
    
