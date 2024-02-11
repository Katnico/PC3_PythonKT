import random

def generar_numeros_aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    print("Lista de números generados aleatoriamente:")
    print(lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)

 