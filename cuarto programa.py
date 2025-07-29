peliculas = {
    "Matrix": 1999,
    "Inception": 2010,
    "Interstellar": 2014
}

buscar = input("Ingrese una película: ").title()

try:
    año = peliculas[buscar]  # Esto lanza un KeyError si no existe
    print(f"Pelicula: {buscar}, año: {año}")
except KeyError:
    print("La película no existe")
    