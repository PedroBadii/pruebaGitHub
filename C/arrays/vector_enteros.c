/*
Escribir un programa modular que permita cargar una serie de números enteros en un vector. No se conoce la cantidad 
exacta de datos, pero se sabe que no superan los 100.  Informar el valor mínimo, la cantidad de veces que aparece y 
la/s posición/es que ocupa.
*/

#include <stdio.h>

#define MAX_F 100

typedef int vector[MAX_F];

int solicitar_datos (vector serie){ //solicita a un usuario que cargue datos en un vector. Devuelve el max logico
        printf("Ingrese una secuencia de numeros. Máximo permitido de 100: ");
        int max_log = 0;
    for (int i=0; i<MAX_F; i++){
        scanf("%d", &serie[i]);
        max_log++;
    }
    return max_log;
}

void analizar_minimo (vector serie, int max_log){ //toma un vector e imprime el menor valor, la cant de veces y posiciones
    int min = serie[0];
    int cant = 0;
    vector posiciones;
    for (int i=1; i<=max_log; i++){
        if (serie[i]<min){
            min = serie[i];
            cant = 0;
        } else if (serie[i]==min){
            cant++;
        }
    }
    }

int main (){

    vector serie;
    int max_logico = solicitar_datos(serie);
    analizar_minimo(serie, max_logico);

    return 0;
}