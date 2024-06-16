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

![alt text](<img/Driver y bus horizontal.png>)

## Pruebas de drivers

Se clona el repositorio `device-drivers`.

```sh
git clone https://gitlab.com/sistemas-de-computacion-unc/device-drivers.git
```


### Drv1.c

Como vimos en el trabajo práctico anterior, cualquier driver de Linux consta de un constructor y un destructor. 
Se llama al constructor de un módulo cada vez que insmod logra cargar el módulo en el núcleo y al destructor del módulo cada vez que rmmod logra descargar el módulo del núcleo. 
Estas funciones se implementan con las macros `module_init()` y `module_exit()` incluidas en el encabezado de `module.h`.

Primero buscamos los drivers en el primer enlace proporcionado y para comenzar se trabajará con el `drv1.c`, éste es un módulo simple ya que sólo imprime un mensaje al registro del kernel al ser cargado y otro mensaje al ser descargado sin otra operación adicional.

![alt text](<img/Pruebas drivers/drv1/drv1 1.png>)

Se procede a compilar con `make all` y se verifica la información del  módulo mediante `modinfo`,de este modo se pueden ver atributos como la descripción, el autor o la versión.

![alt text](<img/Pruebas drivers/drv1/drv1 2.png>)

Se inserta el módulo en el kernel mediante `sudo insmod`, con `dmeg` se verifica su correcta instalación y la impresión del mensaje. 

![alt text](<img/Pruebas drivers/drv1/drv1 3.png>)

![alt text](<img/Pruebas drivers/drv1/drv1 4.png>)

![alt text](<img/Pruebas drivers/drv1/drv1 5.png>)

Como sucede con cualquier módulo, se remueve luego con `rmmod` por lo que se imprime el mensaje de la función `printk` del destructor `drv1_exit()`.

![alt text](<img/Pruebas drivers/drv1/drv1 6.png>)

### Drv2.c

Del mismo modo que antes, compilamos el drv2 y se revisa su información. 

![alt text](<img/Pruebas drivers/drv2/drv2 1.png>)

![alt text](<img/Pruebas drivers/drv2/drv2 2.png>)

Se inserta el módulo y se verifica que se imprimió correctamente el mensaje del constructor:

![alt text](<img/Pruebas drivers/drv2/drv2 3.png>)

![alt text](<img/Pruebas drivers/drv2/drv2 4.png>)

A diferencia del Drv1, se observan 2 números en el registro, esto es debido a que este módulo registra dinámicamente un rango de números de dispositivo de carácter al cargarse y se libera ese rango al descargarse. ¿Pero qué son estos números?
Cada archivo de dispositivo tiene asociado un par de números conocidos como major y minor.

- `Major Number`: Identifica el controlador de dispositivo que maneja las operaciones para ese dispositivo, o dicho de otra manera, varios dispositivos del mismo tipo (controlados por el mismo controlador) compartirán el mismo número mayor.

- `Minor Number`: Este valor identifica el dispositivo específico gestionado por el controlador. por lo que diferentes dispositivos del mismo tipo tendrán diferentes números menores.

En la función de inicialización (drv2_init), se reserva un número mayor y tres números menores para el dispositivo, imprimiendo un mensaje de éxito y los números asignados en el registro del kernel. En la función de limpieza (drv2_exit), se libera el rango de números de dispositivo y se imprime un mensaje de despedida. 
El numero major es 237 y el minor, 0. Esto se puede revisar  también mediante  cat /proc/devices donde se observa que el driver se cargó en el major 237.

![alt text](<img/Pruebas drivers/drv2/drv2 5.png>)

Al realizarse la asignación dinámica del número mayor (major number), no se puede anticipar cuál será el número asignado hasta que el módulo sea cargado por lo que dentro de la carpeta /dev no hay archivos creados para el driver.

![alt text](<img/Pruebas drivers/drv2/drv2 6.png>)

![alt text](<img/Pruebas drivers/drv2/drv2 7.png>)

![alt text](<img/Pruebas drivers/drv2/drv2 8.png>)

La implementación de esta asignación dinámica llama a la función `alloc_chrdev_region` para asignar dinámicamente un rango de números de dispositivo de carácter. Los parámetros de `alloc_chrdev_region` son:

- `&first`: Puntero a una variable dev_t donde se almacenará el primer número de dispositivo asignado.

``

- `0`: Número minor inicial en el rango.

- `3`: Cantidad de números minor en el rango (en este caso, se solicitan 3 números minors).

- `SdeC_Driver2`: Nombre del dispositivo (se usa para crear los archivos de dispositivo en /dev).


A continuación se crean entonces los ficheros del character device driver con mknod, asignando distintos MINORS al MAYOR ya determinado.

![alt text](<img/Pruebas drivers/drv2/drv2 9.png>)

Observamos que se crearon correctamente los device files mediante `grep`:

![alt text](<img/Pruebas drivers/drv2/drv2 10.png>)

Pero sin embargo, si se intenta abrir uno de estos archivos aparece un mensaje de error ya que en este código no tienen implementadas las funciones de open() y close().

![alt text](<img/Pruebas drivers/drv2/drv2 11.png>)

### Drv3.c

Compilamos sin problemas el driver 3, se obtiene su información y se agrega al kernel.

![alt text](<img/Pruebas drivers/drv3/drv3 1.png>)

![alt text](<img/Pruebas drivers/drv3/drv3 2.png>)

![alt text](<img/Pruebas drivers/drv3/drv3 3.png>)

Se verifica su correcto agregado por el mensaje en su `module_init()`.

![alt text](<img/Pruebas drivers/drv3/drv3 4.png>)

Hasta ahora todo se comporta como los drivers anteriores pero tiene una gran diferencia y es que este código define operaciones básicas de dispositivo como abrir, cerrar, leer y escribir, imprimiendo mensajes en el registro del kernel cuando se realizan estas operaciones. Todas estas definidas dentro de `file_operations` como se muestra a continuación y en el constructor drv3_init se crea el puntero a un objeto de la clase device particular mediante: `cl = class_create(THIS_MODULE, “chardrv”)`.

![alt text](<img/Pruebas drivers/drv3/drv3 5.png>)

- `.owner= THIS_MODULE`: Es un puntero al módulo del kernel que contiene estas operaciones. Mantiene una referencia al módulo para evitar que se descargue mientras alguna de estas operaciones está en curso.

- `open= my_open`: Esta función se llama cuando un proceso abre el archivo de dispositivo. En este caso, imprime un mensaje en el registro del kernel indicando que el archivo de dispositivo ha sido abierto.

- `release = my_close`: Esta función se llama cuando un proceso cierra el archivo de dispositivo. Este también imprime un mensaje en el registro del kernel indicando que el archivo de dispositivo ha sido cerrado.

- `read = my_read`: Esta función se llama cuando un proceso intenta leer desde el archivo de dispositivo. Es responsable de transferir datos desde el kernel al espacio de usuario. También  imprime un mensaje indicando que se ha realizado una operación de lectura. Aunque no transfiere datos ya que  la implementación real debería copiar datos desde el dispositivo al búfer del usuario.

- `write = my_write`: Esta función se llama cuando un proceso intenta escribir en el archivo de dispositivo. Es responsable de transferir datos desde el espacio de usuario al kernel. En el código, imprime un mensaje indicando que se ha realizado una operación de escritura y devuelve el número de bytes escritos (que es len, el tamaño de los datos proporcionados por el usuario). 

En las carpeta `/sys/class/chardrv/SdeC_drv3` el kernel coloca información del CDD y se tiene una carpeta `/sys/devices/virtual/chardrv/` donde están los dispositivos relacionados.

![alt text](<img/Pruebas drivers/drv3/drv3 6.png>)

El character device driver creado `SdeC_drv3` se encuentra en la carpeta `dev`.

![alt text](<img/Pruebas drivers/drv3/drv3 7.png>)

Con sudo cat /dev/SdeC_drv3 intentamos abrir el archivo, y con dmesg vemos que se cargaron las operaciones open(), read() y close():

![alt text](<img/Pruebas drivers/drv3/drv3 8.png>)

![alt text](<img/Pruebas drivers/drv3/drv3 9.png>)

Quitando el módulo con `sudo rmmod drv3.ko` , vemos que se imprime el mensaje del destructor:

![alt text](<img/Pruebas drivers/drv3/drv3 10.png>)

### Drv4.c

Se define una variable global char c que se utiliza para almacenar un único carácter, esto no está presente en drv3. A diferencia de drv3, en este caso si se realizan operaciones de escritura y lectura, mediante las funciones `my_read` que lee el valor del carácter y lo copia al espacio de usuario utilizando copy_to_user. Si la lectura es exitosa, devuelve 1 y actualiza el offset; de lo contrario, devuelve un error. 
Por otro lado, la función `my_write` toma el último byte del buffer del usuario y lo almacena en c utilizando copy_from_user. Si la escritura es exitosa, devuelve la longitud del búfer; de lo contrario, devuelve un error.

Algunas de funciones que se ejecutan dentro de la inicialización del módulo son:

`int alloc_chrdev_region(dev_t * dev, unsigned baseminor, unsigned count, const char * name);`

Esta se encarga de registrar un rango de números (menores) para dispositivos de caracteres. Parámetros que la función requiere:

- `dev`: Guarda el número major en la variable first de la cual se pasa su dirección de memoria para ser seteada dentro del cuerpo de la función.

- `baseminor`: Guarda el primero del rango de valores menores. En nuestro caso 0.

- `count`: La cantidad de números menores requeridas. Para nuestro caso solo 1.

- `name`: Nombre del device driver. En nuestro caso `SdeC_drv4`.

`struct class* class_create (struct module* owner, const char* name);`

Crea una estructura que sirve de argumento para otra función llamada `device_create()`. Recibe como argumentos:

- `owner`: Un puntero al módulo que posee esta estructura. En este caso es el mismo módulo que estamos trabajando.

- `name`: Un nombre representativo para el nombre de esta estructura.

`int cdev_add (struct cdev* p, dev_t dev, unsigned count);`

Agrega un dispositivo de caracteres al sistema. Recibe como parámetros:

- `p`: Estructura retornada por el llamado a la función cdev_init .

- `dev`: Número de device obtenido de alloc_chrdev_region.

- `count`: Cantidad de números menores para este dispositivo. En nuestro caso es solo uno.

Compilamos con make como en los casos anteriores y con `modinfo` verificamos su información general.

![alt text](<img/Pruebas drivers/drv4/drv4 1.png>)

![alt text](<img/Pruebas drivers/drv4/drv4 2.png>)

Se agrega el módulo al kernel y se verifica su instalación

![alt text](<img/Pruebas drivers/drv4/drv4 3.png>)

![alt text](<img/Pruebas drivers/drv4/drv4 4.png>)

Por último, se escribe en el archivo del device driver mediante echo y se verifica con cat.

![alt text](<img/Pruebas drivers/drv4/drv4 5.png>)

![alt text](<img/Pruebas drivers/drv4/drv4 6.png>)

### Clipboard.ko

Este módulo de kernel, a diferencia del `drv4`, está diseñado para proporcionar una funcionalidad de portapapeles accesible a través del sistema de archivos `/proc`. Este portapapeles permite a las aplicaciones de espacio de usuario leer y escribir datos en un buffer asignado dinámicamente en el espacio de kernel como se comprobará más adelante.
Cuando se carga el módulo, se reserva un espacio en memoria para el buffer del portapapeles utilizando `vmalloc` y se inicializa a ceros. Además, se crea una entrada en `/proc` llamada `clipboard` con permisos de lectura y escritura `(0666)`. Las operaciones de lectura y escritura están definidas en las funciones `clipboard_read` y `clipboard_write`.

![alt text](<img/Pruebas drivers/clip/clip 1.png>)

`struct proc_dir_entry *proc_create (const char *name, umode_t mode, struct
proc_dir_entry *parent, const struct file_operations *proc_fops)`

Tiene el propósito de crear una entrada en el directorio proc . Recibe los parámetros:

- `name`: Nombre para la nueva entrada en `/proc`. `Clipboard` en nuestro caso.

- `mode`: Permisos de acceso. `0666` en nuestro caso. Lo que se traduce en permisos de lectura y escritura para usuario, grupo y otros.

- `parent`: Nombre del directorio padre de la nueva entrada dentro de `/proc`.

- `proc_fops`: Estructura que contiene punteros a función que se implementan en el `driver`. Es el reemplazo de la estructura deprecada para versiones más viejas del kernel 

- `file_operations`: En nuestro caso definimos `clipboard_read` y `clipboard_wr`.

![alt text](<img/Pruebas drivers/clip/clip 2.png>)

Se compila y se carga el módulo, esto se verifica mediante sudo `dmesg`.

![alt text](<img/Pruebas drivers/clip/clip 3.png>)

![alt text](<img/Pruebas drivers/clip/clip 4.png>)

Se transfiere información desde el espacio de usuario al espacio del kernel creando una entrada en `/proc/clipboard` con `echo “mensaje” > /proc/clipboard`.  Mediante `cat` se puede recuperar ese mensaje.

![alt text](<img/Pruebas drivers/clip/clip 5.png>)

Cuando el módulo se descarga, se libera el espacio en memoria reservado para el buffer y se elimina la entrada en `/proc`.

![alt text](<img/Pruebas drivers/clip/clip 6.png>)

## Implementación en Raspberry Pi emulado en Qemu

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
