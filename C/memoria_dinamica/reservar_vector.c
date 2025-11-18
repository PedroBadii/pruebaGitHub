/*
Escribir un programa el cual reserve memoria dinámica para almacenar una
cierta cantidad de números enteros (n * int), este valor n debe ser ingresado por
el usuario. Luego solicitarle que ingresé n valores enteros ingresados de a uno y
almacenarlos en la memoria previamente reservada. Mostrar luego todos los
valores ingresados. Liberar la memoria reservada al finalizar el programa.
*/

#include <stdlib.h>
#include <stdio.h>

int solicitar_cant (){
    int cant_enteros;
    printf("Ingrese la cantidad de enteros que ingresara en el proximo paso: ");
    scanf("%d", &cant_enteros);
    return cant_enteros;
}

void solicitar_enteros(int *puntero, int cant_enteros){

    printf("Ingrese los enteros de a uno. Por cada ingreso presione enter.\n");

    for (int posicion=0; posicion<cant_enteros; posicion++){
        printf("Ingrese el entero numero %d: ", posicion+1);
        scanf("%d",&puntero[posicion]);
    }

}

void mostrar(int *puntero, int cant_enteros){
    for (int posicion = 0; posicion < cant_enteros; posicion ++){
        printf("El elemento numero %d en ser ingresado fue el %d\n", posicion + 1, puntero[posicion]);
    }
}

int main (){

    int *puntero_num = NULL;
    int cant_enteros = solicitar_cant();
    puntero_num = malloc(cant_enteros * sizeof(int));

    if (puntero_num != NULL) {

        solicitar_enteros(puntero_num, cant_enteros);
        mostrar(puntero_num, cant_enteros);
        free(puntero_num);

    } else {
        printf("No se pudo reservar el espacio en memoria. Fin.");
    }
    return 0;
}