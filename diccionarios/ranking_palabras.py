                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir un programa que solicite el ingreso de un texto y luego informe un ranking de
las palabras que aparecen en el texto.
El texto ingresado debe tener como mínimo 20 palabras. En caso de no tener las
palabras suficientes, solicitar se ingrese más texto, que debe ser agregado al ya
existente.
Considere palabras que sólo estén formadas por letras.
Tenga en cuenta que seguido a una palabra, pueden estar los siguientes signos de
puntuación: “,;.:”, en este caso, se debe quitar el signo.
No debe diferenciar entre mayúsculas y minúsculas, por ejemplo: si aparecen en el
texto las siguientes palabras: “sol”, “Sol”, “SOL”; se deben contabilizar 3 ocurrencias
de la palabra “sol” como clave.
No utilice métodos tales como count, find, index.
Imprima el ranking, ordenado descendentemente, por la cantidad de ocurrencias de la
palabra.
'''
def separar_palabras(texto):

    # palabras = texto.lower().split() no lo uso porque quizás no se puede usar el metodo split
    palabras = []
    inicio_palabra = 0
    texto_min = texto.lower() #entiendo que este si se puede usar

    for i in range(len(texto_min)):
        palabra = ''
        if texto_min[i] == ' ':
            if texto_min[i-1] in ',;.:':
                palabra = texto_min[inicio_palabra:i-1]
            else:
                palabra = texto_min[inicio_palabra:i]
            palabras.append(palabra)

            inicio_palabra = i+1

    palabras.append(texto_min[inicio_palabra:])

    return palabras
    


def ranking_palabras(lista):

    dicc = {}

    for palabra in lista:
        if palabra not in dicc:
            dicc[palabra] = 1
        else:
            dicc[palabra] += 1
    
    return dicc


def mostrar(lista):
    
    for palabra in lista:
        print('{0:<10}{1:>2}'.format(palabra[0],palabra[1]))



def main ():

    lista_palabras = separar_palabras(input('Ingrese un texto con 20 palabras o mas: '))

    while len(lista_palabras)<20:
        lista_palabras = separar_palabras(input('El texto debe contener 20 palabas, intentelo nuevamente: '))

    lista_ordenada = sorted(ranking_palabras(lista_palabras).items(), key=lambda x: x[1], reverse=True)

    mostrar(lista_ordenada)

main()