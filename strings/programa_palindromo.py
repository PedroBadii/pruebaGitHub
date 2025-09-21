                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
'''
Escribir un programa que solicite el ingreso de palabras ó frases, y a medida que se ingresan informar 
si se trata de un palíndromo.
Validar que la palabra ó frase ingresada, sólo este formada por caracteres alfabéticos y por espacios 
en blanco.
El ingreso de las palabras ó frases, terminará cuando el usuario de enter, sin ingresar nada.
La solución debe ser estructurada en funciones, que sigan los lineamientos de la programación
estructurada. Reutilice el código de ejercicios anteriores.
'''

def limpiar_cadena(cadena): #este es para obtener una cadena nueva sin espacios ni mayúsculas
    cadena_min = cadena.lower()
    cadena_mod = ''
    for i in cadena_min:
        if i != ' ':
            cadena_mod += i
    return cadena_mod

def es_palindromo(cadena):

    cadena_mod = limpiar_cadena(cadena)
    palindromo = True
    i = 0

    while palindromo == True and (not cadena_mod[i] == cadena_mod[len(cadena_mod)-1-i]):
        palindromo = False
        i += 1

    return palindromo



def main():

    cadena = input("Ingrese una palabra o frase solo con caracteres alfabéticos: ")

    while not limpiar_cadena(cadena).isalpha():
        cadena = input("La frase contiene carácteres no alfabétivos, intentelo nuevamente: ")

    cadena_mod = ''
    cadena_mod = limpiar_cadena(cadena)
    
    if es_palindromo(cadena_mod):
        print('La frase es un palíndromo')
    else:
        print('La frase no es un palíndromo')

main()



