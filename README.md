# ProyectoPython2
Proyecto que forma parte de la evaluación de mi curso de capacitación. Este proyecto es una aplicación de línea de comandos en Python que permite gestionar una agenda de tareas. Puedes agregar, modificar, mostrar, marcar como completadas y eliminar tareas. Las tareas se almacenan en una base de datos PostgreSQL para persistencia de datos.

Características:
1. Agregar tareas: Permite agregar nuevas tareas con una descripción, fecha de entrega, hora, prioridad, categoría y agenda.

2. Mostrar tareas: Muestra todas las tareas pendientes y completadas, incluyendo detalles como prioridad, categoría y datos específicos (materia, supervisor, lugar).

3. Modificar tareas: Permite editar la descripción, fecha de entrega, hora, prioridad y categoría de una tarea existente. También permite actualizar el dato específico de la categoría (materia, supervisor, lugar).

4. Marcar como completada: Cambia el estado de una tarea a "completada".

5. Eliminar tareas: Elimina una tarea de la agenda.

6. Persistencia de datos: Las tareas se almacenan en una base de datos PostgreSQL para que no se pierdan al cerrar el programa.

7. Categorías y subtipos: Las tareas pueden clasificarse en categorías (Escuela, Trabajo, Casa) y tienen datos específicos según la categoría (materia, supervisor, lugar).

8. Prioridades: Las tareas pueden tener una prioridad (Alta, Media, Baja).

Requisitos:
1. Python 3.12.9 instalado en tu sistema.
2. PostgreSQL instalado y configurado.
3. Librerías necesarias:
  3.1 psycopg2: Para conectarse a PostgreSQL.
  3.2 Instálala con: pip install psycopg2.
  3.3 Ó crear el entorno virtual en anaconda o miniconda.

Instalación:
1. Clona este repositorio o descarga el archivo agenda.py
2. Asegurate de tener Python instalado. Puedes verificar la instalacion ejecutando:
  python --version
3. Crea una base de datos en PostgreSQL llamada agenda con el script sql que esta en la documentacion de la base de datos e haz los ultimos insert's para que funcione.
4. Navega al directorio donde se encuentran los archivos del proyecto.

Uso:
1. Ejecuta el programa desde la terminal:
  python main.py
2. Sigue las instrucciones en pantalla para interactuar con la agenda de tareas.

Menú de opciones:
1. Agregar tarea: Ingresa la descripción, fecha de entrega, hora, prioridad, categoría y agenda. Si la categoría es "Escuela", "Trabajo" o "Casa", se solicitará el dato específico (materia, supervisor, lugar).
2. Mostrar tareas: Muestra todas las tareas registradas, incluyendo detalles como prioridad, categoría y datos específicos.
3. Modificar tarea: Ingresa el ID de la tarea para modificar su descripción, fecha de entrega, hora, prioridad y categoría. También permite actualizar el dato específico de la categoría (materia, supervisor, lugar).
4. Marcar tarea como completada: Ingresa el ID de tarea para marcarla como completada.
5. Eliminar tarea: Ingresa el ID de una tarea para eliminarla de la agenda.
6. Salir: Cierra el programa.

Estructura del proyecto por ahora:
1. main.py: Punto de entrada del programa. 
2. agenda.py: Lógica de la agenda y gestión de tareas.
3. database.py: Conexión y operaciones con la base de datos.
4. tarea.py: Clase que representa una tarea.
5. conexión.py: Configuración de la conexión a PostgreSQL.
6. validaciones.py: Funciones para validar entradas del usuario.
7. menu.py: Muestra el menú de opciones.

Ejemplos de uso:
1. Agregar una tarea de Escuela:
Ingrese la descripción de la tarea: Hacer tarea de matemáticas
Ingrese la fecha de la tarea (YYYY-MM-DD): 2023-10-10
Ingrese la hora de la tarea (HH:MM): 14:00
Ingrese el ID de la prioridad (1. ALTA, 2. MEDIA, 3. BAJA): 1
Ingrese el ID de la categoría (1. ESCUELA, 2. TRABAJO, 3. CASA): 1
Ingrese la materia de la tarea: Matemáticas
Tarea agregada con éxito. ID: 1

2. Modificar una Tarea:
Ingrese el ID de la tarea a modificar: 1
Nueva descripción: Estudiar para el examen de matemáticas
Nueva fecha (YYYY-MM-DD): 2023-10-11
Nueva hora (HH:MM): 15:00
Nuevo ID de prioridad (1. ALTA, 2. MEDIA, 3. BAJA): 2
Nuevo ID de categoría (1. ESCUELA, 2. TRABAJO, 3. CASA): 1
Ingrese la nueva materia de la tarea: Física
Tarea modificada con éxito.

3. Marcar una Tarea como completada:
ID de la tarea a completar: 1
Tarea marcada como completada.

4. Eliminar una tarea:
ID de la tarea a eliminar: 1
Tarea eliminada con éxito.


Licencia:
Este proyecto esta bajo la licencia GNU.
