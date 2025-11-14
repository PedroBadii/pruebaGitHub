/*
Dado un vector a ordenado ascendente de longitud ml y un elemento p del
mismo tipo que los elementos del vector, insertar p en el vector a de modo que
siga ordenado. Validar previamente que en el vector haya espacio libre para
guardar el nuevo dato. Se solicita resolver lo solicitado recorriendo una sola vez
el vector y sin utilizar un arreglo auxiliar.
Ejemplo:
nuevo elemento p=14
*/

#define MF 10

int validar (int max_log){
    int valido = 1;
    if (max_log == MF){
        valido = 0;
    }
    return valido;
}

void insertar_ordenado (int *vector, int max_log, int elemento){
    int i = max_log-1;
    while ( i>=0 && vector[i]>elemento){
        vector[i+1] = vector[i];
        i = i-1;
    }
    vector[i+1] = elemento;
}



int main () { //los datos que tengo son: el vector, MF y el entero p
    solicitar_vector();
    int ;

    return 0;
}