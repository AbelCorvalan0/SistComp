Este archivo se encuentra en edición. Se adjunta la información de las  primeras actividades (implementación de Driver1, Driver2, Driver3, Driver4) en el siguiente link: [TP#5 - Drivers](https://github.com/AbelCorvalan0/SistComp/blob/master/TP5/TP%20%235%20-%20Drivers.pdf)


# TP #5 Drivers - Sistemas de Computación

## Integrantes

- Corvalán, Abel Nicolás - Ing. Electrónica
- Soria, Federico - Ing. en Computación

## Introducción

Un `driver` es aquel que conduce, administra, controla, dirige, monitorea la entidad bajo su mando. Un `bus driver` hace eso con un "bus". De manera similar, un `device driver` hace lo mismo con un dispositivo. Un dispositivo puede ser cualquier periférico conectado a una computadora, por ejemplo, un mouse, un teclado, una pantalla/monitor, un disco duro, una cámara, un reloj, etc.

Un `driver` puede ser una persona o sistemas automáticos, posiblemente monitoreados por otra persona. Del mismo modo, el `device driver` podría ser una pieza de software u otro periférico/dispositivo, posiblemente controlado por un software. Sin embargo, si se trata de otro periférico/dispositivo, se denomina `device controller` en el lenguaje común. Por `driver` solo nos referimos a un `software driver`. Un `device controller` es un dispositivo en sí mismo y, por lo tanto, muchas veces también necesita un `driver`.

Los ejemplos generales de `device controller` incluyen controladores de disco duro, controladores de pantalla, controladores de audio para los dispositivos correspondientes. Ejemplos más técnicos serían los controladores para los protocolos de hardware, como un controlador IDE, un controlador PCI, un controlador USB, un controlador SPI, un controlador I2C, etc. 

## Marco teórico


### Driver: 

Se trata de un software que permite al sistema operativo interactuar con un periférico, creando una abstracción del hardware y proporcionando una interfaz -posiblemente estandarizada- para utilizarlo. Se puede graficar como un manual de instrucciones que indica cómo controlar y comunicarse con un dispositivo en particular. 

### CDD (Character Device Drivers) y CDF (Common Driver Framework):

Son un tipo de controlador de dispositivo en el sistema operativo Linux que manejan dispositivos que transmiten datos de manera secuencial, es decir, carácter por carácter.
A diferencia de los controladores de bloques, que manejan dispositivos que acceden a los datos en bloques (como discos duros). Los CDD leen y escriben datos carácter por carácter.

Estos drivers interactúan directamente con el kernel de Linux y pueden responder a interrupciones de hardware, administrar buffers de entrada y salida, y proporcionar interfaces de `ioctl` (entrada/salida controlada) para operaciones específicas del dispositivo.

### Drivers y buses:

En la siguiente figura se muestra la interacción de los drivers y buses:

![alt text](<img/Drivers y bus.png>)

Los `bus driver` proporcionan una interfaz específica de hardware para los correspondientes protocolos de hardware y son las capas de software (horizontales) más bajas de un sistema operativo. 

Sobre ellos se encuentran los `device driver`, que operan sobre los dispositivos subyacentes utilizando las interfaces de capa horizontal y, por lo tanto, son específicos del dispositivo.

La idea de escribir estos `drivers` es proporcionar una abstracción del hardware para las aplicaciones de usuario a través del sistema operativo. Ofrecer una interfaz común para el usuario que será específica para cada sistema operativo. 

Un `device driver` tiene dos partes: 

    1- Una específica del dispositivo 
    2- Otra específica del sistema operativo. 



## Primeras tareas

Para simular la interfaz GPIO (General-Purpose Input/Output) en Raspberry Pi basado en qemu, el programa `qemu-rpi-gpio` interactúa con qemu implementando el protocolo `qtest`.

Como primer actividad del trabajo práctico se necesita compilar un fork de Qemu con soporte de interrupciones GPIO. Para esto realizamos un fork del QEMU proporcionado por la cátedra. Se utilizó el comando build para crear el directorio y compilarlo.

![image](https://github.com/AbelCorvalan0/SistComp/assets/116111472/0b6bc8d3-c2fc-4136-ba4c-f2f0df490431)

![image](https://github.com/AbelCorvalan0/SistComp/assets/116111472/f7af58b2-42c1-4a47-9531-b7db68709777)

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

Se verifican las modificaciones en el estado del GPIO modificado (pin 4) de la Raspberry Pi emulada.

![alt text](img/cat.png)

Desde el terminal de qemu se puede escribir y leer valores de los pines del dispositivo emulado.

Se carga el módulo `gpio_module.c` ubicado en el directorio `/TP5/qemu-gpio/source/`.

![alt text](<img/modulo cargado.png>)

Se realiza el seteo de valores en los pines configurados.

![alt text](<img/gpio set 10.png>)

En la simulación de la Raspberry Pi se obtiene el valor del pin 1.

![alt text](<img/sensor 1.png>)

Se modifica el valor del pin mediante el GPIO manager.

```
(gpio)> set 1 1
b'OK\r\n'
```

Se obtiene el nuevo valor del pin 1.

![alt text](<img/sensor 1 cc.png>)

Se modifica al pin 2 para leer su valor.

![alt text](<img/sensor 2.png>)
