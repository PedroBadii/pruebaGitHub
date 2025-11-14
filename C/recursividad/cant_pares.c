/*
Desarrollar una función recursiva que reciba un arreglo de enteros y su
máximo lógico. La función debe retornar la cantidad de números pares
presentes en el arreglo.
Ejemplo:
[23, 44, 68, 2, 24, 12] -> 5
Utilizar el siguiente código base:
*/

#include <stdio.h>
#include <stdbool.h>

int cantidad_pares(int numeros[], int ml){

    if (ml==0) {
        return 0;
    } else if ((numeros[ml-1] % 2)==0){
        return cantidad_pares(numeros, ml-1) + 1;
    } else {
        return cantidad_pares(numeros, ml-1);
    }
}

int main(){
    int numeros[] = {23, 44, 68, 2, 24, 12};
    int i, ml = sizeof(numeros) / sizeof(int); //24/4=6
        for (i = 0; i < ml; i++)
        printf("%d ", numeros[i]);
        printf("Cantidad de pares: %d.\n", cantidad_pares(numeros, ml));
    return 0;
}