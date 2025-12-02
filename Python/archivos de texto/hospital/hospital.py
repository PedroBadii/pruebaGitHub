'''
Una clínica registra las atenciones diarias en un archivo atenciones.csv. El archivo se encuentra ordenado por Fecha y,
dentro de cada fecha, por Especialidad.

Formato del archivo: Fecha, Especialidad, Nombre_Medico, Cobertura, Es_Urgencia

Cobertura: Puede ser "PAMI", "OSDE", "PARTICULAR", etc.
Es_Urgencia: "SI" o "NO".

Se pide desarrollar un programa modular en Python que:

A) Reporte Diario y Coberturas (Corte de Control): Recorriendo el archivo una sola vez, mostrar un listado por pantalla
con el siguiente formato:
Mostrar la Fecha actual.
Dentro de cada fecha, agrupar por Especialidad.
Por cada Especialidad, informar: Cantidad total de pacientes atendidos y qué porcentaje de ellos tenía cobertura "PAMI".
Al final del día, mostrar el total de pacientes atendidos en esa fecha. También mostrar el total de pacientes en todas 
las fechas

Salida esperada:

Fecha: 01/12/2024
   Especialidad: CARDIOLOGIA
      - Total Pacientes: 10
      - Porcentaje PAMI: 30.0%
   Especialidad: PEDIATRIA
      - Total Pacientes: 5
      - Porcentaje PAMI: 0.0%
Total Atendidos el 01/12/2024: 15
...

B) Productividad de Médicos (Diccionario): Realizando una nueva lectura del archivo, generar un diccionario donde:

Clave: Nombre_Medico (String).
Valor: Una lista de 2 elementos: [Total de pacientes atendidos, Cantidad de urgencias atendidas ("SI")].

C) Ranking de Médicos de Urgencia: En base al diccionario generado en el punto B, generar un archivo 
ranking_urgencias.txt.
El archivo debe estar ordenado de Mayor a Menor por la cantidad de Urgencias atendidas.

Condición de filtrado: En este archivo NO deben aparecer los médicos que no hayan atendido ninguna urgencia (es decir,
urgencias = 0).

Formato: Medico: [Nombre] - Urgencias: [Cantidad]
'''

#----- PUNTO A -----#

def leer(archivo):
    linea = archivo.readline()
    
    if linea:
        fecha, especialidad, medico, cobertura, urgencia = linea.rstrip().split(',')
    else:
        fecha, especialidad, medico, cobertura, urgencia = ['', '', '', '', '']
        
    return fecha, especialidad, medico, cobertura, urgencia

def generar_listado(archivo):
    
    fecha, especialidad, medico, cobertura, urgencia = leer(archivo)

    total_hospital = 0
    
    while fecha:
        
        fecha_actual = fecha
        pacientes_fecha = 0
        print(f'Fecha: {fecha_actual}')
        
        
        while fecha_actual == fecha:
            
            especialidad_actual = especialidad
            pacientes_esp = 0
            pacientes_pami = 0
            print(f'Especialidad: {especialidad_actual}')
            
            while (especialidad_actual == especialidad) and (fecha_actual == fecha):
                
                pacientes_esp += 1
                if cobertura == 'PAMI':
                    pacientes_pami += 1
                
                fecha, especialidad, medico, cobertura, urgencia = leer(archivo)
                
            pacientes_fecha += pacientes_esp    
            print(f'Total pacientes: {pacientes_esp}')
            
            if pacientes_esp > 0:
                print(f'Porcentaje PAMI: {(pacientes_pami/pacientes_esp)*100} %')
            else:
                print('No hay pacientes PAMI')
            
        total_hospital += pacientes_fecha    
        print(f'Pacientes atendidos el {fecha_actual}: {pacientes_fecha}')
        
    print(f'Total pacientes hospital: {total_hospital}')
    
#----- PUNTO B -----#
        
def generar_dicc(atenciones):
    
    PAC = 0
    URGENCIAS = 1
    dicc_medicos = {}
    fecha, especialidad, medico, cobertura, urgencia = leer(atenciones)
    
    while fecha:
        if medico not in dicc_medicos:
            dicc_medicos[medico] = [0, 0]
            
        dicc_medicos[medico][PAC] += 1
        
        if urgencia == 'SI':
            dicc_medicos[medico][URGENCIAS] += 1
        
        fecha, especialidad, medico, cobertura, urgencia = leer(atenciones)
            
    return dicc_medicos

#----- PUNTO C -----#

def ordenar (dicc):
    return sorted(dicc.items(), key=lambda x: x[1][1], reverse=True)

def generar_ranking(tuplas, archivo): #Medico: [Nombre] - Urgencias: [Cantidad]
    i = 0
    while i<len(tuplas) and tuplas[i][1][1] != 0:
        archivo.write(f'Medico: {tuplas[i][0]} - Urgencias: {tuplas[i][1][1]}\n')
        i += 1
    

def main():
    #PUNTO A
    atenciones = open('Python\\archivos de texto\\hospital\\atenciones.csv','r')
    generar_listado(atenciones)
    
    #PUNTO B
    atenciones.seek(0)
    dicc_medicos = generar_dicc(atenciones)
    atenciones.close()
    
    #PUNTO c
    ranking_urgencias = open('Python\\archivos de texto\\hospital\\ranking_urgencias.txt', 'w')
    ordenado = ordenar(dicc_medicos)
    generar_ranking(ordenado, ranking_urgencias)
    ranking_urgencias.close()
    
main()