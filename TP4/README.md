# TP #4 Módulos de kernel - Sistemas de Computación

## Introducción

En los kernels de Linux, los módulos son piezas de código que se pueden cargar dinámicamente en el núcleo del sistema operativo. Estos módulos amplían la funcionalidad del kernel sin necesidad de recompilarlo o reiniciar el sistema.

Estos permiten añadir nuevas características, controladores de dispositivos o sistemas de archivos al kernel en tiempo de ejecución sin modificar el código fuente del kernel base. Se cargan en la memoria solo cuando son necesarios, lo que permite un uso más eficiente de los recursos del sistema. Los usuarios pueden cargar y descargar módulos según sea necesario, lo que permite una configuración más flexible del sistema. Al separar el código en módulos, se facilita el mantenimiento y la actualización del kernel, ya que no es necesario recompilar todo el kernel para hacer cambios en un módulo específico. Además, los módulos facilitan la depuración y el desarrollo de nuevas características del kernel, ya que los cambios pueden comprobarse de forma incremental sin afectar al kernel en funcionamiento.

## Primeras tareas

El primer comando permite instalar un conjunto básico de herramientas de compilación llamado build-essential, que incluye compiladores y otros programas necesarios para compilar software desde el código fuente.
