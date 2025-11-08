                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Zip toma como argumento dos o más objetos iterables (cada uno de ellos con la
misma longitud) y devuelve un nuevo iterable cuyos elementos son tuplas que
contienen un elemento de cada uno de los iteradores originales.
Ejemplo Para los siguientes diccionarios calcular para cada fruta el Total de los
precios por la cantidad en stock de todas las frutas y el total parcial por fruta
precios = {"banana": 50,"manzana": 28,"naranja": 15, "pera": 30}
stock = { "banana": 60, "manzana": 00, "naranja": 32, "pera": 15}
zip(precios, stock)
iterable que contiene ('banana', 'banana')('manzana', 'manzana')
el iterable no son tuplas, no es algo legible por el humano, es solo para iterar
'''

def total_por_fruta(precios, stock):
    '''
    >>> total_por_fruta({"banana": 50,"manzana": 28,"naranja": 15, "pera": 30}, { "banana": 60, "manzana": 00, "naranja": 32, "pera": 15})
    {'banana': 3000, 'manzana': 0, 'naranja': 480, 'pera': 450}
    '''

    totales_por_fruta = {}
    total_fruta = 0

    for fruta_precio, fruta_stock in zip(precios, stock):#tengo que desempaquetar porque sino va a iterar \
            # sobre ('banana', 'banana') y debe iterar sobre 'banana'
            total_fruta = precios[fruta_precio] * stock[fruta_stock]
            totales_por_fruta[fruta_precio] = total_fruta
    
    return totales_por_fruta

def total (precios, stock):
    '''
    >>> total ({"banana": 50,"manzana": 28,"naranja": 15, "pera": 30}, { "banana": 60, "manzana": 00, "naranja": 32, "pera": 15})
    3930
    '''
      
    total = 0
    total_fruta = total_por_fruta(precios, stock)
    for fruta in total_fruta:
        total += total_fruta[fruta]

    return total


import doctest
print(doctest.testmod())