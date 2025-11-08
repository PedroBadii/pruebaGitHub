/*
Desarrolla una función que reciba dos números (pueden ser float o double) y un carácter 
que represente una operación ('+', '-', '*', /'). La función debe devolver el resultado 
de aplicar esa operación matemática a los dos números.
*/

#include <stdio.h>

float operacion (float num1, float num2, char operador) {
    float resultado;
    if (operador == '+') {
        resultado = num1 + num2;
    } else if (operador == '-') {
        resultado = num1 - num2;
    } else if (operador == '*') {
        resultado = num1 * num2;
    } else {
        resultado = num1 / num2;
    }
    return resultado;
}

int main (){
    printf("Hago operaciones con los numeros 2 y 3\n");
    printf("El resultado de la operacion %-19s: %8.2f\n","suma es", operacion (2,3,'+'));
    printf("El resultado de la operacion %-19s: %8.2f\n", "resta es", operacion (2,3,'-'));
    printf("El resultado de la operacion %-19s: %8.2f\n", "multiplicacion es", operacion (2,3,'*'));
    printf("El resultado de la operacion %-19s: %8.5f\n", "division es", operacion (2,3,'/'));
    return 0;
}