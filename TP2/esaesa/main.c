#include <stdio.h>
#include <stdlib.h>
#include "agregar.c"

int main(){

	float number;
	int result;
	
	printf("Ingrese un número float: ");
	scanf("%f", &number);
	
	result= agrego_uno(number);
	
	printf("Result: %d\n", result)
	
	return 0;

}
