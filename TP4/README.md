# TP #4 Módulos de kernel - Sistemas de Computación

## Introducción

En los kernels de Linux, los módulos son piezas de código que se pueden cargar dinámicamente en el núcleo del sistema operativo. Estos módulos amplían la funcionalidad del kernel sin necesidad de recompilarlo o reiniciar el sistema.

Estos permiten añadir nuevas características, controladores de dispositivos o sistemas de archivos al kernel en tiempo de ejecución sin modificar el código fuente del kernel base. Se cargan en la memoria solo cuando son necesarios, lo que permite un uso más eficiente de los recursos del sistema. Los usuarios pueden cargar y descargar módulos según sea necesario, lo que permite una configuración más flexible del sistema. Al separar el código en módulos, se facilita el mantenimiento y la actualización del kernel, ya que no es necesario recompilar todo el kernel para hacer cambios en un módulo específico. Además, los módulos facilitan la depuración y el desarrollo de nuevas características del kernel, ya que los cambios pued