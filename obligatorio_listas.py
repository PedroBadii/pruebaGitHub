#EJERCICIO EN PROCESO
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
    (['chocolate','limón'] ['chocolate','frutilla'])

    '''

    sabores_veganos=[]
    sabores_celiacos=[]

    for sabor in sabores:
        if len(sabor)==2:
            for i in sabor[1]:
                if i=='v':
                    sabores_veganos.append(sabor[0])
                elif i=='c':
                    sabores_celiacos.append(sabor[0])

    return sabores_veganos, sabores_celiacos

import doctest
doctest.testmod()
                    
