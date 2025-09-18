                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Dada una tupla anidada de sabores de helados y particularidades, del tipo:
sabores = (("chocolate", ("v", "c")), ("dulce de leche"), ("limón", ("v")), ("frutilla", ("c"))
donde "c" indica apto celíaco, y "v" vegano; escribir una función que reciba dicha tupla y devuelva 
dos listas, una con los sabores veganos, y otra con los sabores aptos celíacos.
Para nuestro caso de ejemplo, las listas a devolver serían:
["chocolate","limón"] ["chocolate","frutilla"]

Tenés que agregar el testeo de la función usando doctest, con 5 casos de prueba nuevos diseñados por
vos, sumado al que figura de ejemplo. Los casos que agregues deben probar distintas alternativas
posibles, incluidas por ejemplo aquellas que puedan devolver listas vacías. También considera casos
 con tuplas que contengan 4, 5, 6, 7 y 8 sabores.
'''

def separar_sabores(sabores):
    '''
    >>> separar_sabores([('chocolate', ('v', 'c')), ('dulce de leche',), ('limón', ('v')), ('frutilla', ('c'))])
    (['chocolate', 'limón'], ['chocolate', 'frutilla'])
    >>> separar_sabores([('banana', ('v')), ('naranja',), ('nesquick',), ('toddy',)])
    (['banana'], [])
    >>> separar_sabores([('pistacho', ('v', 'c')), ('crema del cielo', ('v')), ('bon o bon',),
    ... ('ferrero rocher', ('v')), ('rafaelo', ('v'))])
    (['pistacho', 'crema del cielo', 'ferrero rocher', 'rafaelo'], ['pistacho'])
    >>> separar_sabores([('chocolate'), ('chocolate blanco', ('v', 'c')), ('chocolate granizado', ('c')), 
    ... ('chocolate con almendras', ('v')), ('chocolate mocca', ('v', 'c')), ('chocolate ruso')])
    (['chocolate blanco', 'chocolate con almendras', 'chocolate mocca'], ['chocolate blanco', 'chocolate granizado', 'chocolate mocca'])
    >>> separar_sabores([('americana', ('c')), ('tramontana', ('v')), ('vainilla', ('c')), ('limon', ('v', 'c')),
    ... ('menta granizada', ('v', 'c')), ('naranja', ('v', 'c')), ('banana split', ('c'))])
    (['tramontana', 'limon', 'menta granizada', 'naranja'], ['americana', 'vainilla', 'limon', 'menta granizada', 'naranja', 'banana split'])
    >>> separar_sabores([('bazooka',), ('monster',), ('coca cola', ('c')), ('picodulce',), 
    ... ('tofi', ('c')), ('fernet', ), ('fizz acido', ('c')), ('maracuya',)])
    ([], ['coca cola', 'tofi', 'fizz acido'])
    '''

    sabores_veganos=[]
    sabores_celiacos=[]

    for sabor in sabores:
        if len(sabor)==2: #si el sabor no es 'v' ni 'c' lo ignora, así puedo iterar sabor[1] sin error
            for i in sabor[1]:
                if i=='v':
                    sabores_veganos.append(sabor[0])
                elif i=='c':
                    sabores_celiacos.append(sabor[0])

    return sabores_veganos, sabores_celiacos #devuelve tupla, fue aclarado en el campus

import doctest
print(doctest.testmod())
                    
