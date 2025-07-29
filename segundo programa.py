try :
    numero = int(input("Ingrese un numero: "))
except ValueError:
    print("debe ingresar un numero")
else:
    numero *= 3
    print(numero)