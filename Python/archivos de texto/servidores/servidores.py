'''
Ejercicio Simulacro: Unificación de Servidores
Una empresa de servicios en la nube tiene tres servidores regionales que registran el tráfico de usuarios. Al final del 
día, se generan tres archivos CSV ordenados por ID de Usuario: server1.csv, server2.csv y server3.csv.

Formato de los 3 archivos: ID_Usuario, Tiempo_Conexion_Minutos, MegaBytes_Consumidos

Se pide un programa modular en Python que:

A) Unificación (Merge de 3 Archivos): Recorriendo una sola vez los tres archivos simultáneamente (sin cargarlos en 
memoria), genere un archivo unificado trafico_total.csv.
Debe mantener el orden por ID_Usuario.
Debe agregar al final de cada línea un campo indicando el servidor de origen ("SRV1", "SRV2" o "SRV3").
En caso de igualdad de ID entre archivos, el orden de prioridad para escribir es: Servidor 1, luego Servidor 2, luego 
Servidor 3.

B) Procesamiento (Diccionario): Realizando una nueva lectura del archivo generado en el punto A (trafico_total.csv), 
arme un diccionario donde:

Clave: ID_Usuario.

Valor: Una lista de 2 elementos: [Tiempo Total de Conexión, Total MB Consumidos]. (Nota: Un usuario puede aparecer varias 
veces si se conectó a distintos servidores, aquí debés sumar sus consumos).

C) Reporte de Altos Consumos: En base al diccionario del punto B, generar un archivo top_usuarios.txt que liste a los 
usuarios.
Debe estar ordenado de Mayor a Menor por la cantidad de MegaBytes consumidos.

Formato de línea: Usuario: [ID] - Total MB: [Cantidad
'''

ID_MAX = 9999

#----- PUNTO 1 -----#

def leer (archivo):
    linea = archivo.readline()

    if linea:
        id, tiempo, megas = linea.rstrip().split(',') 
        id = int(id)
        tiempo = int(tiempo)
        megas = int(megas)
    else:
        id, tiempo, megas = ID_MAX, 0, 0

    return id, tiempo, megas

def generar_trafico_total(sv_1, sv_2, sv_3, trafico_total):

    id_1, tiempo_1, megas_1 = leer(sv_1)
    id_2, tiempo_2, megas_2 = leer(sv_2)
    id_3, tiempo_3, megas_3 = leer(sv_3)
    
    while id_1 < ID_MAX or id_2 < ID_MAX or id_3 < ID_MAX:
        id_minimo = min(id_1, id_2, id_3)

        if id_minimo == id_1:
            trafico_total.write(f'{id_1},{tiempo_1},{megas_1},SRV1\n')
            id_1, tiempo_1, megas_1 = leer(sv_1)
        elif id_minimo == id_2:
            trafico_total.write(f'{id_2},{tiempo_2},{megas_2},SRV2\n')
            id_2, tiempo_2, megas_2 = leer(sv_2)
        elif id_minimo == id_3:
            trafico_total.write(f'{id_3},{tiempo_3},{megas_3},SRV3\n')
            id_3, tiempo_3, megas_3 = leer(sv_3)
        
#----- PUNTO 2 -----#

def leer_trafico_total(archivo):
    linea = archivo.readline()

    if linea:
        id, tiempo, megas, suc = linea.rstrip().split(',')
        id = int(id)
        tiempo = int(tiempo) 
        megas = int(megas)
    else:
        id, tiempo, megas, suc = ID_MAX, 0, 0, 0

    return id, tiempo, megas, suc

def generar_dicc(archivo):
    TIEMPO = 0
    MB = 1
    dicc_usuarios = {}
    id, tiempo, megas, suc = leer_trafico_total(archivo)

    while id < ID_MAX:
        if id not in dicc_usuarios:
            dicc_usuarios[id] = [0, 0]

        dicc_usuarios[id][TIEMPO] += tiempo
        dicc_usuarios[id][MB] += megas

        id, tiempo, megas, suc = leer_trafico_total(archivo)
    
    return dicc_usuarios

#----- PUNTO 3 -----#

def ordenar(dicc): #(id, [120, 63])
    return sorted(dicc.items(),key=lambda x: x[1][1], reverse=True)

def generar_listado(lista, archivo): #(51, [215, 63])
    for id, datos in lista:
        archivo.write(f'{id}-{datos[1]}\n')

def main():
    #PUNTO 1
    sv_1 = open('Python\\archivos de texto\\servidores\\server1.csv','r')
    sv_2 = open('Python\\archivos de texto\\servidores\\server2.csv','r')
    sv_3 = open('Python\\archivos de texto\\servidores\\server3.csv','r')
    trafico_total = open('Python\\archivos de texto\\servidores\\trafico_total.csv', 'w')
    generar_trafico_total(sv_1, sv_2, sv_3, trafico_total)
    sv_1.close()
    sv_2.close()
    sv_3.close()
    trafico_total.close()#como abrí con w no puedo usar .seek()

    #PUNTO 2
    trafico_total = open('Python\\archivos de texto\\servidores\\trafico_total.csv', 'r')
    dicc_usuarios = generar_dicc(trafico_total)

    #PUNTO 3
    ordenado = ordenar(dicc_usuarios) #lista de tuplas tuplas
    listado = open('Python\\archivos de texto\\servidores\\top_usuarios.txt', 'w')
    generar_listado(ordenado, listado)
    listado.close()

main()
