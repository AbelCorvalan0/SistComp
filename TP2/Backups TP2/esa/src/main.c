#include <stdio.h>
#include "sum_GINI"

int main() {
    float number;
    int result;

    printf("Ingrese un número (formato float): ");
    scanf("%f", &number);

    result= agrego1(number);

    printf("Result: %d\n", result);

    return 0;
}
