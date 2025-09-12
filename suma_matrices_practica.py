def suma_matrices(m1,m2):
    matriz_resultante = []

    for i in range(len(m1)):
        lista_sumada = []
        for j in range(len(m2[i])):
            suma = m1[i][j]+m2[i][j]
            lista_sumada.append(suma)

        matriz_resultante.append(lista_sumada)

    return matriz_resultante

def main():
    matriz1 = [[1,2,3],[4,5,6,7,1,2],[7,8,9],[1,2,3],[6,5,4]]
    matriz2 = [[3,2,1],[6,5,4,1,9,3],[5,6,4],[9,4,2],[7,6,2]]
    m3 = suma_matrices(matriz1,matriz2)

    print(m3)

main()