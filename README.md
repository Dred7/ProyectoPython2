# ProyectoPython2
Proyecto que forma parte de la evaluación de mi curso de capacitación.
Este proyecto es una aplicación de línea de comandos en Python que permite gestionar una agenda de tareas. Puedes agregar, modificar, mostrar, marcar como completadas y eliminar tareas. Las tareas se almacenan en un archivo CSV para persistencia de datos.

Características:
1. Agregar tareas: Permite agragar nuevas tareas con una descripción y una fecha de entrega.
2. Mostrar tareas: Muestra todas las tareas pendientes y completadas.
3. Modificar tareas: Permite editar la descripción y la fecha de entrega de una tarea existente.
4. Marcar como completada: Cambia el estado de una tarea a "completada".
5. Eliminar tareas: Elimnina una tarea de la agenda.
6. Persistencia de datos: Las tareas se guardan en un archivo CSV (tareas.csv) para que no se pierdan al cerrar el programa.

Requisitos:
1. Python 3.12.9 instalado en tu sistema.
2. No se requieren librerías adicionales, de momento.

Instalación:
1. Clona este repositorio o descarga el archivo agenda.py
2. Asegurate de tener Python instalado. Puedes verificar la instalacion ejecutando:
  python --version
3. Navega al directorio donde se encuentra el archivo agenda.py

Uso:
1. Ejecuta el programa desde la terminal
  python agenda.py
2. Sigue las instrucciones en pantalla para interactuar con la agenda de tareas.

Menú de opciones:
1. Agregar tarea: Ingresa la descripción y la fecha de entrega de la tarea.
2. Mostrar tareas: Muestra todas las tareas en la agenda.
3. Modificar tarea: Ingresa el número de la tarea para modificar su descripción y fecha de entrega.
4. Marcar tarea como completada: Ingresa el número de tarea para marcarla como completada.
5. Eliminar tarea: Selecciona  una tarea para eliminarla de la agenda.
6. Salir: Cierra el programa.

Estructura del proyecto por ahora:
1. agenda.py: Archivo principal del programa.
2. tareas.csv: Archivo CSV donde se almacenan las tareas (se crea automáticamente al agregar la primera tarea).

Licencia:
Este proyecto esta bajo la licencia GNU.
