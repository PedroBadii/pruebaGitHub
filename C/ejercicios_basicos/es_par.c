/*
Validación Compleja (Lógica Combinada)
Desarrolla una función que reciba un solo entero. Debe devolver 1 (verdadero) si el número es positivo 
(> 0) Y es par; O si el número es exactamente -100. Para cualquier otro caso, debe devolver 0 (falso).
*/

#include <stdio.h>

int par_o_100 (int num){
    int es_par_o_100 = 0;
    if (num == -100 || (num % 2 == 0 && num > 0)){
        es_par_o_100 = 1;
    }
    return es_par_o_100;
}

int main (){
    printf("Prueba con 5: %d\n", par_o_100 (5));
    printf("Prueba con 6: %d\n", par_o_100 (6));
    printf("Prueba con -5: %d\n", par_o_100 (-5));
    printf("Prueba con -6: %d\n", par_o_100 (-6));
    printf("Prueba con -100: %d\n", par_o_100 (-100));
}