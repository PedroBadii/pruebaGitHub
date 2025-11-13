/*
crear la funcion potencia de manera recursiva
*/
// base=2 exp=3

#include <stdio.h>

int potencia (int base, int exp){

    if (exp==1){
        return base;
    }
    
    return base*potencia(base, exp-1);   // 2 * potencia(2, 2)--> 2 * potencia(2,1)--> 2
}

int main (){

    int base = 2;
    int exp = 4;

    int res = potencia(base, exp);
    printf("El resultado es %d", res);

    return 0;
}