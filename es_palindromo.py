                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función que reciba una palabra ó frase, y devuelva True, si es un palíndromo, ó False en caso
contrario. Asumir que la cadena a recibir, sólo estará formada por caracteres alfabéticos y espacios en
blanco.
'''

def es_palindromo(cadena):
    '''
    >>> es_palindromo('anita lava la tina')
    True
    >>> es_palindromo('55neuquen55')
    True
    >>> es_palindromo('nosoypalindromo')
    False
    '''

    #-----esto es para que la función tome frases con espacios----#
    cadena_min = cadena.lower()
    cadena_mod = '' #cadena mod va a ser solo minúsculas y sin espacios para trabajar
    for i in cadena_min:
        if i != ' ':
            cadena_mod += i
    #-------------------------------------------------------------#

    palindromo = True
    i = 0

    while palindromo == True and (not cadena_mod[i] == cadena_mod[len(cadena_mod)-1-i]):
        palindromo = False
        i += 1

    return palindromo

import doctest
print(doctest.testmod())
