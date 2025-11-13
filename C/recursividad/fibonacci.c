/*
Serie Fibonaci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Ejemplos:
  f(2)=1
  f(3)=2
  f(4)=3
  f(5)=5
  f(6)=8
  f(7)=13
  f(8)=21
La función debe tomar el número de orden de la serie y devolver el valor en cuestión

*/

#include <stdio.h>

int fibonacci (int num){
    if (num == 0){
    return 0;
    }
    if (num == 1){
    return 1;
    }
    return fibonacci(num-1) + fibonacci(num-2); 
}

int main (){
    int num = 7;
    int res_5 = fibonacci(5);
    printf("Fibonacci 5 es %d\n", res_5);
    int res_7 = fibonacci(7);
    printf("Fibonacci 7 es %d", res_7);

    return 0;
}