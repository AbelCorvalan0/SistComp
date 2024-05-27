# TP #2 Stack Frame - Sistemas de Computación

## Introducción

Los sistemas compuestos por hardware y software utilizan arquitecturas de capas para desarrollar aplicaciones complejas. En las capas superiores se trabaja con lenguajes de alto nivel. En la capa inferior, siempre está el hardware puro y duro. Inmediatamente encima está la capa de lenguaje de bajo nivel, podríamos decir más amigable con el hardware.

El lenguaje **ensamblador** es un lenguaje propio de la arquitectura y un intento de construir un lenguaje más accesible con el programador.
Los lenguajes de alto nivel, para controlar el hardware y su interacción con los sistemas físicos que lo rodean, necesitan acceder al hardware a través de los lenguajes de bajo nivel. Para ello utilizan convenciones de llamadas.
Entender cómo funciona una convención de llamada nos acercará a un conocimiento de sumo interés para áreas de desarrollo de sistemas críticos, seguridad y también para profundizar sobre el conocimiento de la interacción entre software y hardware.

Una API de REST (Represntational State Transfer) es un tipo de API que se basa en principio y restricciones arquitectónicas específicas diseñadas para sistemas distribuidos como la web. EST es un estilo de arquitectura que define un conjunto de restricciones y propiedades basadas en el protocolo HTTP. Las API RESTful son conocidas por su simplicidad y escalabilidad.

## Objetivo

Se debe diseñar e implementar calculos en ensamblador. La capa superior recuperará información de una API REST. Los datos de consulta realizados deben ser entregados a un programa en C que convocará rutinas en ensamblador para que hagan los cálculos de conversión y devuelvan los resultados a las capas superiores. Luego el programa en Python mostrará los cálculos obtenidos.

Se debe utilizar el stack para convocar, enviar parámetros y devolver resultados, es decir, las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

## Desarrollo

Se debe instalar, por medio de una termianl, el conjunto de herramientas necesarias para compilar software desde el código fuente (compilador GCC, make, entre otras).

```sh
sudo apt install build-essential nasm gcc-multilib g++-multilib
```

### Interfaz de usuario

Se realiza un interfaz de usuario la cual muestra los países de los cuales se tiene su respectivo Índice de GINI para un determinado año. 

Para ejecutar la misma se debe ejecutar el archivo `indexGINI.sh` desde el terminal con el siguiente comando:

```sh
./indexGINI.sh
```
Se abrirá la interfaz gráfica, que en primer instancia solicitará el país del cuál se desea obtener la información.
<center>
    <img src="img/Interfaz 1.png">
</center>



<center>
    <img src= "img/Interfaz 2.png">
</center>


<center>
    <img src= "img/Interfaz 3.png">
</center>


### Compilación del programa con GDB (GNU Debugger)

Se debe ejecutar el archivo *compiler.sh* desde el terminal con el siguiente comando.

```sh
./compiler.sh
```

Se abrirá la herramienta de depuración GDB (GNU Debugger) para ejecutar el archivo *result* en forma controlada, e identificar como varían los valores de los registros de la computadora.

Se colocan breaks para analizar el comportamiento de los registros en la línea 11 del archivo `main.c` y línea 4 `sum_GINI.c`. 

<!-- PONER IMÁGENES DE LOS CÓDIGOS CORRESPONDIENTES -->

```c
1  #include <stdio.h>
2  #include "sum_GINI.c"
3
4   int main() {
5     float number;
6     int result;
7
8     printf("Ingrese un número (formato float): ");
9     scanf("%f", &number);
10
11    result= agrego1(number);     //Breakpoint
12
13    printf("Result: %d\n", result);
14
15    return 0;
16 }
```

```c
1 extern int asm_operation(float);
2
3 int agrego1(float n){
4    int res= asm_operation(n);    //Breakpoint
5    return res;
6 }
```

Al iniciar el debugueo se pide un valor para convertir a tipo float.

<center>
    <img src="img/gdb 1.png">
</center>

Se ingresa el valor "2" para que procese el programa.

<center>
    <img src="img/gdb 2.png">
</center>

Se inspecciona el valor de los registros `esp` y `ebp` antes de ejecutar el siguiente paso en el debugueo. Esto es para verificar que el `esp` modifique su valor y al terminar el llamado a la función del código assembler `operation.asm` coincidan los valores el registro `esp` y el `ebp`.

<center>
    <img src="img/gdb 3.png">
</center>

<!--- Moviemientos en el Stack

El EIP (Instruction poninter siempre apunta a la siguiente línea de código (1020 para a 1022 y así).

Cuando se hace un llamado a una función el ESP (Stack Pointer) decrementa su valor por ejemplo de 0019 a 0015 (-4)

El ESP apunta en la memoria que tiene valores de la siguiente forma.

0000
0004
0008
000C
0011
0015    1026 (Acá se almacena la dirección de la siguiente línea luego del retorno del la función llamada)
0019    406F
001D    102C


El ESP al restar -4 por cada paso, se va apilando los datos hacia arriba.


 --->

Luego se muestra como varía el `esp` (Stack Pointer)