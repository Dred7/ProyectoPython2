# Definición de la clase Tarea
class Tarea:
    def __init__(self, idTarea, descripcion, fechaEntrega, horaEntrega, idPrioridad, idCategoria, idAgenda, completada=False):
        # Constructor de la clase Tarea
        self.idTarea = idTarea
        self.descripcion = descripcion
        self.fechaEntrega = fechaEntrega
        self.horaEntrega = horaEntrega
        self.completada = completada
        self.idPrioridad = idPrioridad
        self.idCategoria = idCategoria
        self.idAgenda = idAgenda
        
    def __str__(self):
        # Representa la tarea como una cadena de texto
        estado = "Completada" if self.completada else "Pendiente"
        return (
            f"Tarea {self.idTarea}: {self.descripcion} "
            f"(Fecha: {self.fechaEntrega}, Hora: {self.horaEntrega}, "
            f"Estado: {estado}, Prioridad ID: {self.idPrioridad}, "
            f"Categoría ID: {self.idCategoria}, Agenda ID: {self.idAgenda})"
        )