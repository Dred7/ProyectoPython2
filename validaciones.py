from datetime import datetime

# Función para validar que un campo no esté vacío
def validar_campo_no_vacio(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip():  # Verifica que el campo no esté vacío
            return valor
        print("Error: Este campo no puede estar vacío. Intente de nuevo.")

# Función para validar el formato de la fecha (YYYY-MM-DD)
def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje)
        try:
            fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%d")  # Intenta convertir la fecha
            fecha_actual = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Fecha actual sin hora
            
            if fecha_ingresada < fecha_actual:
                print("Error: La fecha no puede ser menor a la fecha actual. Intente de nuevo.")
            else:
                return fecha
        except ValueError:
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD. Intente de nuevo.")

# Función para validar el formato de la hora (HH:MM)
def validar_hora(mensaje):
    while True:
        hora = input(mensaje)
        try:
            datetime.strptime(hora, "%H:%M")  # Intenta convertir la hora
            return hora
        except ValueError:
            print("Error: Formato de hora incorrecto. Use HH:MM. Intente de nuevo.")

# Función para validar que un número esté dentro de un rango
def validar_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Error: El número debe estar entre {minimo} y {maximo}. Intente de nuevo.")
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente de nuevo.")