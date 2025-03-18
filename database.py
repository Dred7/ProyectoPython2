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

    

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos
        self.cur.close()
        self.conn.close()
        print("Conexión cerrada.")