/*
Escribir un programa modular que permita cargar una serie de números enteros en un vector. No se conoce la cantidad 
exacta de datos, pero se sabe que no superan los 100.  Informar el valor mínimo, la cantidad de veces que aparece y 
la/s posición/es que ocupa.
*/

#include <stdio.h>

#define MAX_F 100

typedef int vector[MAX_F];

int solicitar_datos (vector serie){ //solicita a un usuario que cargue datos en un vector. Devuelve el max logico
    printf("Ingrese una secuencia de numeros. Maximo permitido de 100. Para finalizar, ingrese cero: \n");
    int max_log = 0;
    int i = 1;
    while (i!=0 && max_log<MAX_F){
        scanf("%d", &i);
        if (i != 0) {
            serie[max_log] = i;
            max_log++;
        }
    }    
    return max_log;
}

void analizar_minimo (vector serie, int max_log){ //toma un vector e imprime el menor valor, la cant de veces y posiciones
    vector posiciones;
    int min = serie[0];
    int cant = 0;
    for (int i=0; i<max_log; i++){
        if (serie[i]<min){
            min = serie[i];
            cant = 1;
            posiciones[0] = i+1;
        } else if (serie[i]==min){
            posiciones[cant] = i+1;
            cant++;
        }
    }
    printf("El minimo ingresado es %d y aparece %d veces.\n", min, cant);
    printf("Las posiciones en las que aparece son: ");
    for (int i=0; i<cant; i++){
        printf("%d, ", posiciones[i]);
    }
}

int main () {

    vector serie;
    int max_logico = solicitar_datos(serie);
    if (max_logico!=0){
        analizar_minimo(serie, max_logico);
    } else {
        printf("Usted no ha ingresado ningun numero");
    }

    return 0;
}