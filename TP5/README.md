Este archivo se encuentra en edición. Se adjunta la información en el siguiente link: [TP#4 - Módulos de Kernel]()


# TP #5 Drivers - Sistemas de Computación

## Integrantes

- Corvalán, Abel Nicolás - Ing. Electrónica
- Soria, Isaia - Ing. en Computación

## Introducción

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



Se ejecuta el script `./run.sh` que iniciará el raspberry pi virtual en conjunto con la aplicación de gpio.

![alt text](img/run.png)

Al ejecutar el archivo `./run.sh` se obtuvo el siguiente error para los dos integrantes del grupo.

![alt text](<img/error run 1.png>)

![alt text](<img/error run 2.png>)

Este error indica que QEMU requiere un tamaño de imagen sea una potencia de 2 (por ejemplo 1GiB, 2Gib, etc.)

Se resuelve con el siguiente comando en el terminal. 

```sh
qemu-img resize -f raw /home/abel/rootfs.orig/rootfs/kernel8.img 1G
```

