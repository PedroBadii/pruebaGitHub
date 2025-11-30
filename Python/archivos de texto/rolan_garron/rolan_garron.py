'''
El famoso torneo de tenis Rolan Garrón se disputa todos los años. Los resultados se guardan en el archivo 
resultados.csv. Este archivo tiene el siguiente formato:

dia, participante1, puntos1_sets, participante2, puntos2_sets

El archivo se guarda de forma secuencial, comenzando desde el dia 1 del campeonato, por lo que queda ordenado 
por día. Los partidos se juegan al mejor de 5 sets, en caso de ganar los tres primeros no hace falta jugar los
dos que le siguen, es por lo que hay partidos de 3, 4 y 5 sets.

Ejemplo:
1, Jarry Nicolas, 6-6-6, Dellien Hugo, 4-4-2
1, Purcell Max, 7-1-6-6, Thompson Jordan, 5-6-4-4
2, Zapata Miralles, 6-7-2-0-4, Schwartzman Diego, 1-6-6-6-6

Se pide realizar un programa modular en Python que:
1)Recorriendo una sola vez el archivo de resultados y sin cargarlo completamente en memoria, haga un corte por 
día, indicando: día, cantidad de partidos jugados, cantidad de sets jugados

Con nuestro ejemplo sería:
        Día         Partidos        Sets
        1           2               7   
        2           1               5

2) Realizandio una nueva lectura del archivo, arme un diccionario en donde la clave será el nombre del jugador y 
el dato la cantidad de partidos ganados. Tené en cuenta que gana el jugador que consgue 3 sets

3) En base al diccionario generado en el punto 2, dejar en el archivo ganados.txt, un listado, ordenado de mayor
a menor por cantidad de partidos ganados, indicando por cada línea del archivo el nombre del jugador - la cantidad
de partidos ganados

IMPORTANTE: Mantener las buenas prácticas recomendadas por el PEP de la cátedra: nombres, modularización, etc.
'''

DIA_MAX = 99

#----- PUNTO 1 -----#

def leer (resultados):

    linea = resultados.readline()

    if linea:
        linea = linea.strip().split(',') #['1', 'Jarry Nicolas' , '6-6-6', 'Dellien Hugo', '4-4-2']
        dia = int(linea[0])
        sets = len(linea[2].split('-')) #['6', '6', '6']--> 3
    else:
        dia = DIA_MAX
        sets = 0

    return [dia, sets]


def corte_por_dia (resultados):

    dia, sets = leer (resultados)

    print (f'{'Dia':<10}{'Partidos':<15}{'Sets':<10}')
    
    while dia < DIA_MAX:
        dia_actual = dia
        total_sets = 0
        total_partidos = 0

        while dia_actual == dia:
            total_partidos += 1
            total_sets += sets
            dia, sets = leer (resultados)
        
        print (f'{dia_actual:<10}{total_partidos:<15}{total_sets:<10}')

#----- PUNTO 2 -----#

def leer_ganador(resultados): #devuelve el jugador ganador

    ganador = ''
    JUGADOR_1 = 1
    JUGADOR_2 = 3
    GAMES_1 = 2
    GAMES_2 = 4

    linea = resultados.readline()

    if linea: # 1, Jarry Nicolas, 6-6-6, Dellien Hugo, 4-4-2
        linea = linea.strip().split(',') #['1', 'Jarry Nicolas', '6-6-6', 'Dellien Hugo', '4-4-2']

        games_1 = linea[GAMES_1].split('-') #['6', '6', '6']
        games_2 = linea[GAMES_2].split('-') #['4', '4', '2']

        sets_1, sets_2, i = 0, 0, 0

        while (sets_1 < 3) and (sets_2 < 3): #mientras ninguna haya ganado

            if int(games_1[i]) > int(games_2[i]):
                sets_1 += 1
            else:
                sets_2 += 1

            i += 1
        
        if sets_1 > sets_2:
            ganador = linea[JUGADOR_1]
        else:
            ganador = linea[JUGADOR_2]

    return ganador


def ganados_por_jugador(resultados):

    dicc_ganados = {}
    jugador = leer_ganador(resultados)

    while jugador:

        if jugador not in dicc_ganados:
            dicc_ganados[jugador] = 1
        else:
            dicc_ganados[jugador] += 1
        
        jugador = leer_ganador(resultados)

    return dicc_ganados

#----- PUNTO 3 -----#

def ordenar_dicc(dicc):

    return sorted(dicc.items(), key = lambda x: x[1], reverse=True)

def armar_listado(ordenado, ganados):
    JUGADOR = 0
    GANADOS = 1
    for tupla in ordenado:
        ganados.write(f'{tupla[JUGADOR]} - {tupla[GANADOS]}\n')

def main():

    #PUNTO 1:
    resultados = open('Python\\archivos de texto\\rolan_garron\\resultados.csv', 'r')
    corte_por_dia (resultados) #imprime la tabla de partidos y sets por dia
    resultados.close() #cierro y vuelvo a abrir para reestablecer el cursor al principio

    #PUNTO 2:
    resultados = open('Python\\archivos de texto\\rolan_garron\\resultados.csv', 'r')
    dicc_jugadores = ganados_por_jugador(resultados)
    resultados.close()

    #PUNTO 3:
    ordenado = ordenar_dicc(dicc_jugadores) #queda en tuplas
    ganados = open('Python\\archivos de texto\\rolan_garron\\ganados.txt', 'w')
    armar_listado(ordenado, ganados)
    ganados.close()

main()

