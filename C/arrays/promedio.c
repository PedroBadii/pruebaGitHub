/*
Escribir un programa modular en lenguaje C, que solicite el ingreso de HASTA 10 números (podrían ser 
menos),  y luego muestre el promedio, y todos los números superiores al promedio calculado. 
El ingreso de datos puede terminar porque el usuario ingresó 0 o bien porque se alcanzó la cantidad 
máxima de elementos.
*/

#include <stdio.h>

#define MF 10

int solicitar_numeros(int *lista) {  /*toma el puntero de la lista y modifica los valores con lo ingresado. 
    tambien devuelve el maximo lógico de la lista*/
    int max_logico = 0;
    int num;
        printf("Ingrese numeros, si desea parar ingrese 0. Limite 10 numeros. ");
        do {
            printf("Ingrese un numero: ");
            scanf("%d", &num);
            if (num != 0){
                lista[max_logico] = num; //aca lista[i] ya es el valor lista[0] y va sumando 1
                max_logico++;
            }
        } while (max_logico < MF && num!=0 );

    return max_logico;
}

float promedio_lista (int *lista, int max_logico) { /*toma: puntero de lista, cant. elemento y devuelve el 
    promedio*/
    float promedio = 0;
    int suma = 0;
    for (int i=0; i<max_logico; i++){
        suma += lista[i];
    }
    
    if (max_logico!=0){

        promedio = (float)suma / max_logico; /*(float)suma hace que la operación sea float/int, devolviendo un 
    float. Si hiciera suma / max_logico el resultado sería int y truncaria los decimales*/
    }

    return promedio;
}

void numeros_mayores (int *lista, int max_logico, float promedio){ /*toma: puntero de lista, cant. elementos
    y el promedio calculado e imprime los mayores al promedio*/
    printf("Los numeros ingresados mayores al promedio son: ");
    for (int i=0; i<max_logico; i++){
        if (lista[i]>promedio){
            printf("%d ", lista[i]);
        }
    }
}

int main (){
    int lista[MF]; // lista queda como el puntero a la poscisión 0 del array creado
    int max_logico = solicitar_numeros(lista); //acá la lista ya quedo modificada con lo ingresado
    float promedio = promedio_lista(lista, max_logico);
    printf("El promedio de los numeros ingresados es %.2f\n", promedio);
    numeros_mayores(lista, max_logico, promedio);

    return 0;
}