# TP #0 Creación y actualización de repositorios - Sistemas de Computación

## Desarrollo

### Creación y actualizacipon de repositorios

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

### Historial de cambios

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

### Deshacer cambios

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

### Ramas