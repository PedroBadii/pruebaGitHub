/*Desarrollar una función recursiva en lenguaje C que compruebe si un número es binario.
Un número binario está formado únicamente por ceros y unos.

Sugerencia:
recordar el uso de operadores % (mod) y / (div)
202 % 10 = 2 Esto sirve para separar el último digito, luego puedo ver si es 0 ó 1
202 / 10 = 20



Desde el main invocar a la función y mostrar un mensaje adecuado al usuario para todos estos casos de prueba:

es_binario(101) -> true
es_binario(2) -> false
es_binario(20) -> false
es_binario(1) -> true
es_binario(0) -> true
es_binario(100000) -> true
es_binario(100009) -> false
*/

#include <stdbool.h>
#include <stdio.h>

int es_binario (int num){

    if (num == 0 || num == 1){
        return true;
    }

    if (num % 10 != 0 && num % 10 != 1){
        return false;
    } else {
        return es_binario (num / 10);
    }
}

int main (){
    int pruebas[] = {101, 2, 20, 1, 0, 100000, 100009};
    int longitud_pruebas = sizeof(pruebas) / sizeof(pruebas[0]); //asi se calcula la longitud del arreglo
    for (int i = 0; i<longitud_pruebas; i++){
        bool resultado = es_binario(pruebas[i]);
        printf("El numero %d es binario: %s\n",pruebas[i], resultado ? "true" : "false");
    }
    return 0;
}