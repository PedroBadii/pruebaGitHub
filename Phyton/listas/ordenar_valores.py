
'''
Escribir un programa modular que haciendo uso de listas, permita:
1. El ingreso de una secuencia de valores, que termina con el valor 0.
2. Muestre los valores ingresados.
3. Muestre los valores hasta encontrar el 3er. valor impar ingresado inclusive.
4. Muestre los elementos que se encuentren en posiciones pares.
5. Muestre los elementos ordenados de menor a mayor, sin repetirlos.
En todos los casos, las salidas deben contener un título que indique lo que se está mostrando
y mostrar un valor por línea.
'''

def mostrar(titulo, lista):
    print('\n', titulo)#\n es un salto de linea y hay que ponerlo entre comillas siempre
    for i in lista:
        print(i) #aca no hace falta '\n' porque print en iteraciones lo hace por defecto

def tercer_impar(lista): #toma una lista y devuelve otra igual hasta el tercer impar inclusive
    lista_impares = []
    cant_impar = 0
    i = 0
    while cant_impar < 3 and i<len(lista):
        lista_impares.append(lista[i])
        if lista[i] % 2 != 0:
            cant_impar += 1
        i += 1
    return lista_impares
        
def pares(lista): #toma una lista y devuelve otra con las posciciones pares
    lista_pares = []
    for i in range(1, len(lista), 2): #1 para que empieze en el segundo, 2 para que tome solo los pares
        lista_pares.append(lista[i])
    return lista_pares

def menor_a_mayor(lista):
    return sorted(lista) #si usara .sort() mi lista quedaría modificada y ya no la podrían usar otras funx

def solicitar_lista():
    
    lista_valores = []
    valor = 1
    while valor != 0:
        valor = int(input('Ingrese un valor. Para no ingresar mas valores, ingrese 0:'))
        if valor != 0:
            lista_valores.append(valor)
    
    return lista_valores

def main ():

    lista = solicitar_lista()
    mostrar('Esta es la lista', lista)
    mostrar('Esta es la lista hasta el tercer impar incluido', tercer_impar(lista))
    mostrar('Estas son las posiciones pares', pares(lista))
    mostrar('Esta es la lista de menor a mayor', menor_a_mayor(lista))

main()

