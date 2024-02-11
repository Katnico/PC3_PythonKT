class CalificacionesManager:
    def __init__(self):
        self.calificaciones = []

    def ingresar_calificaciones(self, calificaciones_str):
        try:
            calificaciones_lista = calificaciones_str.split(',')
            for calificacion in calificaciones_lista:
                calificacion_entero = int(calificacion.strip())
                self.calificaciones.append(calificacion_entero)
            return True
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")
            return False

    def obtener_calificaciones(self):
        return self.calificaciones


def main():
    calificaciones_manager = CalificacionesManager()
    while True:
        calificaciones_str = input("Ingrese una lista de calificaciones separadas por comas: ")
        if calificaciones_manager.ingresar_calificaciones(calificaciones_str):
            break

    print("Calificaciones (enteros):", calificaciones_manager.obtener_calificaciones())


if __name__ == "__main__":
    main()