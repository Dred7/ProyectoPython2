class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class Agenda:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada con éxito.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la agenda.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def modificar_tarea(self, indice, nueva_descripcion):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].descripcion = nueva_descripcion
            print("Tarea modificada con éxito.")
        else:
            print("Índice de tarea no válido.")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print("Tarea marcada como completada.")
        else:
            print("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            print("Tarea eliminada con éxito.")
        else:
            print("Índice de tarea no válido.")

def mostrar_menu():
    print("\n--- Agenda de Tareas ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Modificar tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            agenda.agregar_tarea(descripcion)
        elif opcion == "2":
            agenda.mostrar_tareas()
        elif opcion == "3":
            agenda.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea modificar: ")) - 1
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            agenda.modificar_tarea(indice, nueva_descripcion)
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