'''
A) En una materia de un posgrado, se aplica evaluación continua. Esto consiste en pedir la entrega de
actividades semanales. En una semana puede haber ninguna, una o varias actividades. Los resultados se guardan en
un archivo notas.csv (CSV) con el siguiente formato (a excepción de la primera línea, en donde figura la
cantidad de trabajos totales):
semana,actividad,apellido_nombre,nota

Ejemplo:
5
1,cuestionario t1,Gonzalez Carlos,5
1,cuestionario t1,Rodriguez Rosa,8
1,trabajo practico t1,Rodriguez Rosa,10
3,cuestionario t2_3,Gonzalez Carlos,4
...

En el ejemplo anterior, el docente pidió 5 trabajos en total (primera línea). En la semana 1 se entregaron dos
cuestionarios y un trabajo práctico, con notas 5, 8 y 10, etc.
Sabiendo que el archivo está ordenado por semana y dentro de cada semana, por actividad, y que la aprobación es
con una nota de 6 o superior, se pide realizar un programa modular en Python que:

1) Recorriendo una sola vez el archivo notas.txt y sin cargarlo completamente en memoria, haga un corte de
control por día y por actividad, indicando: Cantidad de actividades semanales entregadas y dentro de cada
actividad, cantidad de entregados y aprobados.
Tomando el ejemplo anterior sería:
Semana 1:
-- cuestionario t1: entregados: 2 - aprobados: 1
-- trabajo practico t1: entregados: 1 - aprobados: 1
- Total de actividades semanales entregadas: 3

2) Realizando una nueva lectura del archivo notas.txt, arme un diccionario en donde la clave será el nombre del
estudiante y el dato será una lista de longitud 2: actividades entregadas, actividades aprobadas. Al finalizar,
imprimir un listado de los estudiantes que entregaron todas las actividades (en el ejemplo, deberían tener 5
actividades entregadas).

3) En base al diccionario generado en el punto 2 armar un listado, ordenado de mayor a menor por cantidad de
actividades aprobadas, indicando: estudiante - actividades aprobadas. En este listado no deben figurar los
estudiantes que no aprobaron ninguna actividad.
'''
SEMANA_MAX = 99

#----- PUNTO 1 -----#

def leer (notas):

    linea = notas.readline()
    
    if linea:
        semana, actividad, nombre, nota = linea.rstrip().split(',') #['1', 'cuestionario t1', 'Gonzalez Carlos', '5']
        datos = [int(semana), actividad, nombre, int(nota)]
    else:
        datos = [SEMANA_MAX, '', '', 0]
    
    return datos # [1, 'cuestionario t1', 'Gonzalez Carlos', 5] ó [99, '', '', 0]
        
'''
Semana 1:
-- cuestionario t1: entregados: 2 - aprobados: 1
-- trabajo practico t1: entregados: 1 - aprobados: 1
- Total de actividades semanales entregadas: 3
'''
def generar_informe (notas):
    
    semana, actividad, apellido_nombre, nota = leer(notas)
    
    while semana < SEMANA_MAX:
        
        semana_actual = semana
        actividades_semana = 0
        print(f'Semana {semana}: ')
        
        while semana == semana_actual:
            actividad_actual = actividad
            entregados, aprobados = 0, 0
            
            while actividad_actual == actividad:
                entregados += 1
                if nota >= 6:
                    aprobados += 1
                    
                semana, actividad, apellido_nombre, nota = leer(notas)
            
            print(f'--{actividad_actual}: entregados: {entregados} - aprobados: {aprobados}')
            actividades_semana += entregados
            
        print(f'Total de actividades semanales entregadas: {actividades_semana}')

#----- PUNTO 2 -----#
        
def generar_dicc (notas):
    ENTREGADO = 0
    APROBADO = 1
    
    dicc_estudiantes = {}
    total_actividades = int(notas.readline())#leo el total de notas en la primera linea
    semana, actividad, apellido_nombre, nota = leer(notas)
    print(f'Los estudiantes que entregaron todas las actividades son: ')
    
    while semana < SEMANA_MAX:
        if apellido_nombre not in dicc_estudiantes:
            dicc_estudiantes[apellido_nombre] = [0, 0]
        
        dicc_estudiantes[apellido_nombre][ENTREGADO] += 1
        if nota >= 6:
            dicc_estudiantes[apellido_nombre][APROBADO] += 1
            
        if dicc_estudiantes[apellido_nombre][ENTREGADO] == total_actividades:
            print(apellido_nombre)
            
        semana, actividad, apellido_nombre, nota = leer(notas)
    
    return dicc_estudiantes
        
#----- PUNTO 3 -----#

def ordenar_dicc(dicc):
    return sorted(dicc.items(), key=lambda x: x[1][1], reverse=True) #('apellido_nombre', [entregado, aprobado])

def generar_listado(tuplas):
    print(f'{'Estudiante':<15}{'Cant. Aprobadas':>15}')
    i = 0
    while tuplas[i][1][1] >= 1 and i<len(tuplas):
        print(f'{tuplas[i][0]:<15}{tuplas[i][1][1]:>15}')
        i += 1
        

def main():
    #PUNTO 1
    notas = open('Python\\archivos de texto\\materia posgrado\\notas.csv', 'r')
    notas.readline() #aca salteo la primera linea que no me sirve
    generar_informe (notas)
    
    #PUNTO 2
    notas.seek(0) #reseteo el cursor en el inicio del archivo
    dicc_estudiantes = generar_dicc (notas)
    
    #PUNTO 3
    ordenado = ordenar_dicc(dicc_estudiantes) #ordenado es lista de tuplas
    generar_listado(ordenado)
    
    notas.close()
    
main()