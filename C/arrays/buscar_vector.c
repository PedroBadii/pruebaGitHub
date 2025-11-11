/*
Escribí una función que reciba un vector de elementos enteros, el máximo lógico y un elemento p del mismo tipo que los 
elementos del vector. Buscar p en el vector y devolver la primer posición que ocupa en caso de encontrarlo o -1 en caso
contrario. Suponer que como máximo el vector puede tener 20 elementos. Probar con 3 casos de prueba diferentes la función.
*/

#include <stdio.h>

#define MAX_ELEMENTOS 20

int buscador (int *vector, int max_log, int elemento){
    int posicion = -1;
    int i = 0;
    while (posicion == -1 && i<max_log){
        if (elemento == vector[i]){
            posicion = i;
        }
        i++;
    }

    return posicion;
} //5,2,3

int solicitar_vector(int *vector){

    printf("Ingrese una secuencia de numeros que conformaran el vector. Para finalizar, ingrese cero: \n");

    int max_log = 0;
    scanf("%d", &vector[max_log]);

    while (vector[max_log]!=0){
        max_log++;
        scanf("%d", &vector[max_log]);
    }

    return max_log;
}


int solicitar_elemento(){
    int elemento;
    printf("Ingrese una elemento a buscar en el vector: ");
    scanf("%d", &elemento);
    return elemento;
}

int main () {
    int vector[MAX_ELEMENTOS];
    int max_log = solicitar_vector(vector);
    int elemento = solicitar_elemento();
    printf("La posicion del elemento es la posicion %d\n -1 significa ausencia", buscador(vector, max_log, elemento));
    return 0;
}
