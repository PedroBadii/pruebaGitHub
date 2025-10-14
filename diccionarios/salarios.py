'''
Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes 
valores: puesto(string), salario(entero). Los puestos pueden estar repetidos. Ejemplos: 
[['Desarrollador', 1000], ['Tester', 800], ['Desarrollador', 920]]. Los datos surgen de diferentes empresas, por eso las
 repeticiones. Se pide que escribas un programa en python que procese esa lista y genere un diccionario con clave puesto
y valores total_salarios, cantidad, promedio. Luego, debe listar los puestos-promedios, ordenados de mayor a menor por 
promedios salariales.
'''

def promedios (salarios):
    dicc = {}
    for puesto in salarios:
        if puesto[0] not in dicc:
            dicc[puesto[0]] = [puesto[1], 1, puesto[1]]
        else:
            dicc[puesto[0]][0] += puesto[1]
            dicc[puesto[0]][1] += 1
            dicc[puesto[0]][2] = dicc[puesto[0]][0] / dicc[puesto[0]][1]
        
    return dicc

def mostrar (dicc):
    ordenado = sorted(dicc.items(), key=lambda x: x[1][2], reverse=True)
    for puesto, montos in ordenado:
        print('{0:<20}{1:>5}'.format(puesto, montos[2]))

def main():
    dicc = [['Desarrollador', 1000], ['Tester', 800], ['Desarrollador', 920]]
    mostrar(promedios(dicc))

main()