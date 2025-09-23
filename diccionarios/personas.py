                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Pedir al usuario campo por campo el ingreso de personas, el mismo usuario debe poder decidir cuando parar
 de ingresar personas. Cada persona tiene un nombre, una edad, un dni y una o más comidas preferidas 
 (el usuario ingresa cada comida una por una). El nombre de cada persona se asume único para este 
 ejercicio. Luego de decidir parar de ingresar personas, el usuario debe elegir un campo por el cual 
 ordenar las personas, estos pueden ser: por nombre alfabéticamente, por edad, por dni o por la cantidad
 de letras que tiene la primera comida preferida que ingresó el usuario. Luego de elegir el campo, el 
 usuario debe indicar si el ordenamiento es ascendentemente o descendentemente, el resultado final debe 
 tener formato de diccionario
'''

def solicitar_personas():
    dicc_personas = {}
    persona = input('Ingrese el nombre de una persona. Para terminar, ingrese 0: ')
    while persona != '0':

        comidas_preferidas = []

        edad = int(input('Ingrese la edad: '))
        dni = int(input('Ingrese el dni: '))
        comida = input('Ingrese su comida preferida: ')

        while comida != '0':
            comidas_preferidas.append(comida)
            comida = input('Ingrese otra comida preferida. Para terminar, ingrese 0: ')
    
        dicc_personas[persona] = [edad, dni, comidas_preferidas]

        persona = input('Ingrese el nombre de una persona. Para terminar, ingrese 0: ')

    return (dicc_personas)
        

def ordenar_personas(dicc_personas):

    personas_ordenadas = {}

    orden = int(input('Gracias. Ingrese un código de orden para las personas ingresadas \n' \
    '1 - Alfabéticamente por nombre \n' 
    '2 - Edad \n'
    '3 - DNI \n'
    '4 - cantidad de letras que tiene la primera comida preferida '))

    ascendente = int(input('¿Desea que se ordene de manera descendente? Presione 1 para si, 0 para no: '))
    
    if orden == 1:
        personas_ordenadas = dict(sorted(dicc_personas.items(), key=lambda x: x[0], reverse=ascendente))
    elif orden == 2:
        personas_ordenadas = dict(sorted(dicc_personas.items(), key=lambda x: x[1][0], reverse=ascendente))
    elif orden == 3:
        personas_ordenadas = dict(sorted(dicc_personas.items(), key=lambda x: x[1][1], reverse=ascendente))
    elif orden == 4:
        personas_ordenadas = dict(sorted(dicc_personas.items(), key=lambda x: len(x[1][2][0]), \
        reverse=ascendente))
    else:
        print('Ha ingresado una opción inválida. Se cierra el programa')

    return personas_ordenadas

def main():

    print(ordenar_personas(solicitar_personas()))

main()
        