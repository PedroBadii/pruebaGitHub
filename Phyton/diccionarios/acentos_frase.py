                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Pedir al usuario el ingreso de una frase. Contabilizar cuántos acentos por cada tipo de letra tiene 
la frase y mostrarlos por pantalla al usuario. Los posibles acentos son á, é, í, ó, ú (pasar toda 
la frase a minúsculas).
'''

def cant_acentos (frase):
    '''
    >>> cant_acentos('Él gritó así: "CÁLAME ÉSTA"')
    {'é': 2, 'ó': 1, 'í': 1, 'á': 1}
    '''
    dicc_acentos = {}

    for letra in frase.lower():
        if letra in 'áéíóú':
            if letra in dicc_acentos:
                dicc_acentos[letra] += 1
            else:
                dicc_acentos[letra] = 1
    
    return dicc_acentos

def mostrar_dicc(dicc):
    for clave in dicc:
        print('La letra con acento', clave, 'aparece', str(dicc[clave]), 'veces')

def main():
    frase = input('Ingrese una frase: ')
    mostrar_dicc(cant_acentos(frase))
    

main()


import doctest
#print(doctest.testmod())

