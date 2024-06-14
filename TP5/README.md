Este archivo se encuentra en edición. Se adjunta la información en el siguiente link: [TP#4 - Módulos de Kernel]()


# TP #5 Drivers - Sistemas de Computación

## Integrantes

- Corvalán, Abel Nicolás - Ing. Electrónica
- Soria, Isaia - Ing. en Computación

## Introducción

## Teoría

Se trata de un software que permite al sistema operativo interactuar con un periférico, creando una abstracción del hardware y proporcionando una interfaz -posiblemente estandarizada- para utilizarlo. Se puede graficar como un manual de instrucciones que indica cómo controlar y comunicarse con un dispositivo en particular. 

Los CDD (Character Device Drivers, o Controladores de Dispositivos de Carácter) son un tipo de controlador de dispositivo en el sistema operativo Linux que manejan dispositivos que transmiten datos de manera secuencial, es decir, carácter por carácter.
A diferencia de los controladores de bloques, que manejan dispositivos que acceden a los datos en bloques (como discos duros), los CDD leen y escriben datos carácter por carácter.
Estos drivers interactúan directamente con el kernel de Linux y pueden responder a interrupciones de hardware, administrar buffers de entrada y salida, y proporcionar interfaces de ioctl (entrada/salida controlada) para operaciones específicas del dispositivo.

## Primeras tareas

Para simular la interfaz GPIO (General-Purpose Input/Output) en Raspberry Pi basado en qemu.

El programa `qemu-rpi-gpio` interactúa con qemu implementando el protocolo `qtest`.

Se instalan las librerías `socat`, `python3` y `pexpect`.

```sh
pip install-python3-pexpect socat
```

Para descargar las imagenes se necesita 7zip.

```sh
sudo apt install p7zip-full
```

Se ejecuta el siguiente script `./setup.sh` de shell que descarga una imagen de raspbian.

![alt text](img/setup.png)

Se ejecuta el programa de python `./qemu-rpi-gpio` para cargar el socket unix en qemu.

![alt text](<img/qemu gpio.png>)

Se ejecuta el script `./run.sh` que iniciará el raspberry pi virtual en conjunto con la aplicación de gpio.

![alt text](img/run.png)

Al ejecutar el archivo `./run.sh` se obtuvo el siguiente error para los dos integrantes del grupo.

![alt text](<img/error run 1.png>)

![alt text](<img/error run 2.png>)

Este error indica que QEMU requiere un tamaño de imagen sea una potencia de 2 (por ejemplo 1GiB, 2Gib, etc.)

Se resuelve con el siguiente comando en el terminal. 

```sh
qemu-img resize -f raw /home/abel/rootfs.orig/rootfs/kernel8.img 3G
```
Luego se obtuvo el siguiente error en la instalación del archivo `tmp-gpio.sock`.

Se crea el socket por medio de `socat`.

```sh
socat -d -d -lf /tmp/tmp-gpio.sock
```

Luego se verifica la existencia del mismo.

![alt text](<img/verificacion socket.png>)

Se exportan los pines de gpio.

![alt text](<img/gpio export.png>)

Con la interfaz de GPIO Virtual se realiza la prueba del pin 4.

Se pide un valor del pin 4, se obtiene false. Luego se setea al mismo pin un valor de 1, se pide su valor y se obtiene True.

![alt text](<img/gpio set get.png>)