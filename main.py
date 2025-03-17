from agenda import Agenda
from menu import mostrar_menu
from validaciones import validar_campo_no_vacio, validar_fecha, validar_hora, validar_numero_en_rango

# Función principal del programa
def main():
    agenda = Agenda()  # Crear una instancia de la agenda

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = validar_campo_no_vacio("Ingrese la descripción de la tarea: ")
            fecha = validar_fecha("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
            hora = validar_hora("Ingrese la hora de la tarea (HH:MM): ")
            idPrioridad = validar_numero_en_rango("Ingrese el ID de la prioridad (1. ALTA, 2. MEDIA, 3. BAJA): ", 1, 3)
            idCategoria = validar_numero_en_rango("Ingrese el ID de la categoría (1. ESCUELA, 2. TRABAJO, 3. CASA): ", 1, 3)
            idAgenda = validar_numero_en_rango("Ingrese el ID de la agenda: ", 1, 99)  # Ajusta el rango según tus necesidades
            agenda.agregar_tarea(descripcion, fecha, hora, idPrioridad, idCategoria, idAgenda)

        elif opcion == "2":
            agenda.mostrar_tareas()

        elif opcion == "3":
            idTarea = validar_numero_en_rango("Ingrese el ID de la tarea a modificar: ", 1, 99)  # Ajusta el rango según tus necesidades
            nueva_descripcion = validar_campo_no_vacio("Nueva descripción: ")
            nueva_fecha = validar_fecha("Nueva fecha (YYYY-MM-DD): ")
            nueva_hora = validar_hora("Nueva hora (HH:MM): ")
            nueva_prioridad = validar_numero_en_rango("Nuevo ID de prioridad (1. ALTA, 2. MEDIA, 3. BAJA): ", 1, 3)
            nueva_categoria = validar_numero_en_rango("Nuevo ID de categoría (1. ESCUELA, 2. TRABAJO, 3. CASA): ", 1, 3)
            agenda.modificar_tarea(idTarea, nueva_descripcion, nueva_fecha, nueva_hora, nueva_prioridad, nueva_categoria)

        elif opcion == "4":
            idTarea = validar_numero_en_rango("ID de la tarea a completar: ", 1, 1)
            agenda.marcar_completada(idTarea)

        elif opcion == "5":
            idTarea = validar_numero_en_rango("ID de la tarea a eliminar: ", 1, 999)
            agenda.eliminar_tarea(idTarea)

        elif opcion == "6":
            agenda.cerrar_conexion()
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
