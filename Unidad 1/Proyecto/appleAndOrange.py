def countapplesAndOranges(s, t, a, b, apples, oranges):
    Manzanas_en_casa = 0
    for distancia in apples:
        posicion = a + distancia
        if s <= posicion <= t:
            Manzanas_en_casa += 1

    Naranjas_en_casa = 0
    for distancia in oranges:
        posicion = b + distancia
        if s <= posicion <= t:
            Naranjas_en_casa += 1

    print(Manzanas_en_casa)
    print(Naranjas_en_casa)

# Leer entrada
s, t = map(int, input("Ingrese s y t separados por espacio: ").split())
a, b = map(int, input("Ingrese a y b separados por espacio: ").split())
m, n = map(int, input("Ingrese m y n separados por espacio: ").split())
apples = list(map(int, input(f"Ingrese {m} distancias de manzanas separadas por espacio: ").split()))
oranges = list(map(int, input(f"Ingrese {n} distancias de naranjas separadas por espacio: ").split()))

countapplesAndOranges(s, t, a, b, apples, oranges)


    