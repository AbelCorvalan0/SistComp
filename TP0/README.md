# TP #0 Creación y actualización de repositorios - Sistemas de Computación

## Desarrollo

Link del repositorio [libro-git](https://github.com/AbelCorvalan0/libro-git)

### Uso de Git

#### Creación y actualizacipon de repositorios

- Ejercicio 1

Configurar Git definiendo el nombre del usuario, el correo electrónico y activar el coloreado de la salida. Mostrar la configuración final.

![alt text](<img/Creación y actualización de repositorios/ejercicio 1.png>)

- Ejercicio 2

Crear un repositorio nuevo con el nombre `libro` y mostrar su contenido.

![alt text](<img/Creación y actualización de repositorios/ejercicio 2.png>)

- Ejercicio 3

    1. Comprobar el estado del repositorio.
    2. Crear fichero `indice.txt` con el siguiente contenido.

        ```sh
            Capítulo 1: Introducción a Git
            Capítulo 2: Flujo de trabajo básico
            Capítulo 3: Repositorios remotos
        ```
    3. Comprobar el nuevo el estado del repositorio.
    4. Añadir el fichero a la zona del intercambio temporal.
    5. Volver a comprobar una vez más el estado del repositorio.

- Ejercicio 4

Realizar un commit de los últimos cambios con el mensaje “Añadido índice del libro.” y ver el estado del repositorio.

- Ejercicio 5

    1. Cambiar el fichero `indice.txt` para que contenga lo siguiente:

        ```sh
        Capítulo 1: Introducción a Git
        Capítulo 2: Flujo de trabajo básico
        Capítulo 3: Gestión de ramas
        Capítulo 4: Repositorios remotos
        ```
    2. Mostrar los cambios con respecto a la última versión guardada en el repositorio.
    3. Hacer un commit de los cambios con el mensaje “Añadido capítulo 3 sobre gestión de ramas”.

![alt text](<img/Creación y actualización de repositorios/ejercicio 5.png>)

- Ejercicio 6

    1. Mostrar los cambios de la última versión del repositorio con respecto a la anterior.
    2. Cambiar el mensaje del último commit por “Añadido capítulo 3 sobre gestión de ramas al índice.”
    3. Volver a mostrar los últimos cambios del repositorio.

![alt text](<img/Creación y actualización de repositorios/ejercicio 6.png>)

#### Historial de cambios

- Ejercicio 1

    1. Mostrar el historial de cambios del repositorio.
    2. Crear la carpeta `capitulos` y crear dentro de ella el fichero `capitulo.txt` con el siguiente texto.

    ```sh
        Git es un sistema de control de versiones ideados por Linus Torvalds.
    ```

    3. Añadir los cambios a la zona de intercambio temporal.
    4. Hacer un commit de los cambios con el mensaje “Añadido capítulo 1.”
    5. Volver a mostrar el historial de cambios del repositorio.

![alt text](<img/Historial de cambios/ejercicio 1.png>)

- Ejercicio 2

    1. Crear el fichero `caoitulo2.txt` en la carpeta `capitulos` con el siguiente texto.

    ```sh
        El flujo de trabajo básico con Git consiste en: 1- Hacer cambios en el repositorio. 2- Añadir los cambios a la zona de intercambio temporal. 3- Hacer un commit de los cambios. 
    ```
    2. Añadir los cambios a la zona de intercambio temporal.
    3. Hacer un commit de los cambios con el mensaje "Añadido capítulo 2."
    4. Mostrar las diferencias entre la última versión y dos versiones anteriores.

![alt text](<img/Historial de cambios/ejercicio 2.png>)

- Ejercicio 3

    1. Crear el fichero `capitulo.txt` en la carpeta `capitulos` con el siguiente texto.

    ```sh
        Git permite la creación de ramas lo que permite tener distintas versiones del mismo proyecto y trabajar de manera simultanea en ellas.   
    ```
    2. Añadir los cambios a la zona de intercambio temporal.
    3. Hacer un commit de los cambios con el mensaje “Añadido capítulo 3.”
    4. Mostrar las diferencias entre la primera y la última versión del repositorio.

![alt text](<img/Historial de cambios/ejercicio 3.png>)

![alt text](<img/Historial de cambios/ejercicio 3.png>)

![alt text](<img/Historial de cambios/ejercicio 3a.png>)

- Ejercicio 4

    1. Añadir al final del fichero `indice.txt` la siguiente línea:

    ```sh
        Capítulo 5:Conceptoos avanzados
    ```
    2. Añadir los cambios a la zona de intercambio temporal.
    3. Hacer un commit de los cambios con el mensaje “Añadido capítulo 5 al índice.”.
    4. Mostrar quién ha hecho cambios sobre el fichero `indice.txt`.

![alt text](<img/Historial de cambios/ejercicio 4.png>)

#### Deshacer cambios

- Ejercicio 1

    1. Eliminar la última línea del fichero `indice.txt` y guardarlo.
    2. Comprobar el estado del repositorio.
    3. Deshacer los cambios realizados en el fichero `indice.txt` para volver a la versión anterior del fichero.
    4. Volver a comprobar el estado del repositorio.

![alt text](<img/Deshacer cambios/ejercicio 1.png>)

![alt text](<img/Deshacer cambios/ejercicio 1a.png>)

- Ejercicio 2

    1. Eliminar la última línea del fichero `indice.txt` y guardarlo.
    2. Añadir los cambios a la zona de intercambio temporal.
    3. Comprobar de nuevo el estado del repositorio.
    4. Quitar los cambios de la zona de intercambio temporal, pero mantenerlos en el directorio de trabajo.
    5. Comprobar de nuevo el estado del repositorio. pero mantenerlos en el directorio de trabajo.
    6. Deshacer los cambios realizados en el fichero `indice.txt` para volver a la versión anterior del fichero.
    7. Volver a comprobar el estado del repositorio.

![alt text](<img/Deshacer cambios/ejercicio 2.png>)

- Ejercicio 3

    1. Eliminar la última línea del fichero indice.txt y guardarlo.
    2. Eliminar el fichero capitulos/capitulo3.txt.
    3. Añadir un fichero nuevo captitulos/capitulo4.txt vacío.
    4. Añadir los cambios a la zona de intercambio temporal.
    5. Comprobar de nuevo el estado del repositorio.
    6. Quitar los cambios de la zona de intercambio temporal, pero mantenerlos en el directorio de trabajo.
    7. Comprobar de nuevo el estado del repositorio.
    8. Deshacer los cambios realizados para volver a la versión del repositorio.
    9. Volver a comprobar el estado del repositorio.

![alt text](<img/Deshacer cambios/ejercicio 3.png>)

![alt text](<img/Deshacer cambios/ejercicio 3a.png>)

- Ejercicio 4

    1. Eliminar la última línea del fichero indice.txt y guardarlo.
    2. Eliminar el fichero capitulos/capitulo3.txt.
    3. Añadir los cambios a la zona de intercambio temporal y hacer un commit con el mensaje “Borrado accidental.”
    4. Comprobar el historial del repositorio.
    5. Deshacer el último commit pero mantener los cambios anteriores en el directorio de trabajo y la zona de intercambio temporal.
    6. Comprobar el historial y el estado del repositorio.
    7. Volver a hacer el commit con el mismo mensaje de antes.
    8. Deshacer el último commit y los cambios anteriores del directorio de trabajo volviendo a la versión anterior del repositorio.
    9. Comprobar de nuevo el historial y el estado del repositorio.

![alt text](<img/Deshacer cambios/ejercicio 4.png>)

![alt text](<img/Deshacer cambios/ejercicio 4a.png>)

![alt text](<img/Deshacer cambios/ejercicio 4b.png>)

![alt text](<img/Deshacer cambios/ejercicio 4c.png>)

![alt text](<img/Deshacer cambios/ejercicio 4d.png>)

![alt text](<img/Deshacer cambios/ejercicio 4e.png>)

![alt text](<img/Deshacer cambios/ejercicio 4f.png>)

#### Ramas

- Ejercicio 1

Crear una nueva rama `bibliografia` y mostrar las ramas del repositorio.

![alt text](<img/Ramas/ejercicio 1.png>)

- Ejercicio 2

    1. Crear una nueva rama `capitulos/capitulo4.txt` y añadir el texto siguiente

    ```sh
        En este capítulo veremos cómo usar GitHub para alojar repositorios en remoto.
    ```

    2. Añadir los cambios a la zona de intercambio temporal.
    3. Hacer un commit con el mensaje "Añadido capítulo 4."
    4. Mostrar la historia del repositorio incluyendo todas las ramas.

![alt text](<img/Ramas/ejercicio 2.png>)

- Ejercicio 3

    1. Cambiar a la rama bibliografia.
    2. Crear el fichero bibliografia.txt y añadir la siguiente referencia.

    ```sh
        Chacon, S. and Straub, B. Pro Git. Apress.
    ```

    3. Añadir los cambios a la zona de intercambio temporal.
    4. Hacer un commit con el mensaje “Añadida primera referencia bibliográfica.”
    5. Mostrar la historia del repositorio incluyendo todas las ramas.

![alt text](<img/Ramas/ejercicio 3.png>)

- Ejercicio 4

    1. Fusionar la rama `bibliografia` con la rama `master`.
    2. Mostrar la historia del repositorio incluyendo todas las ramas.
    3. Eliminar la rama `bibliografia`.
    4. Mostrar de nuevo la historia del repositorio incluyendo todas las ramas.

![alt text](<img/Ramas/ejercicio 4.png>)

![alt text](<img/Ramas/ejercicio 4a.png>)

- Ejercicio 5

    1. Crear la rama bibliografia.
    2. Cambiar a la rama bibliografia.
    3. Cambiar el fichero bibliografia.txt para que contenga las siguientes referencias:

    ```sh
        Scott Chacon and Ben Straub. Pro Git. Apress.
        Ryan Hodson. Ry’s Git Tutorial. Smashwords (2014)
    ```

    4. Añadir los cambios a la zona de intercambio temporal y hacer un commit con el mensaje “Añadida nueva referencia bibliográfica.”
    5. Cambiar a la rama master.
    6. Cambiar el fichero bibliografia.txt para que contenga las siguientes referencias:

    ```sh
        Chacon, S. and Straub, B. Pro Git. Apress.
        Loeliger, J. and McCullough, M. Version control with Git. O’Reilly.
    ```

    7. Añadir los cambios a la zona de intercambio temporal y hacer un commit con el mensaje “Añadida nueva referencia bibliográfica.”
    8. Fusionar la rama bibliografia con la rama master.
    9. Resolver el conflicto dejando el fichero bibliografia.txt con las referencias:

    ```sh
        Chacon, S. and Straub, B. Pro Git. Apress.
        Loeliger, J. and McCullough, M. Version control with Git. O’Reilly.
        Hodson, R. Ry’s Git Tutorial. Smashwords (2014)
    ```

    10. Añadir los cambios a la zona de intercambio temporal y hacer un commit con el mensaje “Resuelto conflicto de bibliografía.”
    11. Mostrar la historia del repositorio incluyendo todas las ramas.

![alt text](<img/Ramas/ejercicio 5.png>)

![alt text](<img/Ramas/ejercicio 5a.png>)

![alt text](<img/Ramas/ejercicio 5b.png>)

#### Repositorios remotos

- Ejercicio 1

    1. Crear un nuevo repositorio público en GitHub con el nombre libro-git.
    2. Añadirlo al repositorio local del libro.
    3. Mostrar todos los repositorios remotos configurados.

![alt text](<img/Repositorios remotos/ejercicio 1.png>)

- Ejercicio 2

    1. Añadir los cambios del repositorio local al repositorio remoto de GitHub.
    2. Acceder a GitHub y comprobar que se han subido los cambios mostrando el historial de versiones.

![alt text](<img/Repositorios remotos/ejercicio 2.png>)

- Ejercicio 3

    1. Colaborar en el repositorio remoto libro-git de otro usuario.
    2. Clonar su repositorio libro-git.
    3. Añadir el fichero autores.txt que contenga el nombre del 4. usuario y su correo electrónico.
    4. Añadir los cambios a la zona de intercambio temporal.
    5. Hacer un commit con el mensaje “Añadido autor.”
    6. Subir los cambios al repositorio remoto.

![alt text](<img/Repositorios remotos/ejercicio 3.png>)

![alt text](<img/Repositorios remotos/ejercicio 3a.png>)

- Ejercicio 4

    1. Hacer una bifurcación del repositorio remoto asalber/libro-git en GitHub.
    2. Clonar el repositorio creado en la cuenta de GitHub del usuario.
    3. Crear una nueva rama autoria y activarla.
    4. Añadir el nombre del usuario y su correo al fichero autores.txt.
    5. Añadir los cambios a la zona de intercambio temporal.
    6. Hacer un commit con el mensaje “Añadido nuevo autor.”
    7. Subir los cambios de la rama autoria al repositorio remoto en GitHub.
    8. Hacer un Pull Request de los cambios en la rama autoria.

![alt text](<img/Repositorios remotos/ejercicio 4.png>)

### Herramientas de consolas

Se revisan las siguientes habilidades básicas de Linux:

- Navegación por comandos. 
- Administración de archivos.
- Expresiones regulares y la administración del sistema. 

#### Parte 1: Exploración de sintaxis de comandos.

Se implementan los comandos `ls`, `pwd`, `cd` y `sudo` para revisar la navegación básica de sintaxis de comandos.

- Paso 1: Abrir una terminal.

Se abre un terminal con el shortcut `Ctrl + Alt + T`.

- Paso 2: Navegar por los directorios.

    a. Utilizar el comando ls para mostrar el directorio actual. Estos comandos distinguen entre mayúsculas y
    minúsculas.
    
    ![alt text](<img/Herramientas de consolas/2a.png>)
    
    b. Utilice el comando ls con el argumento "nombre de un archivo" para mostrar el contenido de la carpeta.

    ![alt text](<img/Herramientas de consolas/2b.png>)
    
    c. Utilice el comando ls con la opción -l para mostrar una "visualización larga" del contenido del directorio
    actual.
    
    ![alt text](<img/Herramientas de consolas/2c.png>)

    d. Utilice el comando ls con la opción -r para mostrar el contenido del directorio actual en orden alfabético
    inverso.

    ![alt text](<img/Herramientas de consolas/2d.png>)

    e. Se pueden utilizar varias opciones al mismo tiempo. Utilice el comando ls con las opciones -l y -r para
    mostrar el contenido del directorio actual tanto en orden largo como inverso.

    ![alt text](<img/Herramientas de consolas/2e.png>)
    
    f. Hay muchas más opciones que se pueden usar con el comando ls. Utilice el comando man con el argumento ls para ver todas las posibilidades en el manual. El comando man se puede usar para buscar cualquier comando dentro del sistema. Utilice la barra espaciadora para avanzar a pantallas posteriores. Presione q para salir.

    ![alt text](<img/Herramientas de consolas/2f.png>)

    g. También puede usar el argumento —help después de la mayoría de los comandos para ver un resumen más corto de todas las opciones de comando disponibles.

    ![alt text](<img/Herramientas de consolas/2g.png>)

    h. Use el comando pwd para desplegar el directorio actual con el que se está trabajando.

    ![alt text](<img/Herramientas de consolas/2h.png>)

    i. Utilice el comando cd para cambiar el directorio a /home/abel/documents.

    ![alt text](<img/Herramientas de consolas/2i.png>)

    j. Utilice el comando cd con el símbolo / para cambiar los directorios al directorio raíz. Utilice pwd de nuevo
    para ver que ahora está en el directorio raíz.

    ![alt text](<img/Herramientas de consolas/2j.png>)

    k. Vuelva al directorio /home/abel/documents. Consejo: Puede mover un directorio a la vez o todo el camino a un destino. Para ingresar rápidamente el comando, escriba las primeras letras del nombre del directorio y presione Tab para que el sistema introduzca automáticamente el resto del nombre. Recuerde que los nombres distinguen entre letras mayúsculas y minúsculas.

    ![alt text](<img/Herramientas de consolas/2k.png>)

    l. Use los caracteres .. para subir un solo directorio. Utilice pwd de nuevo para ver que está de vuelta en el
    directorio de inicio del usuario.

    ![alt text](<img/Herramientas de consolas/2l.png>)

- Parte 3: Utilizar comandos de superusuario para el acceso adminisitrativo.

    a. Utilice el comando sudo para emitir un solo comando como usuario root (raíz). No se creará una nueva terminal. Utilice el comando sudo apt-get update para actualizar la lista de paquetes disponibles instalados en la máquina virtual (Virtual Machine). Este comando no funcionará si no se utiliza el comando sudo.

    ![alt text](<img/Herramientas de consolas/p3 a.png>)

#### Parte 2: Revisión de Administración de Archivos

En esta parte, revisará los permisos de archivos, cambiará los permisos y la propiedad de archivos, moverá archivos, copiará archivos, eliminará archivos y verá archivos.

- Paso 1: Revisión de permisos de archivos.

    a. Utilice ls Desktop -l para mostrar el contenido de la carpeta Escritorio.

    ![alt text](<img/Herramientas de consolas/Parte 2/parte 2 1.png>)


    b. Responda a las siguientes preguntas sobre la salida anterior. Si es necesario, busque en Internet la
    información del permiso del archivo Linux que se muestra en la salida del comando ls.

    - ¿Qué representa el guion inicial en la información de  permisos?
    Este es el campo de tipo de archivo. El guion representa un archivo normal.
    
    - ¿Qué habría en el lugar del guion si el elemento fuera un directorio?
    Sería una "d" para "directorio".

    - ¿Qué representan las tres letras o guiones siguientes en la información de permisos?
    Estos representan los permisos del propietario del archivo sobre el archivo.

    - ¿Qué representan las tres letras intermedias o guiones en la información de permisos?
    Estos representan los permisos del grupo sobre el archivo.
    
    - ¿Qué representan las tres últimas letras o guiones en la información de permisos?
    Estos representan los permisos que otros usuarios tienen sobre el archivo.

    - ¿Qué indica la primera instancia de "devasc" en la información de permiso?
    Esto indica el usuario propietario del campo y que es el propietario del archivo.

    - ¿Qué indica la segunda instancia de "devasc" en la información de permiso?
    Esto indica el campo propietario del grupo y es el grupo del archivo.

    - ¿Qué significa un tipo de permiso de "r"?
    Esto significa un permiso de "leer". Esto permite leer o copiar el contenido del archivo.

    - ¿Qué significa un tipo de permiso de "w"?
    Esto significa un permiso de "escribir". Esto permite modificar o sobrescribir el contenido. Permite agregar o eliminar archivos de un directorio.

    - ¿Qué significa un tipo de permiso de "x"?
    Esto significa un permiso de "ejecutar". Esto permite que un archivo se ejecute como un proceso, aunque los archivos de script también requieren permiso de lectura.

- Paso 2: Cambiar los permisos y la propiedad de los archivos.

    a. Utilice el comando cd para pasar a los Documentos del Directorio.

    b. Utilice el comando echo para crear un archivo de script de shell, que tendrá el comando ls../Desktop dentro del archivo. Recuerde que el carácter mayor que (>) redirige la salida del comando a un archivo.

    c. El script myfile.sh se almacena en el directorio /Documents. Utilice el comando cat para ver el único comando del script. Este archivo se utilizará como ejemplo para modificar los permisos y la propiedad.

    d. Usa el comando. /myfile.sh para ejecutar el script. Se deniega el acceso porque debe establecer el permiso del ejecutable en el archivo.

    e. Utilice el comando ls -l myfile.sh para ver los permisos de archivo actuales.

    f. Utilice el comando chmod +x myfile.sh para permitir la ejecución del archivo.

    g. Usa el comando. /myfile.sh para ejecutar el script.

    h. Utilice el comando sudo chown root myfile.sh para cambiar la propiedad del archivo a "root".

    i. Mostrar los permisos del archivo myfile.sh.

    ![alt text](<img/Herramientas de consolas/Parte 2/paso 2.png>)

- Paso 3: Utilice el comando para mover archivos.

    a. Utilice el comando mv para mover el archivo myfile.sh al escritorio.

    b. Mostrar el contenido de la carpeta Escritorio.


    c. Devuelva el archivo a la carpeta Documentos.

    d. Utilice el comando mv para cambiar el nombre de myfile.sh a myfile_renamed.sh.

    ![alt text](<img/Herramientas de consolas/Parte 2/paso 3.png>)

- Paso 4: Utilice el comando copy files (copiar archivos).
    
    a. Utilice el comando cp para hacer una copia del archivo myfile_renamed.sh.

- Paso 5: Utilice el comando para remover archivos.

Utilice el comando rm para quitar el archivo myfile_renamed_and_copied.sh.

- Paso 6: Utilice la redirección de salida estándar.

    a. Utilice la redirección (>) para colocar texto en un nuevo archivo llamado linux.txt.

    b. Utilice el comando cat para redirigir el contenido de linux.txt a otro archivo.

    c. Utilice el comando cat para ver el contenido de linux2.txt.

    d. Utilice el comando echo para anexar texto al archivo linux2.txt .

    e. Utilice el comando cat para ver el contenido del linux.txt archivo.


    f. Utilice el comando echo para sobrescribir el contenido de un archivo utilizando el corchete de ángulo único.

    g. Utilice el comando cat para ver el contenido del archivo linux.txt. Observe que el estado anterior “¡Linux es impresionante!" se sobrescribió.

    ![alt text](<img/Herramientas de consolas/Parte 2/paso 6.png>)

- Paso 7: Utilice el editor de texto vim.

    a. Utilice el siguiente comando para iniciar el editor de texto vi y abrir un archivo de texto.

    b. Utilice el editor de texto para cambiar el contenido a lo siguiente:

    La tecla insert le permitirá entrar en el modo de edición, añadiendo después de la posición del cursor, mientras que la tecla i le permitirá entrar en el modo de edición, insertando en la posición del cursor.
    Tiene que usar la tecla Esc para entrar en el modo de comando para moverse. Recuerde que d eliminará (cortará), y tirará (copiará), y p pondrá (pegará) la línea actual con el cursor.


    c. Guarde el texto en un nuevo archivo llamado "linux3.txt". Recuerde que tiene que estar en el modo de comando y escribir dos puntos ( : ) para entrar en modo ex para que pueda escribir (guardar) el documento :w linux3.txt). A continuación, puede usar el comando quit (exit) :q )para salir del editor vi.

    d. Use el comando cat para ver el contenido del archivo linux3.txt.

    ![alt text](<img/Herramientas de consolas/Parte 2/paso 7 1.png>)

    ![alt text](<img/Herramientas de consolas/Parte 2/paso 7 2.png>)

#### Parte 3: Revisión de Expresiones Regulares

En esta parte, se utiliza el comando `grep` para revisar cómo se pueden utilizar expresiones regulares para filtrar.

    a. Utilice el comando grep para filtrar el contenido del archivo passwd para mostrar la línea del archivo passwd que contiene devasc. Observe que las dos instancias de devasc están resaltadas. También observe que el comando grep distingue entre mayúsculas y minúsculas. La instancia de DEVASC no está resaltada.

    b. Utilice el comando grep para mostrar cuántas veces aparece root en el archivo passwd. Observe que las tres instancias root (raíz) están resaltadas.

    c. Utilice el comando grep con el carácter de anclaje ^ para encontrar la palabra, pero solo al principio de la línea. Observe que sólo se resalta la palabra al principio de la línea.

    d. Utilice el comando grep con el carácter de anclaje $ para encontrar una palabra al final de una línea.

    e. Utilice el comando grep con el carácter de anclaje . para que coincida con palabras de longitud específica con letras diferentes en ellas. Observe que no solo se resalta daem, sino que también se resalta dnsm.

    f. Utilice el comando grep para encontrar líneas donde solo estén presentes los números 8 o 9. Observe que sólo se devuelven las líneas que contienen un 8, un 9 o ambos.

    g. Utilice el comando grep para buscar caracteres literales. Observe que sólo se devuelven las líneas que contienen una coma.

    h. Utilice el comando grep para buscar apariciones de cero o más del patrón que lo precede. Observe que sólo se devuelven las líneas con new y ne.

![alt text](<img/Herramientas de consolas/Parte 3/parte 3.png>)

![alt text](<img/Herramientas de consolas/Parte 3/parte 3a.png>)

#### Parte 4: revisión del Sistema de Administración.

En esta parte, revise las tareas básicas de administración del sistema Linux, incluyendo el apagado del equipo, ver y probar la configuración de red, vigilar procesos, administrar paquetes de instalación, actualizar contraseñas de usuario, agregar contenido a archivos y usar editores de texto.

- Paso 1: Apague la computadora.

    a. Utilice el comando shutdown now para iniciar un apagado del sistema operativo (y la máquina virtual) inmediatamente. No tiene que realizar esta acción, ya que la máquina virtual se apagará y tendrá que reiniciarla manualmente. Los formatos de este argumento de tiempo pueden ser la palabra now, una hora del día en el formato hh:mm o el número de minutos a retrasar en el formato +minutes.

    ```sh
        shutdown now
    ```

    b. Utilice el comando date para comprobar la fecha establecida del sistema operativo.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 1.png>)

    c. Utilice el comando shutdown +1 “¡Vuelva pronto!" para apagar el sistema operativo en un minuto y mostrar el mensaje "¡Vuelva pronto!" Asegúrese de cancelar o su máquina virtual se apagará.

    ```sh
        shutdown+1 
        shutdown -c 
    ```

- Paso 2: Ver y probar la configuración de red.

    a. Utilice el comando ip address para mostrar la configuración de red. La salida es un poco más detallada. Por ejemplo, observe que se muestran cinco direcciones IPv4 para la interfaz dummy0.


    b. Utilice el comando ping con las opciones -c 4 para hacer ping a un equipo de la red local cuatro veces. Debe utilizar una dirección IP válida de un dispositivo en su red local. En el siguiente ejemplo se utiliza 192.168.1.1, pero es probable que su red tenga direcciones IPv4 diferentes.

    c. También puede hacer ping a un nombre y el Sistema de nombres de dominio (DNS) resolverá el nombre en una dirección IP. Por ejemplo, ping al sitio web de Cisco. Su máquina virtual (Virtual Machine) enviará una solicitud DNS primero para obtener la dirección IP y luego enviar los paquetes ping. El proceso DNS no se muestra en la salida ping.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 2.png>)    

- Paso 3: Ver procesos.

    a. Utilice el comando ps para mostrar los procesos que se están ejecutando en la terminal actual.

    b. Utilice el comando ps con la opción -e para mostrar todos los procesos que se ejecutan en el equipo.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 3.png>)    

    c. Puede canalizar cualquier salida de comando a una pantalla a la vez agregando | more. Se muestra una pantalla de salida con el —more— que se muestra en la parte inferior. Ahora puede usar la tecla Enter para mostrar una línea a la vez, la barra espaciadora para mostrar una pantalla a la vez o Ctrl+C para salir y volver al símbolo del sistema.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 4.png>)   
    
    d. Utilice el comando ps con la opción -ef para mostrar con más detalle todos los procesos que se ejecutan en el equipo. 

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 5.png>)

- Paso 4: Administrar paquetes.

    a. Utilice el comando apt-get update para actualizar la lista de paquetes disponibles en el sistema operativo, como se muestra anteriormente en la Parte 1 de este laboratorio. Debe utilizar permisos de nivel administrativo para utilizar este comando.

    b. Utilice el comando apt-cache search para encontrar un paquete específico.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 6.png>)

    c. Utilice el comando apt-get install para instalar un paquete.
    
    d. Ahora puede usar el comando speedtest-cli para probar su velocidad actual de conexión a Internet.

    e. Utilice el comando apt-get upgrade para actualizar todos los paquetes y dependencias del equipo.

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 6.png>)

    f. Utilice el comando apt-get purge para eliminar completamente un paquete del equipo.  

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 8.png>)

- Paso 5: Actualizar Contraseñas.

    a. Utilice el comando passwd para actualizar su contraseña.

    b. Utilice el comando passwd con la opción -S para ver el estado de su contraseña.    

    c. Utilice las páginas de manual para el comando passwd (man passwd) para investigar la opción -S y encontrar la respuesta a las siguientes preguntas.    

![alt text](<img/Herramientas de consolas/Parte 4/parte 4 9.png>)

    ¿Cuál es el estado actual de la contraseña?
    P indica una contraseña utilizable.
    
    ¿Cuál es el número mínimo de días que deben pasar antes de que se pueda cambiar la contraseña?
    0

    ¿Cuál es el número de días después de la expiración de la contraseña que la cuenta permanece activa?
    -1 indica que la contraseña nunca caduca debido a la inactividad.