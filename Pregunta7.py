import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


def main():

    punto1 = Punto(3, 4)
    punto2 = Punto(6, 8)

    distancia = punto1.distancia(punto2)

    print(f"La distancia entre los puntos {punto1} y {punto2} es: {distancia}")

if __name__ == "__main__":
    main()
