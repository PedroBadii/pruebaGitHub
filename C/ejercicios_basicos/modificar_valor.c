/*
Modificación Directa (Punteros y Matemática)
Escribe una función que reciba un puntero a un entero. La función debe leer el valor al que apunta, 
multiplicarlo por 5, y almacenar el nuevo resultado en la misma dirección de memoria.

Conceptos clave: Lectura y escritura de valores usando punteros, operadores matemáticosss.
*/

#include <stdio.h>

void modificacion_directa (int *puntero) {
    *puntero *= 5; /*    *puntero = *puntero * 5;    */
    printf("Funcion modificacion_directa\n");
}

int main (){
    int var1 = 2;
    int *puntero = &var1;
    printf("El puntero apunta a la direccion de memoria %p que tiene valor %d\n", puntero, *puntero);
    modificacion_directa(puntero);
    printf("El puntero apunta a la direccion de memoria %p que tiene valor %d\n", puntero, *puntero);
    return 0;
}