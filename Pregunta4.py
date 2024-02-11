class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

def main():

    rectangulo1 = Rectangulo(6, 2)

    area = rectangulo1.calcular_area()

    print("El área del rectángulo es:", area)

if __name__ == "__main__":
    main()
