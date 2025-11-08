/*
Definir una función en c que:
recibe por parámetro un vecto de enteros y su longitud
a) Devuelve la sumatoria de todos los elementos
b)Devuelve la sumatoria de todos los elementos múltiplos de un valor que se recibe 
como tercer parámetro
*/

#include <stdio.h>

int sumar_elementos(int v[], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += v[i];
    }
    return suma;
}

int main() {
    int numeros[] = {3, 7, 2, 8, 5};
    int longitud = 5;

    int total = sumar_elementos(numeros, longitud);
    printf("La suma total es: %d\n", total);

    return 0;
}

