class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


def main():

    catalogo = Catalogo()

    producto1 = Producto("Llanta", 80, 2021)
    producto2 = Producto("Batería", 100, 2023)
    producto3 = Producto("Filtro de aire", 25, 2022)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_productos()

    catalogo.filtrar_por_año(2023)


if __name__ == "__main__":
    main()
