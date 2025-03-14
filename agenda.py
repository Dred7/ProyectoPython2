import csv
import os

# Definino la clase Tarea
class Tarea:
    def __init__(self, descripcion, fecha, completada=False):
        #Constructor de la clase Tarea
        self.descripcion = descripcion
        self.fecha = fecha
        self.completada = completada

    def __str__(self):
        #Representamos la tarea como una cadena de texto
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} (Fecha: {self.fecha}) - {estado}"

class Agenda:
    def __init__(self, agenda_csv = "tareas.csv"):
        #Constructor de la clase Agenda
        #Lista para almacenar las tareas
        self.tareas = [] 
        self.agenda_csv = agenda_csv
        self.cargar_csv()

    def agregar_tarea(self, descripcion, fecha):
        #Metodo para agregar una tarea a la agenda
        tarea = Tarea(descripcion, fecha)
        self.tareas.append(tarea)
        print("Tarea agregada con éxito.")
        self.guardar_csv()

    def mostrar_tareas(self):
        #Metodo para mostrar todas las tareas
        if not self.tareas:
            print("No hay tareas en la agenda.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def modificar_tarea(self, indice, nueva_descripcion, nueva_fecha):
        #Metodo para modificar una tarea existente en la lista
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].descripcion = nueva_descripcion
            self.tareas[indice].fecha = nueva_fecha
            print("Tarea modificada con éxito.")
            self.guardar_csv()
        else:
            print("Índice de tarea no válido.")

    def marcar_completada(self, indice):
        #Metodo para marcar una tarea como completada
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print("Tarea marcada como completada.")
            self.guardar_csv()
        else:
            print("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        #Metodo para eliminar una tarea de la agenda
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            print("Tarea eliminada con éxito.")
            self.guardar_csv()
        else:
            print("Índice de tarea no válido.")

    def guardar_csv(self):
        #Metodo para guardar las tareas en un archivo csv
        with open (self.agenda_csv, mode = "w", newline = "", encoding = "utf-8") as agenda:
            escribir = csv.writer(agenda)
            escribir.writerow(["Descipcion", "Fecha", "Completada"])
            for tarea in self.tareas:
                escribir.writerow([tarea.descripcion, tarea.fecha, tarea.completada])
    
    def cargar_csv(self):
        #Metodo para cargar las tareas de un archivo csv
        if os.path.exists(self.agenda_csv):
            with open(self.agenda_csv, mode = "r", newline = "", encoding = "utf-8") as agenda:
                leer = csv.reader(agenda)
                next(leer)
                for fila in leer:
                    descripcion, fecha, completada = fila
                    completada = completada.lower() == "true" #Convertimos a booleano
                    self.tareas.append(Tarea(descripcion, fecha, completada))
            print(f"Tareas cargadas desde {self.agenda_csv}.")
        else:
            print(f"El archivo {self.agenda_csv} no existe. Se creara uno nuevo cuando guardes una tarea")



def mostrar_menu():
    #Funcion para mostrar el menu con las opciones
    print("\n--- Agenda de Tareas ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Modificar tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    #Funcion principal del programa
    agenda = Agenda() #Crear una instancia de la clase agenda

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha = input("Ingrese la fecha de la tarea en formato: DD/MM/AAAA:")
            agenda.agregar_tarea(descripcion, fecha)
        elif opcion == "2":
            agenda.mostrar_tareas()
        elif opcion == "3":
            agenda.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea modificar: ")) - 1
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_fecha = input("Ingrese la nueva fecha en formato DD/MM/AAAA:")
            agenda.modificar_tarea(indice, nueva_descripcion, nueva_fecha)
        elif opcion == "4":
            agenda.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            agenda.marcar_completada(indice)    
        elif opcion == "5":
            agenda.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            agenda.eliminar_tarea(indice)
        elif opcion == "6":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()