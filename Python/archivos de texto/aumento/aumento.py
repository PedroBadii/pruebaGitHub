
'''
Ejercicio clase archivos de texto (csv).
Recorrer el archivo maestro de clientes, y aplicar al saldo del cliente una actualización del 50%. 
Mostrar los datos del cliente, con su saldo original y el actualizado. Al mismo tiempo, generar un 
nuevo archivo que contenga en lugar del saldo original, el saldo actualizado.
'''

def aumento(maestro, maestro_nuevo):
    
    print(f"{'Numero cliente':<20}{'Nombre cliente':<20}{'Saldo':<6}{'Saldo actualizado':<10}\n")
    
    linea = maestro.readline()
    
    while linea:
        nro_cliente, nombre, saldo = linea.strip().split(',')
        nro_cliente = float(nro_cliente)
        saldo = float(saldo)
        saldo_nuevo = saldo * 1.5
            
        print(f'{nro_cliente:<20}{nombre:<20}{saldo:<6}{saldo_nuevo:<10}\n')
           
        maestro_nuevo.write(f'{nro_cliente},{nombre},{saldo_nuevo}\n')
        
        linea = maestro.readline()

def main():

    maestro = open('Python\\archivos de texto\\aumento\\maestro.csv','r')
    maestro_nuevo = open('Python\\archivos de texto\\aumento\\maestro_con_aumento.csv','w')
    
    aumento (maestro, maestro_nuevo)
    
    maestro.close()
    maestro_nuevo.close()

main()