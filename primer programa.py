colores = ["rojo", "Verde", "azul"]

try:
    num = int(input("ingrese un numero entre 0 y 2"))

    print(f"{colores[num]}")
except ValueError:
    print("Ingrese un numero")
except IndexError:
    print("Está fuera del rango")
finally:
    print("gracias por utilizar este programa")