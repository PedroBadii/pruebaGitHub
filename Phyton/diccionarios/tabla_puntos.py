                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Problema Se pide que ingresen por teclado pares de   Equipo-Puntos ganados, el mismo par se puede 
ingresar varias veces. Se pide generar  una Tabla de Puntos Acumulados para cada equipo, ordenando 
la tabla por puntos en forma decreciente
'''

def pedir_equipo():
    tabla = {}
    equipo = input('Ingrese un equipo. Para terminar, ingrese 0: ')

    while equipo != '0':
        if equipo not in tabla:
            puntos = int(input('Ingrese los puntos del equipo: '))
            tabla[equipo] = puntos
        else:
            tabla[equipo] += puntos
        
        equipo = input('Ingrese un equipo. Para terminar, ingrese 0: ')
    
    print(tabla)

pedir_equipo()





