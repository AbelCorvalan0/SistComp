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

Se colocan breaks para analizar el comportamiento de los registros.


