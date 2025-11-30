'''
Se tienen los resultados de la Eurocopa y la Copa América en dos archivos de texto  con formato csv,
llamados eurocopa.csv y copa_america.csv. Estos archivos tienen en cada linea, el resultado de un 
partido.
Los campos son:

    dia, equipo_local, goles_local, equipo_visitante, goles_visitante

Los archivos se guardaron en forma secuencial, comenzando desde el dia 1 del campeonato, por lo que 
están ordenados por dia.


Ejemplo

    1,Alemania,5,Escocia,1
    2,Hungria,1,Suiza,3
    2,Espania,3,Croacia,0
    2,Italia,2,Albania,2
    etc

Se pide realizar un programa modular (compuesto por funciones) en python que:

1) 
Recorriendo una sola vez los dos archivos y sin cargarlos completamente en memoria, los unifique 
(merge con clave máxima) en un único archivo ordenado por dia,
manteniendo el orden original y agregando un campo que indique de que archivo es la linea que se 
está escribiendo (EUROCOPA o COPA_AMERICA), 
ante igualdad del dia, guardar en primer lugar los de Eurocopa.
2) Realizando una lectura del archivo generado en el punto anterior, arme un diccionario en donde
la clave será el país y el dato será una lista de longitud 3: partidos ganados, empatados y 
perdidos
3) En base al diccionario generado en el punto 2 mostrar por pantalla un listado, ordenado de 
mayor a menor por cantidad de partidos ganados, indicando: país, partidos ganados. En este listado
no deben figurar los países que no ganaron ningún partido. 
'''

#--------PUNTO 1 ------#

DIA_MAYOR = 99

def leer (archivo): # 1,Alemania,5,Escocia,1  -->  [1,['Alemania'],['5'],['Escocia'],['1']] 
    linea = archivo.readline()
    if linea:
        linea = linea.strip()
    else:
        linea = str(DIA_MAYOR) + ',,,,' # linea = '99,,,,'

    datos = linea.split(',')
    #opcion 1: hay datos: ['1','Alemania','5','Escocia','1']
    #opcion 2: no hay datos: ['99',','','','']

    datos_format = [int (datos[0])] + datos[1:] #transforma el dia en un int

    return datos_format

def merge (copa_america, eurocopa, ambas_copas):

    dia_am, eq_local_am, gol_loc_am, eq_vis_am, gol_vis_am = leer(copa_america)
    # [1,'Argentina','4','Brasil','0'] o [99,','','','']

    dia_eu, eq_local_eu, gol_loc_eu, eq_vis_eu, gol_vis_eu = leer(eurocopa)
    # [1,'Alemania','5','Escocia','1'] o [99,','','','']


    while (dia_am < DIA_MAYOR) or (dia_eu < DIA_MAYOR): #cuando ambos dias sean 99, ahí se detiene

        if dia_eu <= dia_am:
            ambas_copas.write(f'{dia_eu},{eq_local_eu},{gol_loc_eu},{eq_vis_eu},{gol_vis_eu}, EUROCOPA\n')
            dia_eu, eq_local_eu, gol_loc_eu, eq_vis_eu, gol_vis_eu = leer(eurocopa)

        elif dia_am < dia_eu:
            ambas_copas.write(f'{dia_am},{eq_local_am},{gol_loc_am},{eq_vis_am},{gol_vis_am}, COPA_AMERICA\n')
            dia_am, eq_local_am, gol_loc_am, eq_vis_am, gol_vis_am = leer(copa_america)



    #--------PUNTO 2 ------#

def generar_dicc (ambas_copas):

    dicc_resultados = {}
    
    linea = ambas_copas.readline()

    GANADOS = 0
    EMPATADOS = 1
    PERDIDOS = 2

    while linea: #cuando linea sea vacia, se detiene

        dia, eq_local, gol_loc, eq_vis, gol_vis, copa = linea.strip().split(',')
        gol_loc = int (gol_loc)
        gol_vis = int (gol_vis)

        if eq_local not in dicc_resultados:
            dicc_resultados[eq_local] = [0,0,0]
        if eq_vis not in dicc_resultados:
                dicc_resultados[eq_vis] = [0,0,0]

        if gol_loc > gol_vis:
            dicc_resultados[eq_local][GANADOS] += 1
            dicc_resultados[eq_vis][PERDIDOS] +=1
        elif gol_loc < gol_vis:
            dicc_resultados[eq_local][PERDIDOS] += 1
            dicc_resultados[eq_vis][GANADOS] +=1
        else:
            dicc_resultados[eq_local][EMPATADOS] += 1
            dicc_resultados[eq_vis][EMPATADOS] +=1

        linea = ambas_copas.readline()

    return dicc_resultados

    #--------PUNTO 3 ------#

def ordenar_dicc(dicc): #dicc --> lista de tuplas ordenadas por partidos ganados
    # dicc = {'Alemania': [1, 0, 0], 'Escocia': [0, 0, 1], 'Argentina': [1, 0, 0]}
    # dicc.items() = ('Alemania',[1, 0, 0]) ('Escocia',[0, 0, 1]) ('Argentina',[1, 0, 0])
    return sorted(dicc.items(), key= lambda x: x[1][0], reverse=True)


def mostrar_dicc (resultados): #('Argentina', [1, 0, 0])
    for equipo in resultados:
        if equipo[1][0] > 0:
            print(f'{equipo[0]:<15}{equipo[1][0]:>5}')

def main ():

    #PUNTO 1:
    copa_america = open('Python\\archivos de texto\\copa_america.csv','r')
    eurocopa = open('Python\\archivos de texto\\eurocopa.csv','r')
    ambas_copas = open('Python\\archivos de texto\\ambas_copas.csv', 'w')

    merge(copa_america, eurocopa, ambas_copas)

    copa_america.close()
    eurocopa.close()
    ambas_copas.close()

    #PUNTO 2:

    ambas_copas = open('Python\\archivos de texto\\ambas_copas.csv', 'r')
    dicc_resultados = generar_dicc(ambas_copas)
    ambas_copas.close()

    #PUNTO 3:

    resultados_ordenados = ordenar_dicc(dicc_resultados) #son tuplas
    mostrar_dicc(resultados_ordenados)

main()