/*
Intercambio de Valores (Uso de Punteros)
Crea una función que reciba dos punteros a enteros. La función no debe devolver nada 
(void), pero debe modificar los valores en las direcciones de memoria recibidas, 
intercambiándolos de lugar.

Conceptos clave: Declaración de punteros como parámetros, desreferenciación de punteros 
(usando * para acceder al valor) y el concepto de "paso por referencia". Necesitarás 
una variable auxiliar temporal dentro de la función.
*/

#include <stdio.h> 

void intercambiar_punteros (int *puntero1, int *puntero2) {
    int auxiliar;
    auxiliar = *puntero1;
    *puntero1 = *puntero2;
    *puntero2 = auxiliar;
}

int main () {
    int var1 = 1;
    int var2 = 2;
    printf("La direccion de memoria de %d es %p\n", var1, &var1);
    printf("La direccion de memoria de %d es %p\n", var2, &var2);
    int *puntero1 = &var1;
    int *puntero2 = &var2;
    printf("El puntero 1 apunta a %p y contiene %d\n", puntero1, *puntero1);
    printf("El puntero 2 apunta a %p y contiene %d\n", puntero2, *puntero2);
    intercambiar_punteros(puntero1, puntero2);
    printf("Aplicada la funcion 'cambiar punteros'\n");
    printf("Ahora el puntero 1 contiene %d\n", *puntero1);
    printf("Ahora el puntero 2 contiene %d\n", *puntero2);
    return 0;
}