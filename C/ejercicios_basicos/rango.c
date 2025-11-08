/*
Escribe una función que reciba tres enteros: valor, minimo y maximo. La función debe 
devolver 1 (representando "verdadero") si valor se encuentra dentro del rango (incluyendo 
los extremos minimo y maximo), y 0 (representando "falso") si está fuera de ese rango.
*/

#include <stdio.h>

int rango (float valor, float min, float max) {
    int en_rango = 0;
    if (valor <= max && valor >= min) {
        en_rango = 1;
    }
    return en_rango;
    }

int main (){
    printf("Dentro del rango: %d\n",rango(5, 3, 6));
    printf("Fuera del rango: %d",rango(5.5, 3, 5));
}