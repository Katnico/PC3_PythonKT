import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

def main():
    circulo1 = Circulo(7)

    area = circulo1.calcular_area()

    print("El área del círculo es:", area)

if __name__ == "__main__":
    main()
