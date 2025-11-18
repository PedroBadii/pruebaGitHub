#-------EJERCICIO PENDIENTE
'''
Procese una lista de listas, con datos de partidos de fútbol y genere un diccionario “campeonato”.
La lista “partidos” contiene sublistas con tres valores: el primer y segundo valor son los nombres de los equipos, 
y el tercer valor podrá ser: 0 o 1 para indicar la posición del equipo ganador, 2 para indicar empate.
Los nombres de los equipos pueden repetirse. El diccionario “campeonato” deberá tener por clave el nombre del equipo, 
y como valor, una terna compuesta por: partidos ganados (primer valor), partidos perdidos (segundo valor), partidos 
empatados (tercer valor).

Informe el o los equipos con más partidos jugados.

Muestre por pantalla de mayor a menor los equipos con sus puntajes, teniendo en cuenta que por cada partido ganado se 
obtienen 3 puntos, y un punto por cada partido empatado. Los datos deben mostrarse en dos columnas: una para el equipo 
y otra para el puntaje.
'''

def campeonato(partidos):
    dicc= {}
    for partido in partidos:

        #primero agrego los equipos al dicc si no estan
        if partido[0] not in dicc:
            dicc[partido[0]] = [0,0,0]
        if partido[1] not in dicc:
            dicc[partido[1]] = [0,0,0]

        #cambio los contadores
        if partido[2] == 0:
            dicc[partido[0]][0] += 1
            dicc[partido[1]][1] += 1 
        elif partido[2] == 1:
            dicc[partido[0]][1] += 1
            dicc[partido[1]][0] += 1
        elif partido[2] == 2:
            dicc[partido[0]][2] += 1
            dicc[partido[1]][2] += 1

    return dicc

def mostrar(dicc):

    ordenado = sorted(dicc.items(), key=lambda x: (x[1][0]*3)+x[1][2], reverse=True)
    for equipo in ordenado:
        print('{0:<15}{1:>3}'.format(equipo[0],(equipo[1][0]*3)+(equipo[1][2])))



partidos = [['Boca', 'River', 0], ['Estudiantes', 'Gimnasia', 1], ['San Telmo', 'Godoy Cruz', 2]]
mostrar(campeonato(partidos))