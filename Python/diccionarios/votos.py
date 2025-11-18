                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Se cuenta con una lista votacion, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes
 valores: partido (string), diputados (entero), senadores (entero). Ejemplo:
[ [“PP”, 19, 35], [“PSOE”, 20, 30], [“VOX”, 15, 15], [“PP”, 0, 15], …]. Los recuentos son de diferentes mesas por lo que
 los partidos aparecerán varias veces.
Se pide que escribas un programa en Python que procese esa lista y genere un diccionario con clave partido y valor 
total_votos.  El total de votos es la suma de diputados y senadores.
Luego, debe listar los partidos – total_votos, ordenados de mayor a menor por total_votos
'''

def votos_totales(votaciones):
    dicc = {}

    for partido in votaciones:
        if partido[0] not in dicc:
            dicc[partido[0]] = partido[1] + partido[2]
        else:
            dicc[partido[0]] += (partido[1] + partido[2])
    
    return dicc

def mostrar (dicc):
    for partido in dicc:
        print('{0:<5}{1:>3}'.format(partido,dicc[partido]))

def main():
   votaciones = [['PP', 19, 35], ['PSOE', 20, 30], ['VOX', 15, 15], ['PP', 0, 15], ['LLA', 1, 6]]
   mostrar(votos_totales(votaciones))

main()