                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba por parámetro un texto, y devuelva un diccionario, el
cual tendrá como claves, cada una de las palabras que hay en el texto, y como valor,
la cantidad de ocurrencias de dicha palabra en el texto.
No distinguir entre mayúsculas y minúsculas.
Considerar que las palabras del texto estarán separadas por blancos.
'''

def palabras_cantidad(texto):

    dicc = {}
    palabras = texto.lower().split(' ')

    for palabra in palabras:
        if palabra not in dicc:
            dicc[palabra] = 1
        else:
            dicc[palabra] += 1
    return dicc

print(palabras_cantidad('Escribir una función que reciba por parámetro un texto escribir un un un un por por'))