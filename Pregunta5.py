class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas.extend(notas)


def main():

    alumno1 = Alumno("Luis Rojas", "2021001")

    alumno1.display()

    alumno1.set_edad(20)

    alumno1.set_notas(20, 15, 11)

    alumno1.display()


if __name__ == "__main__":
    main()