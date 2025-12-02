'''
Una fábrica de alimentos procesa distintos lotes de producción. La información se guarda en un archivo produccion.csv 
ordenado por Planta y, dentro de cada planta, por Línea de Producción.

Datos del archivo: Planta, Linea_Produccion, Codigo_Lote, Kilos_Producidos (Todos son Strings menos Kilos que es entero)

Se pide un programa modular en Python que:

A) Reporte de Producción (Corte de Control): Recorriendo una sola vez el archivo y sin cargarlo todo en memoria, muestre
por pantalla un reporte detallado.
Debe mostrar el nombre de la Planta.
Dentro de cada planta, listar cada Línea de Producción y el total de kilos producidos en esa línea.
Al cambiar de planta, mostrar el total acumulado de kilos de esa planta específica.
Al final de todo, informar el Total General de kilos producidos por la fábrica.

Ejemplo de salida:

Planta: NORTE
   Línea: L1 - Kilos: 300
   Línea: L2 - Kilos: 500
Total Planta NORTE: 800

Planta: SUR
   Línea: L1 - Kilos: 1050
   Línea: L3 - Kilos: 2000
Total Planta SUR: 3050

Total General Fábrica: 3850

B) Rendimiento por Lote (Diccionario): Realizando una nueva lectura del archivo, generar un diccionario donde:
Clave: Codigo_Lote (String).
Valor: Un entero indicando los Kilos_Producidos. (Nota: Un mismo lote puede aparecer fragmentado en varias líneas si 
se procesó en etapas, debés acumular los kilos).

C) Ranking de Lotes: En base al diccionario del punto B, generar un archivo ranking_lotes.txt.
Ordenado de Mayor a Menor por kilos.
Formato: Lote: [Codigo] - Total: [Kilos]
'''

#----- PUNTO A -----#

def leer(archivo):
    
    linea = archivo.readline()
    
    if linea:
        planta, linea_prod, cod_lote, kilos =  linea.rstrip().split(',')
        kilos = int(kilos)
    else:
        planta, linea_prod, cod_lote, kilos = ['', '', '', 0]
    
    return planta, linea_prod, cod_lote, kilos # ('NORTE', 'L1', 'AAA01', 100)

def generar_informe(archivo):
    
    planta, linea_prod, cod_lote, kilos = leer(archivo)
    total_fabrica = 0
    
    while planta:
        
        total_planta = 0
        planta_actual = planta
        print(f'Planta: {planta_actual}')
        
        while planta_actual == planta: #strings
        
            linea_prod_actual = linea_prod
            total_linea = 0
        
            while linea_prod_actual == linea_prod and planta_actual == planta: #strings
                
                total_linea += kilos
                planta, linea_prod, cod_lote, kilos = leer(archivo)
                
            print(f'Línea: {linea_prod_actual} - Kilos: {total_linea}')
            total_planta += total_linea
    
        print(f'Total planta {planta_actual}: {total_planta}')
        total_fabrica += total_planta
        
    print(f'Total General de la Fabrica: {total_fabrica}')
    
#----- PUNTO B -----#    
            
def generar_dicc(archivo):
    
    dicc_lotes = {}
    planta, linea_prod, cod_lote, kilos = leer(archivo)
    
    while cod_lote:
        
        if cod_lote not in dicc_lotes:
            dicc_lotes[cod_lote] = 0
            
        dicc_lotes[cod_lote] += kilos
        planta, linea_prod, cod_lote, kilos = leer(archivo)
        
    return dicc_lotes

#----- PUNTO C -----#
    
def ordenar_dicc(dicc):
    return sorted(dicc.items(), key=lambda x: x[1], reverse=True)

def generar_ranking(tuplas, archivo):
    LOTE = 0
    TOTAL_K = 1
    for tupla in tuplas:
        archivo.write(f'Lote: {tupla[LOTE]} - Total: {tupla[TOTAL_K]}\n')
        

def main():
    #PUNTO A
    produccion = open('Python\\archivos de texto\\fabrica\\produccion.csv', 'r')
    generar_informe(produccion)
    
    #PUNTO B
    produccion.seek(0)
    dicc_lotes = generar_dicc(produccion)
    produccion.close()
    
    #PUNTO C
    ordenado = ordenar_dicc(dicc_lotes) #ordenado son tuplas
    ranking = open('Python\\archivos de texto\\fabrica\\ranking_lotes.txt','w')
    generar_ranking(ordenado, ranking)
    ranking.close()
    
main()