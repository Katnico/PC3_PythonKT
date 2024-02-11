def obtener_porcentaje(fraction):
    try:
        numerador, denominador = map(int, fraction.split('/'))

        if numerador <= denominador and denominador != 0:
            porcentaje = (numerador / denominador) * 100

            porcentaje_redondeado = round(porcentaje)

            if porcentaje_redondeado < 1:
                return 'E'
            elif porcentaje_redondeado > 99:
                return 'F'
            else:
                return f'{porcentaje_redondeado}%'
        else:
            return "X debe ser menor o igual a Y, y Y no puede ser cero."

    except ValueError:
        return "Debe ingresar números enteros separados por un '/'."
    except ZeroDivisionError:
        return "El denominador no puede ser cero."


def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        resultado = obtener_porcentaje(fraction)
        print("Resultado:", resultado)
        if resultado not in ['X debe ser menor o igual a Y, y Y no puede ser cero.',
                             "Debe ingresar números enteros separados por un '/'."]:
            break


if __name__ == "__main__":
    main()