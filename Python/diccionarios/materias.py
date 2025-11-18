                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Dado el diccionario "dic_materias" que tiene cargados los nombre de las materias
como clave, y como valor asociado, una lista con tres números enteros, que indican:
la cantidad de alumnos anotados (como primer valor), cantidad de alumnos que
rindieron el parcial (segundo valor), cantidad de alumnos que aprobaron el parcial
(tercer valor).
Se pide que escribas:
a) Una función que reciba el diccionario y devuelva una lista con las materias cuyo
índice de deserción sea mayor al 50% (esto se calcula teniendo en cuenta la cantidad
de alumnos que rindieron el parcial sobre la cantidad de anotados).
b) Una función que reciba el diccionario y que devuelva una lista de tuplas, formadas
por pares (materia, porcentaje_aprobados), ordenada de mayor a menor por
porcentaje de aprobados (en este caso, se calcula sobre la cantidad que rindieron).
'''
#dicc = {'analisis': [105, 35, 5], 'progamacion': [50, 40, 40], 'algebra': [60, 20, 10]}

import doctest

def desercion(dicc):
    '''
    >>> desercion({'analisis': [105, 35, 5], 'progamacion': [50, 40, 40], 'algebra': [60, 20, 10]})
    ['analisis', 'algebra']
    '''

    materias_desercion = []

    for materia in dicc:
        if (dicc[materia][1]/dicc[materia][0]) < 0.5:
            materias_desercion.append(materia)
    
    return materias_desercion

def porcentaje_aprobados(dicc):
    '''
    >>> porcentaje_aprobados({'analisis': [105, 35, 7], 'programacion': [50, 40, 40], 'algebra': [60, 20, 10]})
    [('programacion', 1.0), ('algebra', 0.5), ('analisis', 0.2)]
    '''

    porcentaje_aprobacion = []

    for materia in dicc:

        porcentaje_aprobacion.append((materia, dicc[materia][2]/dicc[materia][1]))

    return sorted(porcentaje_aprobacion, key=lambda x: x[1], reverse=True)

print(doctest.testmod())