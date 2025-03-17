import psycopg2
from conexion import DATABASE_CONFIG

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(**DATABASE_CONFIG)
            self.cur = self.conn.cursor()
            print("Conexión a la base de datos exitosa.")
        except psycopg2.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            exit(1)

    def ejecutar_consulta(self, query, params=None, fetch=False):
        # Ejecuta consultas en la base de datos
        try:
            self.cur.execute(query, params or ())
            if fetch:
                return self.cur.fetchall()
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error en la consulta: {e}")
            self.conn.rollback()

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos
        self.cur.close()
        self.conn.close()
        print("Conexión cerrada.")