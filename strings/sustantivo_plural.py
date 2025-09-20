                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
 Escribir una función que recibirá por parámetro, una palabra, que representa un sustantivo
en singular.
La función deberá devolver, el plural de dicho sustantivo, aplicando las siguientes reglas:
a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
c. Si la palabra termina en “z”, la reemplazamos por “ces”.
d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la “s”, la
“z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.
e. Si el sustantivo termina en “s” ó “x”, entonces el plural es igual al singular, por lo tanto la
función deberá devolver lo mismo que recibió
'''
'casa'
def sustantivo_plural (sustantivo):
    '''
    >>> sustantivo_plural ('casa')
    'casas'
    >>> sustantivo_plural ('yacaré')
    'yacarés'
    >>> sustantivo_plural ('vzeraz')
    'vzeraces'
    >>> sustantivo_plural ('monitor')
    'monitores'
    >>> sustantivo_plural ('tabú')
    'tabúes'
    >>> sustantivo_plural ('análisis')
    'análisis'
    '''

    letra_final = sustantivo[len(sustantivo)-1]
    sustantivo_plural = sustantivo

    if letra_final in 'aeiou' or letra_final == 'é':
        sustantivo_plural = sustantivo + 's'
    elif letra_final == 'z':
        # sustantivo_plural = sustantivo_plural.replace(letra_final,'ces') si hago esto va a reemplazar
        #  cualquier z, yo quiero solo la última
        sustantivo_plural = sustantivo[:len(sustantivo)-1] + 'ces'
    elif letra_final not in 'aeiouszxé':
        sustantivo_plural = sustantivo + 'es'
    
    return sustantivo_plural

import doctest
print(doctest.testmod())