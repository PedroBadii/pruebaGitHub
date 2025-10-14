                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir una función elegir en Python para decidir asociarse o no a un
club. Esta función debe devolver True si el club es aceptado, False de
lo contrario.
La función recibe dos listas y un entero: una de actividades
(actividades que se realizan en el club), otra de actividades_deseadas
(son las actividades que al usuario le gustaría realizar) y un valor de
cuota.
El club se aceptará si:
Si realizan por lo menos dos actividades deseadas y el valor de la
cuota es menor o igual a MAX_CUOTA (asumir como predefinida)
'''

import doctest

def elegir(actividades, actividades_deseadas, cuota):
    '''
    >>> elegir(['museos', 'senderismo', 'bares', 'montañismo'], ['bares', 'museos', 'senderismo', 'conciertos'], 2000)
    True
    >>> elegir(['museos', 'senderismo', 'bares', 'montañismo'], ['bares', 'museos', 'senderismo', 'conciertos'], 6000)
    False
    >>> elegir(['futbol', 'basquet', 'bares', 'cilismo'], ['bares', 'museos', 'senderismo', 'conciertos'], 1000)
    False
    '''

    actividades_coincidentes = 0

    if cuota <= 5000: #acá iría la variable MAX_CUOTA pero pongo el valor para que funcione
        i = 0
        while actividades_coincidentes < 2 and i < len(actividades_deseadas):
            if actividades_deseadas[i] in actividades:
                actividades_coincidentes += 1
            i += 1
    
    return actividades_coincidentes == 2

print(doctest.testmod())


