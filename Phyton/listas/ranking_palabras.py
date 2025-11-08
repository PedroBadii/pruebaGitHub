                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba un texto y devuelva una lista anidada que representa un
ranking de palabras.
El texto puede tener gran cantidad de palabras.
La función deberá devolver una lista anidada, en la que cada sublista, esté formada por un par
[palabra, cantidad de veces en el texto], ordenada por la cantidad de veces que aparece la
palabra.
Las palabras sólo deben aparecer una vez en la lista.
'''

def texto_a_palabras(texto):#toma el texto y devuelve la lista de palabras
    '''
    >>> texto_a_palabras('ya voy para alla')
    ['ya', 'voy', 'para', 'alla']
    '''
    lista_palabras = []
    inicio_palabra = 0 #aca guardo el indice del ultimo espacio encontrado
    for i in range(len(texto)-1):
        if texto[i] == ' ':
            lista_palabras.append(texto[inicio_palabra:i]) #desde el ultimo espacio encontrado hasta el nuevo
            inicio_palabra = i + 1
    
    lista_palabras.append(texto[inicio_palabra:])#esto es porque si no encuentra un espacio al final no \
    #agrega la ultima palabra
    
    return lista_palabras

def ranking_palabras (texto):
    '''
    >>> ranking_palabras('ya voy para alla ya voy ya')
    [['ya', 3], ['voy', 2], ['para', 1], ['alla', 1]]
    >>> ranking_palabras('hola mundo hola mundo hola Python')
    [['hola', 3], ['mundo', 2], ['Python', 1]]
    '''
    
    lista_palabras = texto_a_palabras(texto)
    ranking = []
    
    for palabra in lista_palabras:
        ya_existe = False #sin la bandera no podría appendear fuera del bucle
        for lista in ranking:
            if lista[0] == palabra:
                lista[1] += 1
                ya_existe = True

        if not ya_existe: #appendeo solo en el caso que no haya encontrado la palabra
            ranking.append([palabra, 1])

    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking

import doctest
print(doctest.testmod())
    