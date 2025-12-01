'''
A) Durante el año 2023, la Facultad de Ingeniería ha dictado cursos para el plan Argentina Programa 4.0. En el
segundo tramo del programa, se ofrecieron los cursos de: Python, Java, Programación Front End,
Programación Back End y Testing. Cada uno de estos cursos tenía entre 2 y hasta 6 comisiones, con
120 alumnos en promedio por comisión

El archivo inscriptos_AP40.csv, posee los siguientes datos:
    Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision
Se encuentra ordenado por Curso y dentro de este por Comisión.

Escribir un programa modular (compuesto por funciones), en Python, que en base a los datos que se
encuentran en el archivo inscriptos_AP40.csv, genere:

a. Recorriendo sólo una vez el archivo, un informe indicando el nombre del curso, y para cada curso,
   las comisiones y la cantidad de alumnos inscriptos en cada una de las comisiones. Además por
   cada curso debe informar el total de alumnos inscriptos. Al final del listado se debe informar el total
   de alumnos inscriptos en todos los cursos, y que porcentaje de estos trabaja (este dato viene
   indicado con un “si”, en el respectivo campo).

b. Realizando una nueva lectura del archivo, arme un diccionario en donde la clave será el Nombre
   del Curso y asociado a este, una lista con: la cantidad de inscriptos con estudios primarios, la
   cantidad con estudios secundarios y la cantidad con estudios universitarios (este dato viene
   indicado en el campo Nivel Educativo, como “PRI”, “SEC”, “UNI”).

c. En base al diccionario del punto anterior, dejar en el archivo inscripciones.txt, un listado ordenado
   de menor a mayor por el total de inscriptos en cada curso, indicando por cada línea del archivo:
   Nombre del Curso - Total Inscriptos - Cant. Est. Prim. - Cant. Est. Sec. - Cant. Est. Univ.
'''
# Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision
# numero???, SEC, si, Java, 61.01

PRI = 0
SEC = 1
UNI = 2

def leer (inscriptos): #esta sirve para varios puntos
    linea = inscriptos.readline()

    if linea:
        nro_inscripto, nivel, trabaja, curso, comision = linea.rstrip().split(',')
    else:
        nro_inscripto = ''
        nivel = ''
        trabaja = ''
        curso = ''
        comision = ''
    
    return nro_inscripto, nivel, trabaja, curso, comision #('SEC', 'si', 'Java', '61.01') ó ('', '', '', '0')

#-----PUNTO A-----#

def generar_informe(inscriptos):
    
    cant_trabaja = 0
    total_alumnos = 0
    nro_inscripto, nivel, trabaja, curso, comision = leer(inscriptos)
    
    while curso: #si aún hay datos
        
        curso_actual = curso
        alumnos_curso = 0
        print(f'Curso: {curso_actual}\n')
        
        while curso_actual == curso:
            alumnos_comision = 0
            comision_actual = comision 
            
            while comision_actual == comision and curso_actual == curso:
                alumnos_comision += 1
                if trabaja == 'si':
                    cant_trabaja += 1
                nro_inscripto, nivel, trabaja, curso, comision = leer(inscriptos)
                
            print(f'En la comision {comision_actual} hay {alumnos_comision} alumnos\n')
            alumnos_curso += alumnos_comision
            
        print(f'En el curso {curso_actual} hay {alumnos_curso}\n')
        total_alumnos += alumnos_curso
        
    print(f'Los alumnos en total de todos los cursos son {total_alumnos}\n')
    print(f'El porcentaje de alumnos que trabaja es {(cant_trabaja/total_alumnos)*100}%\n')
    
#-----PUNTO B-----#
    
def alumnos_estudios (inscriptos):
    
    dicc_estudios = {}
    nro_inscripto, nivel, trabaja, curso, comision = leer(inscriptos)
    
    while curso:
        
        if curso not in dicc_estudios:
            dicc_estudios[curso] = [0,0,0]
            
        if nivel == 'PRI':
            dicc_estudios[curso][PRI] += 1
        elif nivel == 'SEC':
            dicc_estudios[curso][SEC] += 1
        elif nivel == 'UNI':
            dicc_estudios[curso][UNI] += 1
        
        nro_inscripto, nivel, trabaja, curso, comision = leer(inscriptos)
        
    return dicc_estudios   
            
#-----PUNTO C-----#

def ordenar(dicc):
    return sorted(dicc.items(), key=lambda x: (x[1][PRI] + x[1][SEC] + x[1][UNI]))

def generar_listado(ordenado, inscripciones): #[('Python',[25,58,6]), ('Java', [26, 63, 14])]
    
    for curso, lista in ordenado:
        total_inscriptos = lista[PRI]+lista[SEC]+lista[UNI]
        inscripciones.write(f'{curso}-{total_inscriptos}-{lista[PRI]}-{lista[SEC]}-{lista[UNI]}\n')
        

def main():
    #PUNTO A
    inscriptos = open('Python\\archivos de texto\\Argentina programa\\inscriptos_AP40.csv', 'r')
    generar_informe (inscriptos)
    inscriptos.close()
    
    #PUNTO B
    inscriptos = open('Python\\archivos de texto\\Argentina programa\\inscriptos_AP40.csv', 'r')
    dicc_estudios = alumnos_estudios(inscriptos)
    inscriptos.close()
    
    #PUNTO C
    inscripciones = open('Python\\archivos de texto\\Argentina programa\\inscripciones.txt', 'w')
    ordenado = ordenar(dicc_estudios) #es una lista de tuplas 
    generar_listado(ordenado, inscripciones)
    inscripciones.close()
    
main()