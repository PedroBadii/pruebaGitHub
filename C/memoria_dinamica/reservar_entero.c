/*
Escribir un programa el cual reserve memoria dinámica para almacenar un
número entero (int), le solicite al usuario el ingreso de un número y se asigna
dicho valor en la memoria reservada, luego mostrar dicho valor por pantalla
Liberar la memoria reservada al finalizar el programa.
*/

#include <stdio.h>
#include <stdlib.h>

void solicitar_num (int *puntero){
    printf("Ingrese un numero: ");
    scanf("%d", puntero);
}

void mostrar_num(int *entero){
    printf("El numero ingresado es %d y se encuentra en la direccion de memoria %p\n", *entero, entero);
    printf("Se procede a liberar la memoria\n");
}

int main (){

    int *puntero_num = NULL; //inicializar en NULL para sacar basura
    puntero_num = malloc(sizeof(int)); // sizeof(int) --> el espacio que ocupa 1 solo int que es 4 bytes
    // malloc(x espacio) --> reserva x espacio en memoria

    if (puntero_num != NULL){
        solicitar_num(puntero_num);

        mostrar_num(puntero_num);

        free(puntero_num);
    } else {
        printf("No se ha podido reservar memoria. Fin del programa.");
    }
    return 0;
}