
'''
Ejercicio clase archivos de texto (csv).
Recorrer el archivo maestro de clientes, y aplicar al saldo del cliente una actualización del 50%. 
Mostrar los datos del cliente, con su saldo original y el actualizado. Al mismo tiempo, generar un 
nuevo archivo que contenga en lugar del saldo original, el saldo actualizado.
'''

#falta modularizar y debuggear
def leer():

    maestro_nuevo = open('archivos de texto\\maestro_con_aumento.csv','w')

    with open('archivos de texto\\maestro.csv') as archivo:

        for linea in archivo:
            nro_cliente, nombre, saldo = linea.strip('/n').split(',')
            nro_cliente = float(nro_cliente)
            saldo = float(saldo)
            saldo_nuevo = saldo * 1.5

            print('{0:3}\t{1:15}\t{2:5}\t{3:7}'.format(nro_cliente, nombre, saldo, saldo_nuevo))

            linea_nueva = '{},{},{}\n'.format(nro_cliente, nombre, saldo_nuevo)
            maestro_nuevo.write(linea_nueva)

    return

leer()