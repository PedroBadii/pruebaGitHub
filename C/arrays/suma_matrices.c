/*
Dadas dos matrices A y B cuadradas de igual dimensión, tales que A∈Rn×n y B∈Rn×n
Escribir un programa que permita cargar su dimensión y sus datos. El
programa debe sumarlas y mostrar la matriz resultante. Para la estructura de
datos considere un tamaño máximo de 10 (1 <= n <= 10).
*/

#include <stdio.h>

#define MF 10

typedef float matriz [MF][MF];

void sumar_matrices(matriz m_a, matriz m_b, matriz res, int dim){
    for (int i=0; i==dim; i++){
        for (int j=0; j==dim; j++){//chequear i==0 y j==0
            printf("Ingrese el valor para la posicion %d %d", i, j);
            scanf("%d", res[i][j]);
        }
}
}

int main(){

    int dim = solicitar_dim();
    matriz m_a;
    matriz m_b;
    completar_matriz(m_a);
    completar_matriz(m_a);
    matriz res;
    sumar_matrices(m_a, m_b, dim);

    return 0;
}