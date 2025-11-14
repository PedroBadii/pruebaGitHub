/*
Definir una función pertenece recursiva en C que recibe un vector de enteros por parámetro, su tamaño y un 
valor entero y devuelve 1 si dicho valor está en el vector, 0, en caso contrario.
int pertenece(int vec[], int n, int valor);
*/

#include <stdio.h>

int pertenece(int *vector, int tamaño, int num){

    if (tamaño==0){
        return 0;
    } else if (vector[tamaño-1]==num){
        return 1;
    }
    return pertenece(vector, tamaño-1, num);
}

int main (){
    int vector[] = {6,5,4,3,2,1};
    int tamaño = 6;
    int num = 9;
    int pert = pertenece(vector, tamaño, num);
    printf("%d", pert);

    return 0;
}