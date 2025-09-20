                     #-------------EJERCICIO TERMINADO/ENTREGADO--------------#
def sumar_matrices(m1, m2):
    resultado = []

    for fil in range(len(m1)): #este for sucede tres veces
        resultado_fila = []

        for col in range(len(m1[fil])): #esto sucede 3 veces por cada vez del for de arriba
            resultado_fila.append(m1[fil][col] + m2[fil][col])

        resultado.append(resultado_fila)

    return resultado



def main ():
    m1 = [
        [1,2,3],
        [5,6,7],
        [4,8,9]
    ]
    m2 = [
        [11,12,32],
        [53,62,72],
        [42,84,96]
    ]

    m3 = sumar_matrices(m1,m2)

    print(m3)

main()
