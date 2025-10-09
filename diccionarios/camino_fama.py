'''
En el programa “Camino a la fama”, los participantes muestran sus aptitudes: baile, canto, etc. Un jurado vota
a los participantes colocando un puntaje del 1 al 10. Esto genera una lista de listas (cada sublista es una 
votación). Ejemplo: [ [“Luisa”, 4], [“Mariano”, 10], [“Luisa”, 5], etc…]. Las votaciones son de distintos 
jueces y por distintas actuaciones por lo que los participantes aparecerán varias veces. Se pide que escribas
un programa en Python que procese esa lista y genere un diccionario con clave participantey valores: 
sumatoria_puntaje, cantidad_puntajes, promedio_puntaje.  Luego, debe listar: 
participantes – promedio_puntaje, ordenados de mayor a menor por promedio_puntaje. Con el ejemplo anterior 
debería quedar:
Mariano	10
Luisa		4.5
'''

def mostrar_dicc(dicc): #acá dicc es una tupla ('nombre', [lista])
    for participante in dicc:
        print('{0:<10}{1:>10}'.format(participante[0], participante[1][2]))

def listar_participantes(puntajes):

    dicc = {}

    for puntaje in puntajes:
        if puntaje[0] not in dicc:
            dicc[puntaje[0]] = [puntaje[1], 1, puntaje[1]]
        else:
            dicc[puntaje[0]][0] += puntaje[1]
            dicc[puntaje[0]][1] += 1
            dicc[puntaje[0]][2] = dicc[puntaje[0]][0] / dicc[puntaje[0]][1]

    dicc_ordenado = sorted(dicc.items(), key=lambda x: x[1][2], reverse=True)
    
    return dicc_ordenado


def main():
    puntajes = [['Luisa', 4], ['Mariano', 10], ['Luisa', 5]]
    dicc = listar_participantes(puntajes)
    mostrar_dicc(dicc)

main()