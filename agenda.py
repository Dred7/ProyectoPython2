import psycopg2
from database import Database
from tarea import Tarea

# Clase Agenda para gestionar tareas
class Agenda:
    def __init__(self):
        self.db = Database()  # Instancia de la base de datos
        self.conn = self.db.conn  # Obtener la conexión desde Database
        self.cur = self.conn.cursor()  # Crear el cursor para ejecutar queries

    def agregar_tarea(self, descripcion, fechaEntrega, horaEntrega, idPrioridad, idCategoria, idAgenda):
        # Agrega una nueva tarea a la base de datos
        query = '''
        INSERT INTO tarea (descripcion, fechaEntrega, horaEntrega, completada, idPrioridad, idCategoria, idAgenda)
        VALUES (%s, %s, %s, 'P', %s, %s, %s)
        RETURNING idTarea;
        '''
        try:
            self.cur.execute(query, (descripcion, fechaEntrega, horaEntrega, idPrioridad, idCategoria, idAgenda))
            idTarea = self.cur.fetchone()[0]
            # Dependiendo del tipo de categoría, insertar en la tabla correspondiente
            if idCategoria == 1:  # Escuela
                materia = input("Ingrese la materia de la tarea: ")
                self.cur.execute("INSERT INTO escuela (idCategoria, materia) VALUES (%s, %s);", (idCategoria, materia))

            elif idCategoria == 2:  # Trabajo
                supervisor = input("Ingrese el nombre del supervisor: ")
                self.cur.execute("INSERT INTO trabajo (idCategoria, supervisor) VALUES (%s, %s);", (idCategoria, supervisor))

            elif idCategoria == 3:  # Casa
                lugar = input("Ingrese el lugar donde se realizará la tarea: ")
                self.cur.execute("INSERT INTO casa (idCategoria, lugar) VALUES (%s, %s);", (idCategoria, lugar))

            self.conn.commit()
            print(f"Tarea agregada con éxito. ID: {idTarea}")
        except psycopg2.Error as e:
            print(f"Error al agregar tarea: {e}")
            self.conn.rollback()

    def mostrar_tareas(self):
        # Muestra todas las tareas registradas en la base de datos
        query = '''
        SELECT t.idTarea, t.descripcion, t.fechaEntrega, t.horaEntrega, t.completada,
            p.nombre AS prioridad, c.nombre AS categoria, a.anio AS agenda,
            COALESCE(
                (SELECT e.materia FROM escuela e WHERE e.idCategoria = t.idCategoria LIMIT 1),
                (SELECT tr.supervisor FROM trabajo tr WHERE tr.idCategoria = t.idCategoria LIMIT 1),
                (SELECT ca.lugar FROM casa ca WHERE ca.idCategoria = t.idCategoria LIMIT 1)
            ) AS dato_especifico
        FROM tarea t
        JOIN prioridad p ON t.idPrioridad = p.idPrioridad
        JOIN categoria c ON t.idCategoria = c.idCategoria
        JOIN agenda a ON t.idAgenda = a.idAgenda;
        '''

        try:
            self.cur.execute(query)
            tareas = self.cur.fetchall()
            if not tareas:
                print("No hay tareas en la agenda.")
            else:
                print("\nLista de tareas:")
                for tarea in tareas:
                    estado = "Completada" if tarea[4] == "C" else "Pendiente"
                    print(
                        f"ID: {tarea[0]}\n"
                        f"Descripción: {tarea[1]}\n"
                        f"Fecha: {tarea[2]}\n"
                        f"Hora: {tarea[3]}\n"
                        f"Estado: {'Completada' if tarea[4] == 'C' else 'Pendiente'}\n"
                        f"Prioridad: {tarea[5]}\n"
                        f"Categoría: {tarea[6]}\n"
                        f"Agenda: {tarea[7]}\n"
                        f"Dato: {tarea[8]}\n"
                        "-----------------------------"
                    )
        except psycopg2.Error as e:
            print(f"Error al obtener tareas: {e}")

    def modificar_tarea(self, idTarea, nueva_descripcion, nueva_fecha, nueva_hora, nueva_prioridad, nueva_categoria):
        # Modifica una tarea existente
        try:
            # Obtener la categoría actual de la tarea
            self.cur.execute("SELECT idCategoria FROM tarea WHERE idTarea = %s;", (idTarea,))
            resultado = self.cur.fetchone()
        
            if not resultado:
                print("Error: No se encontró la tarea con el ID especificado.")
                return
        
            categoria_anterior = resultado[0]

            # Actualizar la tarea en la tabla principal
            query = '''
            UPDATE tarea
            SET descripcion = %s, fechaEntrega = %s, horaEntrega = %s, 
                idPrioridad = %s, idCategoria = %s
            WHERE idTarea = %s;
            '''
            self.cur.execute(query, (nueva_descripcion, nueva_fecha, nueva_hora, nueva_prioridad, nueva_categoria, idTarea))

            # Si la categoría ha cambiado, eliminar la entrada anterior y agregar una nueva
            if nueva_categoria != categoria_anterior:
                # Eliminar datos de la categoría anterior
                if categoria_anterior == 1:  # Escuela
                    self.cur.execute("DELETE FROM escuela WHERE idCategoria = %s;", (categoria_anterior,))
                elif categoria_anterior == 2:  # Trabajo
                    self.cur.execute("DELETE FROM trabajo WHERE idCategoria = %s;", (categoria_anterior,))
                elif categoria_anterior == 3:  # Casa
                    self.cur.execute("DELETE FROM casa WHERE idCategoria = %s;", (categoria_anterior,))

                 # Insertar nueva entrada según la nueva categoría
                if nueva_categoria == 1:  # Escuela
                    materia = input("Ingrese la materia de la tarea: ")
                    self.cur.execute("DELETE FROM escuela WHERE idCategoria = %s;", (nueva_categoria,))
                    self.cur.execute("INSERT INTO escuela (idCategoria, materia) VALUES (%s, %s);", (nueva_categoria, materia))
                elif nueva_categoria == 2:  # Trabajo
                    supervisor = input("Ingrese el nombre del supervisor: ")
                    self.cur.execute("DELETE FROM trabajo WHERE idCategoria = %s;", (nueva_categoria,))
                    self.cur.execute("INSERT INTO trabajo (idCategoria, supervisor) VALUES (%s, %s);", (nueva_categoria, supervisor))
                elif nueva_categoria == 3:  # Casa
                    lugar = input("Ingrese el lugar donde se realizará la tarea: ")
                    self.cur.execute("DELETE FROM casa WHERE idCategoria = %s;", (nueva_categoria,))
                    self.cur.execute("INSERT INTO casa (idCategoria, lugar) VALUES (%s, %s);", (nueva_categoria, lugar))

            # Confirmar cambios en la base de datos
            self.conn.commit()
            print("Tarea modificada con éxito.")

        except psycopg2.Error as e:
            print(f"Error al modificar tarea: {e}")
            self.conn.rollback()

    def marcar_completada(self, idTarea):
        # Marca una tarea como completada
        query = '''
        UPDATE tarea
        SET completada = 'C'
        WHERE idTarea = %s;
        '''
        try:
            self.cur.execute(query, (idTarea,))
            self.conn.commit()
            print("Tarea marcada como completada.")
        except psycopg2.Error as e:
            print(f"Error al completar tarea: {e}")
            self.conn.rollback()

    def eliminar_tarea(self, idTarea):
        # Elimina una tarea de la base de datos
        query = '''
        DELETE FROM tarea
        WHERE idTarea = %s;
        '''
        try:
            self.cur.execute(query, (idTarea,))
            self.conn.commit()
            print("Tarea eliminada con éxito.")
        except psycopg2.Error as e:
            print(f"Error al eliminar tarea: {e}")
            self.conn.rollback()

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos 
        self.db.cerrar_conexion()