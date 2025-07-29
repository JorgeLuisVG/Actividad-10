frutas = ["manzana", "banano", "naranja"]

eliminar = input("Ingrese el nombre de la fruta que desea eliminar: ").lower()

try:
    frutas.remove(eliminar)  # Esto lanza un ValueError si no existe
except ValueError:
    print("La fruta no existe")
finally:
    for i in frutas:
        print(i)
