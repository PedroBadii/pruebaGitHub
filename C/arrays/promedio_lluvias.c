/*
Escribir un programa modular que solicite el ingreso de la cantidad de mililitros llovidos en la semana, 
de lunes a domingo, de 0 a 23hs.  El ingreso de datos es por día comenzando el lunes, y para cada día, 
por hora de 0 a 23. 
Informar el promedio de mililitros llovidos para cada día de la semana.
*/
/* lo que esta pidiendo es que el usuario cargue un valor de ml de lluvias por cada hora y por cada dia
de la semana, sin darle nombre a los dias. Lunes=1, martes=2, etc. 
*/

#include <stdio.h>

#define MAX_HS 24
#define MAX_DIAS 7

void solicitar_lluvias(matriz_lluvias) //toma una matriz vacia y la completa con los datos del usuario
    for (int dia=0, dia<MAX_DIAS, dia++){
        printf("Ingrese los ml de agua")
    }

    

void mostrar_promedio(matriz_lluvias) // toma la matriz, calcula el promedio e imprime

int main () {
    // primero creo una matriz que simbolice horas y dias
    int lluvias[MAX_DIAS][MAX_HS];
    // solicito al usuario que cargue las lluvias en la matriz
    solicitar_lluvias(lluvias);
    mostrar_promedio(lluvias)

    return 0;
}